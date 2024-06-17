from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import ReportLog
from scan.utils import get_filters, get_datetime, table_data, print_params


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/report/index.html")


@require_http_methods(["GET", "POST"])
def add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/report/add.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Params"), ["name"])
    result = ReportLog.objects.filter(**filters).order_by("-id")
    fields = ["id", "name", "url", "create_time"]
    return table_data(request, result, fields)


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    ReportLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = ReportLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = ReportLog.objects.get(id=id)
        return success_api(data)
    except ReportLog.DoesNotExist:
        return fail_api("未找到该记录")


@require_http_methods(["POST"])
def download(request: HttpRequest):
    id = request.POST.get("id")
    ReportLog.objects.filter(id=id).delete()
    return success_api()
