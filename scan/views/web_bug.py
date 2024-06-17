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
    get_delete_param,
)


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/web_bug/index.html")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/web_bug/start.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Param"), [])
    result = WebBugLog.objects.filter(**filters).order_by("-id")
    fields = [
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
    return table_data(request, result, fields)


def stop(request: HttpRequest):
    print_params(request)
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id_ = request.POST.get("id")
    WebBugLog.objects.filter(id=id_).delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    # 获取参数
    ids_list = get_delete_param(request)
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
