import json

from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from common.API import res_josn_data
from scan.utils.scanning import start_host_scan, stop_host_scan
from scan.models import HostLog
from scan.utils import get_filters, get_datetime


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/scanning/host-index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print("查询参数", request.POST)
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    filters = get_filters(request.POST.get("Params"), ["ip"])

    host_log_list = HostLog.objects.filter(**filters).all()
    page_data = Paginator(host_log_list, limit).page(page)

    count = len(host_log_list)
    data_list = []
    for host_log in page_data:
        data = {
            "id": host_log.id,
            "ip": host_log.ip,
            "mac": host_log.mac,
            "os": host_log.os,
            "supplier": host_log.supplier,
            "start_time": get_datetime(host_log.start_time),
            "end_time": host_log.end_time
        }
        data_list.append(data)
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/host-start.html")

    print("请求参数", request.POST)
    start_host_scan()
    return res_josn_data.success_api("主机发现任务开始")


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print("查询参数", request.POST)
    stop_host_scan()
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    print("查询参数", request.POST)
    id = request.POST.get("id")
    HostLog.objects.filter(id=id).delete()
    return res_josn_data.success_api("删除成功")
