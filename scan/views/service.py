import json

from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.utils.scanning import start_service_discovery

def index(request: HttpRequest):
    print("服务识别")
    return render(request, "scan/scanning/service-found-index.html")


def start(request: HttpRequest):
    return render(request, "scan/scanning/service-found-add.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
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
