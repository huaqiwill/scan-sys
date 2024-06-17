from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from common.API.json_result import success_api, fail_api
from scan.utils.scanning import start_host_scan, stop_host_scan
from scan.models import HostLog
from scan.utils import get_filters, table_data, print_params


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/host/index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Params"), ["ip"])
    result = HostLog.objects.filter(**filters).order_by("-id")
    fields = ["id", "ip", "mac", "os", "supplier", "start_time", "end_time"]
    return table_data(request, result, fields)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/host/start.html")

    print_params(request)
    start_host_scan()
    return success_api()


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print_params(request)
    stop_host_scan()
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    HostLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def deleteBatch(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = HostLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = HostLog.objects.get(id=id)
        return success_api(data)
    except HostLog.DoesNotExist:
        return fail_api("未找到该记录")
