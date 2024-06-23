import datetime
import json
from django.db import models
from django.http import HttpRequest
from django.core.paginator import Paginator
from common.API import json_result
from django.db.models.query import QuerySet
from django.http import JsonResponse


def get_delete_param(request: HttpRequest):
    ids = request.POST.get("ids", "")
    if ids is "":
        id_list = []
    else:
        id_list = ids.split(",")
    return id_list


def get_page(request: HttpRequest, data: QuerySet):
    """获取分页数据

    Args:
        request (HttpRequest): _description_
        host_log_list (_type_): _description_

    Returns:
        _type_: _description_
    """
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    page_data = Paginator(data, limit).page(page)
    return page_data


def table_data(request: HttpRequest, data: QuerySet, args: list[str]):
    # 分页
    page_data = get_page(request, data)
    # 长度
    count = len(data)
    # 数据集
    data_list = []
    for item in page_data:
        one = {}
        for arg in args:
            one[arg] = getattr(item, arg)
        data_list.append(one)
    # 以json格式返回
    return json_result.table_api(count=count, data=data_list)


def success_api():
    return json_result.success_api()


def fail_api():
    return json_result.fail_api()


def print_params(request: HttpRequest):
    if request.method == "GET":
        print("请求参数", request.GET)
    if request.method == "POST":
        print("请求参数", request.POST)


def get_filters(params: str, fields: list[str]):
    filters = {}
    if params not in [None, ""]:
        req = json.loads(params)
        for field in fields:
            if req.get(field) not in [None, ""]:
                filters[field] = req[field]
    return filters


def get_datetime(model: datetime.datetime):
    if model is None:
        return ""
    return model.strftime("%Y-%m-%d %H:%M:%S")
