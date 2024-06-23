import datetime
import json
from django.db import models
from django.http import HttpRequest, QueryDict
from django.core.paginator import Paginator
from common.API import json_result
from django.db.models.query import QuerySet
from django.http import JsonResponse


def get_delete_param(data: QueryDict):
    id = data.get("id")
    return id


def get_batch_delete_param(data: QueryDict):
    ids = data.get("ids")
    ids_list = ids.split(",")
    return ids_list


def get_form(data: QueryDict, fields: []):
    form = {}
    for field in fields:
        if data.get(field) is not None:
            form[field] = data.get(field)
        else:
            form[field] = ""
    return form


def get_item(data: QuerySet, fields: []):
    item = {}
    for field in fields:
        if hasattr(data, field):
            item[field] = getattr(data, field)
        else:
            print("不存在的属性：" + field)
    return item


def get_item_list(data: QuerySet, fields: []):
    data_list = []
    for item in data:
        data_list.append(get_item(item, fields))
    return data_list


def get_delete_param(request: HttpRequest):
    id = request.POST.get("id", "")
    if id == "":
        return json_result.fail_api("请求参数{id}不能为空")
    return id


def get_delete_batch_param(request: HttpRequest):
    ids = request.POST.get("ids", "")
    if ids == "":
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


def alias_filters(filters: dict, fields: list[str], alias: list[str]):
    """
    对来自前端的filters进行重命名操作
    """
    data = {}
    if len(fields) != len(alias):
        raise Exception("参数错误")
    for index, field in enumerate(fields):
        if filters.get(field) is not None:
            data[alias[index]] = filters[field]
    return data


def get_filters(params: str, fields: list[str]) -> dict:
    """
    参数，
    对应fields的为alias
    如果有别名
    """
    filters = {}
    if params not in [None, ""]:
        req = json.loads(params)
        for field in fields:
            if req.get(field) not in [None, ""]:
                filters[field] = req.get(field)
    return filters


def get_datetime(model: datetime.datetime):
    if model is None:
        return ""
    return model.strftime("%Y-%m-%d %H:%M:%S")


def get_menu_tree(data: list, parent_id=0):
    tree = []
    for item in data:
        if item["parent_id"] == parent_id:
            item["children"] = get_menu_tree(data, item["id"])
            tree.append(item)
    return tree
