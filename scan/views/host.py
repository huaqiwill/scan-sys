import json

from django.shortcuts import render
from django.http import HttpRequest
from django.views.decorators.http import require_http_methods
from common.API import res_josn_data
from scan.utils.scanning import start_host_scan, stop_host_scan
from scan.models import HostLog


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/scanning/host-index.html")


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print("查询参数", request.POST)
    params = request.POST.get("Params", None)
    if params:
        req = json.loads(params)
        print("查询参数", req)

    host_log_list = HostLog.objects.all()
    count = len(host_log_list)
    data_list = []
    for host_log in host_log_list:
        data = {
            "ip": host_log["ip"],
            "mac": host_log["mac"],
            "os": host_log["os"],
            "supplier": host_log["vendor"],
            "start_time": host_log["start_time"],
            "end_time": host_log["end_time"]
        }
        data_list.append(data)
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/host-start.html")
    print("查询参数", request.POST)
    start_host_scan()
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def stop(request: HttpRequest):
    print("查询参数", request.POST)
    stop_host_scan()
    return res_josn_data.success_api()
