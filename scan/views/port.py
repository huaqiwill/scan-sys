from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import PortLog
from scan.utils.scanning import start_port_scan, stop_port_scan
from scan.utils import get_filters, print_params, table_data


def index(request: HttpRequest):
    return render(request, "scan/port/index.html")


def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Params"), ["host"])
    result = PortLog.objects.filter(**filters).order_by("-id")
    fields = ["id", "host", "ports"]
    return table_data(request, result, fields)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/port/start.html")

    host = request.POST.get("host")
    start_port = request.POST.get("start_port")
    end_port = request.POST.get("end_port")

    start_port_scan(host, start_port, end_port)

    return success_api()


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    stop_port_scan()
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    PortLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = PortLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = PortLog.objects.get(id=id)
        return success_api(data)
    except PortLog.DoesNotExist:
        return fail_api("未找到该记录")
