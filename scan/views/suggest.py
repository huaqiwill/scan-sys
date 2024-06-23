from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api, table_api
from scan.models import SuggestLog
from scan.utils import get_filters, table_data, get_form, get_item, get_batch_delete_param

result_fields = ["id", "name_en", "name_cn", "risk", "describe", "solution", "cve", "is_update"]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/suggest/index.html")


@require_http_methods(["GET", "POST"])
def add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/suggest/add.html")

    form = get_form(request.POST, ["name_en", "name_cn", "risk", "describe", "solution", "cve", "is_update"])
    SuggestLog.objects.create(**form)
    return success_api()


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = SuggestLog.objects.get(id=id)
        context = {
            "suggest": get_item(obj, result_fields)
        }
        return render(request, "scan/suggest/add.html", context)

    form = get_form(request.POST, ["id", "name_en", "name_cn", "risk", "describe", "solution", "cve", "is_update"])
    obj = SuggestLog.objects.get(id=form["id"])
    obj.name_en = form["name_en"]
    obj.name_cn = form["name_cn"]
    obj.risk = form["risk"]
    obj.describe = form["describe"]
    obj.solution = form["solution"]
    obj.cve = form["cve"]
    obj.is_update = form["is_update"]
    obj.save()
    return success_api()


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Param"), [])
    result = SuggestLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    SuggestLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def delete_batch(request: HttpRequest):
    ids_list = get_batch_delete_param(request.POST)
    objects_to_delete = SuggestLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    obj = SuggestLog.objects.get(id=id)
    return success_api(get_item(obj, result_fields))
