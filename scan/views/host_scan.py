import json

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods

# Create your views here.
from common.API import res_josn_data
from scan.utils.scanning import start_host_discovery
from scan.models import PortScan


def index(request: HttpRequest):
    return render(request, "scan/index.html")


def check(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-index.html")


def check_add(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-add.html")


@require_http_methods(["GET", "POST"])
def found(request: HttpRequest):
    print("主机发现")
    if request.method == "GET":
        return render(request, "scan/scanning/host-found-index.html")
    print("主机发现")


@require_http_methods(["GET", "POST"])
def found_add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/host-found-add.html")

    print("查询参数", request.POST)
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def found_query(request: HttpRequest):
    """主机发现"""
    print("查询参数", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    devices = start_host_discovery()

    print("查询")
    count = 1
    data_list = []
    for device in devices:
        print(device)
        data_list.append({
            "ip": device["ip"],
            "mac": device["mac"],
            "os": "Windows 10",
            "supplier": "Unknown"
        })
    return res_josn_data.table_api(count=count, data=data_list)


def server(request: HttpRequest):
    print("服务识别")
    return render(request, "scan/scanning/service-found-index.html")


def server_add(request: HttpRequest):
    return render(request, "scan/scanning/service-found-add.html")


from scan.utils.scanning import start_service_discovery


@require_http_methods(["POST"])
def server_query(request: HttpRequest):
    print("服务识别--query 参数：", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    count = 1
    data_list = []
    services = start_service_discovery()
    print(services)
    for service in services:
        data_list.append({
            "host": service["ip"],
            "port": service["port"],
            "service": service["service"],
            "version": service["version"],
            "protocol": service["protocol"],
            "state": service["state"],
            "product": service["product"]
        })
    return res_josn_data.table_api(count=1, data=data_list)


def port(request: HttpRequest):
    return render(request, "scan/scanning/port-found-index.html")


from scan.utils.scanning import start_port_scan


def port_query(request: HttpRequest):
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
def port_add(request: HttpRequest):
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
