import json
from datetime import datetime

from django.shortcuts import render
from django.core.paginator import Paginator
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from common.API.auth import login_required
from .models import Monitor, Notify, SubEmail, Handle
from django.http import JsonResponse, HttpResponse
from .utils import sqlbak
import psutil
from .forms import NotifyForm, SubEmailForm
from django.shortcuts import get_object_or_404, redirect
from .utils import json_response


def ratelimit_handler(request):
    """访问限制处理工具"""
    return HttpResponse("访问过于频繁，请稍后再试")


"""
事件监控预警
"""


@login_required
@require_http_methods(["GET", "POST"])
def monitor(request):
    """事件监控预警"""
    return render(request, "monitor/monitor.html")

def index(request):
    return render(request, 'monitor/index.html')

def get_system_info(request):
    cpu_percent = psutil.cpu_percent(percpu=True)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage('/')
    net_io = psutil.net_io_counters()

    data = {
        'cpu_percent': cpu_percent,
        'memory': {
            'total': memory_info.total,
            'used': memory_info.used,
            'free': memory_info.available,
            'percent': memory_info.percent,
        },
        'disk': {
            'total': disk_usage.total,
            'used': disk_usage.used,
            'free': disk_usage.free,
            'percent': disk_usage.percent,
        },
        'network': {
            'bytes_sent': net_io.bytes_sent,
            'bytes_recv': net_io.bytes_recv,
        }
    }
    
    return JsonResponse(data)


@login_required
@require_http_methods(["GET", "POST"])
def monitor_query(request):
    """监控预警查询"""
    # if request.method != "POST":
    #     return res_josn_data.fail_api("不支持的请求格式")

    # 获取必填参数
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    user_obj = Monitor.objects.filter().order_by("id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    return res_josn_data.table_api(count=len(user_obj), data=page_data)


@login_required
@require_http_methods(["GET", "POST"])
def monitor_delete(request):
    return res_josn_data.success_api("success")


@login_required
@require_http_methods(["GET", "POST"])
def monitor_dashboard(request):
    return render(request, "monitor/dashboard.html")


@login_required
@require_http_methods(["GET", "POST"])
def monitor_get_system_data(request):
    cpu_usage = psutil.cpu_percent(interval=1)
    memory_info = psutil.virtual_memory()
    disk_usage = psutil.disk_usage("/")
    system_data = {
        "cpu_usage": cpu_usage,
        "memory_usage": memory_info.percent,
        "disk_usage": disk_usage.percent,
    }
    return JsonResponse(system_data)


"""
安全事件通报
"""


@login_required
@require_http_methods(["GET", "POST"])
def notify(request):
    """通知管理"""
    # EMail().send_email()
    return render(request, "monitor/notify.html")


@login_required
@require_http_methods(["GET", "POST"])
def notify_query(request):
    notifies = Notify.objects.all()
    print(notifies)
    data_list = []
    for notify_ in notifies:
        data_list.append({
            "id": notify_.id,
            "notify_type": notify_.notify_type,
            "notify_mail": notify_.notify_mail,
            "notify_subject": notify_.notify_subject,
            "notify_content": notify_.notify_content,
            "notify_time": notify_.notify_time,
            "notify_status": notify_.notify_status,
        })
    print(data_list)
    return res_josn_data.table_api(count=10, data=data_list)


@login_required
@require_http_methods(["POST"])
def notify_delete(request):
    Notify.objects.filter(id=request.POST.get("id")).delete()
    return res_josn_data.success_api("刪除成功")


@login_required
@require_http_methods(["GET", "POST"])
def sub_email(request):
    """
    订阅列表页面
    """
    return render(request, "monitor/sub_email.html")


from .utils.serializer import SubEmailSerializer


@login_required
@require_http_methods(["POST"])
def sub_email_query(request):
    """
    订阅列表查询
    """
    sub_emails = SubEmail.objects.all()

    data_list = []
    for email in sub_emails:
        email_dict = {
            "id": email.id,
            "sub_name": email.sub_name,
            "sub_email": email.sub_email,
            "sub_status": email.sub_status,
            "sub_date": email.sub_date,
            "user_id": email.user_id,
        }
        data_list.append(email_dict)

    return res_josn_data.table_api(count=10, data=data_list)


@login_required
@require_http_methods(["GET", "POST"])
def sub_email_add(request):
    """
    订阅列表添加
    """
    if request.method == "GET":
        return render(request, "monitor/sub_email_add.html")
    else:
        try:
            sub_name = request.POST.get("sub_name")
            sub_email_ = request.POST.get("sub_email")
            sub_status = request.POST.get("sub_status")
            sub_date = datetime.now()
            user_id = 1
            email = SubEmail.objects.create(sub_name=sub_name, sub_email=sub_email_, sub_status=sub_status,
                                            sub_date=sub_date, user_id=user_id)
            if email.id is not None:
                return res_josn_data.success_api("添加成功")
        except:
            pass

        return res_josn_data.fail_api("添加失败")


@login_required
@require_http_methods(["GET", "POST"])
def sub_email_delete(request):
    """
    删除订阅记录
    """
    sub_email_ = request.POST["sub_email"]
    print(sub_email_)
    SubEmail.objects.filter(sub_email=sub_email_).delete()
    return res_josn_data.success_api(f"订阅邮件:{sub_email_} 删除成功")


def to_dict(**kwargs):
    pass


@login_required
@require_http_methods(["GET", "POST"])
def sub_email_edit(request):
    """
    修改订阅信息
    """
    print("AJAX数据:", request.POST)
    sub_name = request.POST["sub_name"]
    sub_email_ = request.POST["sub_email"]
    sub_status = request.POST["sub_status"]
    SubEmail.objects.filter(sub_email=sub_email_).update(sub_name=sub_name, sub_status=sub_status,
                                                         sub_email=sub_email_)
    return res_josn_data.success_api(f"更新成功")


"""
应急响应处置
"""


@login_required
@require_http_methods(["GET", "POST"])
def handle(request):
    """
    应急响应处置页面
    """
    return render(request, "monitor/handle.html")


@login_required
@require_http_methods(["POST"])
def handle_query(request):
    """
    应急响应处置查询
    """
    handles = Handle.objects.all()
    data_list = []
    for handle_ in handles:
        data_list.append({
            "id": handle_.id,
            "request_time": handle_.request_time,
            "request_method": handle_.request_method,
            "request_path": handle_.request_path,
            "response_status": handle_.response_status,
            "response_time": handle_.response_time,
            "disposal_time": handle_.disposal_time,
            "source_ip": handle_.source_ip,
            "attack_type": handle_.attack_type,
            "details": handle_.details,
        })
    return res_josn_data.table_api(count=10, data=data_list)


@login_required
@require_http_methods(["GET", "POST"])
def handle_delete(request):
    """
    应急响应处置删除
    """
    handle_id = request.POST["id"]
    print(handle_id)
    SubEmail.objects.filter(id=handle_id).delete()
    return res_josn_data.success_api("刪除成功")


"""
数据业务恢复
"""


@login_required
@require_http_methods(["GET", "POST"])
def restore(request):
    """
    业务数据恢复页面
    """
    return render(request, "monitor/restore.html")


@login_required
@require_http_methods(["GET", "POST"])
def restore_query(request):
    """
    业务数据恢复列表查询
    """
    return res_josn_data.success_api("success")


@login_required
@require_http_methods(["GET", "POST"])
def restore_delete(request):
    """
    删除业务数据恢复记录
    """
    return res_josn_data.success_api("success")
