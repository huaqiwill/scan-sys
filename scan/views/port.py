import json

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.models import PortLog
from scan.utils.scanning import start_port_scan, stop_port_scan


def index(request: HttpRequest):
    return render(request, "scan/scanning/port-index.html")


def query(request: HttpRequest):
    print("服务识别--query 参数：", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    ports = PortLog.objects.all()
    count = len(ports)
    data_list = []
    for port in ports:
        data_list.append({
            "host": port["host"],
            "ports": port["ports"],
        })
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/port-start.html")

    print("端口扫描：", request.POST)
    start_port_scan()
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print("端口扫描：", request.POST)
    stop_port_scan()
    return res_josn_data.success_api()
