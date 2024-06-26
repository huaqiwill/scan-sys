from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from common.API.json_result import success_api, fail_api
from scan.utils.report.aev4 import get_local_ip
from scan.utils.scanning.host import start_host_scan, stop_host_scan
from scan.models import HostLog
from scan.utils import get_filters, table_data, print_params, get_item, get_form

result_fields = ["id", "ip", "mac", "os", "supplier", "start_time", "end_time", "name"]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/host/index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Params"), ["ip"])
    result = HostLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        context = {
            "local_ip": get_local_ip()
        }
        return render(request, "scan/host/start.html", context=context)

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
def delete_batch(request: HttpRequest):
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


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = HostLog.objects.get(id=id)
        context = {
            "host": get_item(obj, result_fields)
        }
        return render(request, "scan/host/add.html", context)

    form = get_form(request.POST, ["id", "ip", "name", "os", "mac", "supplier"])
    HostLog.objects.filter(id=form["id"]).update(**form)
    return success_api()
