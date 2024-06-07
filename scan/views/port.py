import json

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.models import PortLog
from scan.utils.scanning import start_port_scan, stop_port_scan
from scan.utils import get_filters


def index(request: HttpRequest):
    return render(request, "scan/scanning/port-index.html")


def query(request: HttpRequest):
    print("端口扫描数据库查询", request.POST)
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    filters = get_filters(request.POST.get("Params"), ["host"])

    ports = PortLog.objects.filter(**filters).all()
    page_data = Paginator(ports, limit).page(page)

    count = len(ports)
    data_list = []
    for port in page_data:
        data_list.append({
            "id": port.id,
            "host": port.host,
            "ports": port.ports,
        })
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/port-start.html")

    print("请求参数", request.POST)

    host = request.POST.get("host")
    start_port = request.POST.get("start_port")
    end_port = request.POST.get("end_port")

    start_port_scan(host, start_port, end_port)

    return res_josn_data.success_api("端口扫描任务开始")


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print("端口扫描：", request.POST)
    stop_port_scan()
    return res_josn_data.success_api()

@require_http_methods(["POST"])
def delete(request: HttpRequest):
    print("查询参数", request.POST)
    id = request.POST.get("id")
    PortLog.objects.filter(id=id).delete()
    return res_josn_data.success_api("删除成功")
