import os
from datetime import datetime

from aiohttp.web_fileresponse import FileResponse
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import ReportLog
from scan.utils import get_filters, get_datetime, table_data, print_params, get_item, get_form, get_batch_delete_param

result_fields = ["id", "name", "url", "create_time", "format"]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/report/index.html")


@require_http_methods(["GET", "POST"])
def add(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/report/add.html")

    form = get_form(request.POST, ["name", "format"])
    form["url"] = "/scan/report/download/test.pdf"
    form["create_time"] = datetime.now()
    ReportLog.objects.create(**form)
    return success_api()


@require_http_methods(["POST"])
def query(request: HttpRequest):
    filters = get_filters(request.POST.get("Params"), ["name"])
    result = ReportLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    ReportLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def delete_batch(request: HttpRequest):
    ids_list = get_batch_delete_param(request.POST)
    objects_to_delete = ReportLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    try:
        data = ReportLog.objects.get(id=id)
        return success_api(get_item(data, result_fields))
    except ReportLog.DoesNotExist:
        return fail_api("未找到该记录")


@require_http_methods(["GET"])
def download(request: HttpRequest, file_name):
    # 确定文件的路径
    file_path = os.path.join("static/uploads/", file_name)

    print(file_name)

    # 检查文件是否存在
    if not os.path.exists(file_path):
        raise Http404("File does not exist")

    # 打开文件并创建 HttpResponse 对象
    try:
        with open(file_path, 'rb') as f:
            file_data = f.read()

        response = HttpResponse(file_data, content_type='application/octet-stream')
        response['Content-Disposition'] = f'attachment; filename="{file_name}"'
        return response
    except Exception as e:
        raise Http404(f"Error occurred while reading the file: {str(e)}")


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = ReportLog.objects.get(id=id)
        context = {
            "id": id,
            "name": obj.name
        }
        return render(request, "scan/report/edit.html", context)

    id = request.POST.get("id", "")
    name = request.POST.get("name", "")
    if id == "":
        return fail_api("错误的请求地址")

    try:
        item = ReportLog.objects.get(id=id)
        item.name = name
        item.save()
        return success_api()
    except:
        return fail_api("未找到相关资源")
