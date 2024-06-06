import json

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.utils.scanning import start_port_scan


def index(request: HttpRequest):
    return render(request, "scan/scanning/port-found-index.html")


def query(request: HttpRequest):
    print("服务识别--query 参数：", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    count = 1
    data_list = []
    ports = start_port_scan()
    print(ports)
    for port in ports:
        data_list.append({
            "ports": port["ports"],
            "host": port["host"],
        })
    return res_josn_data.table_api(count=1, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/port-found-add.html")

    print("端口扫描：", request.POST)

    data_list = []
    ports = start_port_scan()
    print(ports)
    for service in ports:
        data_list.append({
            "port": service["port"],
            "state": service["state"],
            "host": service["host"],
        })

    return res_josn_data.success_api()
