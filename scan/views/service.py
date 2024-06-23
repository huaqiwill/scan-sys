from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from common.API.json_result import success_api, fail_api
from scan.models import ServiceLog
from scan.utils.scanning.service import start_service_scan, stop_service_scan, get_local_ip
from scan.utils import get_filters, print_params, table_data, get_item, get_form

result_fields = [
    "id",
    "ip",
    "port",
    "service",
    "version",
    "protocol",
    "state",
    "product",
    "notes"
]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/service/index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print_params(request)
    fields = ["ip", "port", "protocol", "state", "product"]
    filters = get_filters(request.POST.get("Params"), fields)
    result = ServiceLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        context = {
            "local_ip": get_local_ip()
        }
        return render(request, "scan/service/start.html", context=context)

    ip = request.POST.get("ip")
    start_service_scan(ip)
    return success_api("服务识别任务开始")


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    stop_service_scan()
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    ServiceLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def delete_batch(request: HttpRequest):
    ids = request.POST.get("ids")
    ids_list = ids.split(",")
    objects_to_delete = ServiceLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = ServiceLog.objects.get(id=id)
        return success_api(data)
    except ServiceLog.DoesNotExist:
        return fail_api("未找到该记录")


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = ServiceLog.objects.get(id=id)
        context = {
            "service": get_item(obj, result_fields)
        }
        return render(request, "scan/service/add.html", context)

    form = get_form(request.POST, ["id", "ip", "port", "protocol", "service", "version", "state", "product", "notes"])
    ServiceLog.objects.filter(id=form["id"]).update(**form)
    return success_api()
