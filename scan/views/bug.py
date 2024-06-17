from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import BugLog
from scan.utils import get_filters, get_datetime, print_params, table_data


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/bug/index.html")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/bug/start.html")



@require_http_methods(["POST"])
def query(request: HttpRequest):
    print_params(request)
    filters = get_filters(request.POST.get("Param"), [])
    result = BugLog.objects.filter(**filters).order_by("-id")
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
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = BugLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    id = request.POST.get("id")
    BugLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = BugLog.objects.get(id=id)
        return success_api(data)
    except BugLog.DoesNotExist:
        return fail_api("未找到该记录")
