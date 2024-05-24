from django.shortcuts import render
from django.core.paginator import Paginator
from .utils.mail import EMail
from common.API import res_josn_data
from common.API.auth import authorize, login_required
from login.models import Log
import json
from .models import Monitor, Notify
from django.http import JsonResponse


def ratelimit_handler(request):
    return JsonResponse({"error": "Too many requests. Please try again later."})


# Create your views here.
@login_required
def monitor(request):
    return render(request, "monitor/monitor.html")

@login_required
def monitor_query(request):
    if request.method != "POST":
        return res_josn_data.fail_api("不支持的请求格式")

    data_list = []
    # 获取必填参数
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    user_obj = Monitor.objects.filter().order_by("id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    for item in page_data:
        count += 1
        item_data = {
            "id": count,
            "fieldID": item.id,
            "userID": item.id_number,
            "name": item.user_name,
            "department": item.department,
            "position": item.position,
            "email": item.email,
            "status": item.user_status,
            "role": item.role_des,
        }
        data_list.append(item_data)

    return res_josn_data.table_api(count=len(user_obj), data=data_list)


def monitor_delete(request):
    return res_josn_data.success_api("success")


@login_required
def notify(request):
    # EMail().send_email()
    return render(request, "monitor/notify.html")


def notify_query(request):
    return res_josn_data.success_api("success")


def notify_delete(request):
    return res_josn_data.success_api("success")


@login_required
def handle(request):
    return render(request, "monitor/handle.html")


def handle_query(request):
    return res_josn_data.success_api("success")


def handle_delete(request):
    return res_josn_data.success_api("success")


@login_required
def recover(request):
    return render(request, "monitor/recover.html")


def recover_query(request):
    return res_josn_data.success_api("success")


def recover_delete(request):
    return res_josn_data.success_api("success")
