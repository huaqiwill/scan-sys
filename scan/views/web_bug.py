import datetime
import json
import random

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from scan.models import WebBugLog
from scan.utils import (
    get_filters,
    print_params,
    table_data,
    success_api,
    fail_api,
    get_delete_param, get_form, get_item, get_batch_delete_param,
)
from scan.utils.scanning import get_local_ip

result_fields = [
    "id",
    "name",
    "os",
    "found_by",
    "found_time",
    "bug_type",
    "bug_name",
    "bug_level",
    "bug_url",
    "bug_status",
    "notes",
]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/web_bug/index.html")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/web_bug/start.html")

    print(request.POST)
    form = get_form(request.POST, ["url", "range", "type", "token", "strategy"])
    print(form)

    size = random.randint(1, 10)
    bug_type = ["弱口令", "弱密码", "SQL注入", "文件上传漏洞", "远程命令注入", "目录遍历", "源码泄露", "CSRF注入", "XSS攻击", "Dos攻击"]
    bug_level = ["低级", "中级", "高级", "紧急", "建议", "轻松", "非常紧急", "重大损失"]
    log_inf = ["待跟进", "unknown", "未知的", "正在进一步操作"]
    for i in range(0, size):
        save_form = json.dumps(form)
        load_form = json.loads(save_form)
        load_form["name"] = load_form["type"]
        load_form["os"] = "windows 10"
        load_form["found_by"] = get_local_ip()
        load_form["found_time"] = datetime.datetime.now()
        load_form["bug_type"] = random.choice(bug_type)
        load_form["bug_name"] = load_form["type"]
        load_form["bug_level"] = random.choice(bug_level)
        load_form["bug_url"] = load_form["url"]
        load_form["bug_status"] = random.choice(log_inf)
        load_form["notes"] = load_form["token"]
        load_form.pop("url")
        load_form.pop("range")
        load_form.pop("type")
        load_form.pop("token")
        load_form.pop("strategy")
        WebBugLog.objects.create(**load_form)
    return success_api()


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Param"), [])
    result = WebBugLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


def stop(request: HttpRequest):
    print_params(request)
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id_ = request.POST.get("id")
    WebBugLog.objects.filter(id=id_).delete()
    return success_api()


@require_http_methods(["POST"])
def delete_batch(request: HttpRequest):
    # 获取参数
    ids_list = get_batch_delete_param(request.POST)
    # 执行批量删除操作
    objects_to_delete = WebBugLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    # 执行完成
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id_ = request.POST.get("id")
    try:
        web_bug_log = WebBugLog.objects.get(id=id_)
        return success_api(web_bug_log)
    except WebBugLog.DoesNotExist:
        return fail_api("未找到该记录")


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = WebBugLog.objects.get(id=id)
        context = {
            "webbug": get_item(obj, result_fields)
        }
        return render(request, "scan/web_bug/add.html", context)

    form = get_form(request.POST,
                    ["id", "name", "os", "found_by", "bug_type", "bug_name", "bug_level", "bug_url", "bug_status",
                     "notes"])
    WebBugLog.objects.filter(id=form["id"]).update(**form)
    return success_api()
