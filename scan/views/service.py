import json

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods
from common.API import res_josn_data
from scan.models import ServiceLog
from scan.utils.scanning import start_service_scan, stop_service_scan
from scan.utils import get_filters


@require_http_methods(["GET"])
def index(request: HttpRequest):
    print("服务识别")
    return render(request, "scan/scanning/service-index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print("请求参数", request.POST)
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    filters = get_filters(request.POST.get("Params"), ["ip", "port", "protocol", "state", "product"])

    services = ServiceLog.objects.filter(**filters).all()
    page_data = Paginator(services, limit).page(page)

    count = len(services)
    data_list = []
    for service in page_data:
        data_list.append({
            "id": service.id,
            "host": service.ip,
            "port": service.port,
            "service": service.service,
            "version": service.version,
            "protocol": service.protocol,
            "state": service.state,
            "product": service.product
        })
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/service-start.html")

    print("请求参数", request.POST)
    ip = request.POST.get("ip")
    start_service_scan(ip)
    return res_josn_data.success_api("服务识别任务开始")


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    stop_service_scan()
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    print("查询参数", request.POST)
    id = request.POST.get("id")
    ServiceLog.objects.filter(id=id).delete()
    return res_josn_data.success_api("删除成功")
