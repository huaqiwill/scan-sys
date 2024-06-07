from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.models import ReportLog
from scan.utils import get_filters, get_datetime


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/report/report-index.html")


@require_http_methods(["GET", "POST"])
def add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/report/report-add.html")

    print("请求参数", request.POST)


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print("请求参数", request.POST)
    page = request.POST.get("page")
    limit = request.POST.get("limit")
    filters = get_filters(request.POST.get("Params"), ["name"])

    bugs = ReportLog.objects.filter(**filters).all()
    page_data = Paginator(bugs, limit).page(page)

    count = len(bugs)
    data_list = []
    for bug in page_data:
        data_list.append({
            "id": bug.id,
            "name": bug.name,
            "url": bug.url,
            "create_time": get_datetime(bug.create_time),
        })
    return res_josn_data.table_api(count=count, data=data_list)


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    print("查询参数", request.POST)
    id = request.POST.get("id")
    ReportLog.objects.filter(id=id).delete()
    return res_josn_data.success_api("删除成功")
