import datetime
import json

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from common.API import res_josn_data
from scan.utils.scanning import start_host_discovery
from scan.models import HostLog


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/scanning/host-found-index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    """主机发现"""
    print("查询参数", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    start_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    devices = start_host_discovery()
    end_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # 转换成字典类型的数据并且返回
    count = 1
    data_list = []
    for device in devices:
        print(device)
        data = {
            "ip": device["ip"],
            "mac": device["mac"],
            "os": device["os"],
            "supplier": device["vendor"],
            "start_time": start_time,
            "end_time": end_time
        }
        data_list.append(data)
        # 扫描结果保存到数据库
        HostLog.objects.create(*data)

    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/host-found-add.html")

    print("查询参数", request.POST)
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print("查询参数", request.POST)
    return res_josn_data.success_api()
