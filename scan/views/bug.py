from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API import res_josn_data
from scan.models import BugLog
from scan.utils import get_filters, get_datetime


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/scanning/bug-index.html")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/scanning/bug-start.html")

    print("请求参数", request.POST)


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print("请求参数", request.POST)
    page = request.POST.get("page")
    limit = request.POST.get("limit")
    filters = get_filters(request.POST.get("Param"), [])

    bugs = BugLog.objects.filter(**filters).all()
    page_data = Paginator(bugs, limit).page(page)

    count = len(bugs)
    data_list = []
    for bug in page_data:
        data_list.append({
            "id": bug.id,
            "name": bug.name,
            "os": bug.os,
            "found_by": bug.found_by,
            "found_time": get_datetime(bug.found_time),
            "bug_type": bug.bug_type,
            "bug_name": bug.bug_name,
            "bug_level": bug.bug_level,
            "bug_url": bug.bug_url,
            "bug_status": bug.bug_status,
            "notes": bug.notes,
        })
    return res_josn_data.table_api(count=count, data=data_list)


def stop(request: HttpRequest):
    print("请求参数", request.POST)
    return res_josn_data.success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    print("查询参数", request.POST)
    id = request.POST.get("id")
    BugLog.objects.filter(id=id).delete()
    return res_josn_data.success_api("删除成功")
