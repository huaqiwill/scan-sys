from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import BugLog
from scan.utils import get_filters, get_datetime, print_params, table_data, get_form, get_item

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
    return render(request, "scan/bug/index.html")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/bug/start.html")

    form = get_form(request.POST, ["url", "range", "type", "token", "strategy"])

    return success_api()


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print_params(request)
    filters = get_filters(request.POST.get("Param"), [])
    result = BugLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


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
def delete_batch(request: HttpRequest):
    id = request.POST.get("id")
    BugLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    data = BugLog.objects.get(id=id)
    return success_api(get_item(data, result_fields))


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/port/add.html")

    form = get_form(request.POST, ["id"])
    obj = BugLog.objects.get(id=form["id"])
    obj.name = form["name"]
    obj.save()
    return success_api()
