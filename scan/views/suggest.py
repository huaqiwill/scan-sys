from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api, table_api
from scan.models import SuggestLog
from scan.utils import get_filters, table_data


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/suggest/index.html")


@require_http_methods(["GET", "POST"])
def add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/suggest/add.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Param"), [])
    result = SuggestLog.objects.filter(**filters).order_by("-id")
    fields = [
        "id",
        "name_en",
        "name_cn",
        "risk",
        "describe",
        "solution",
        "cve",
        "is_update",
    ]
    return table_data(request, result, fields)


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    SuggestLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = SuggestLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        web_bug_log = SuggestLog.objects.get(id=id)
        return success_api(web_bug_log)
    except SuggestLog.DoesNotExist:
        return fail_api("未找到该记录")
