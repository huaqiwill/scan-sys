# encoding:utf-8
"""
@file = log_manage
@author = zouju
@create_time = 2022-08-24- 9:54
"""
import json

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render

from common.API import json_result
from common.API.auth import authorize, login_required
from login.models import Log
from django.views.decorators.http import require_http_methods

from scan.utils import get_form, success_api


@login_required
def log_manage(request):
    return render(request, "manage/log_manage/log_main.html")


@login_required
@require_http_methods(["POST"])
def log_query(request):
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    post_data_str = request.POST.get("Params", None)

    filters = {}  # 查询参数构造
    data_list = []
    if post_data_str is not None:
        post_data = json.loads(post_data_str)
        user_id = post_data["UID"]
        method = post_data["method"]
        url = post_data["URL"]
        desc = post_data["desc"]
        log_status = post_data["status"]
        log_time = post_data["time"]

        # model或数据库对应字段
        orm_field = [
            "__gt",
            "__gte",
            "__lt",
            "__lte",
            "__exact",
            "__iexact",
            "__contains",
            "__icontains",
            "__startswith",
            "__istartswith",
            "__endswith",
            "__iendswith",
            "__range",
            "__isnull",
            "__in",
        ]

        filed_dict = {0: "uid", 1: "method", 2: "url", 3: "desc", 4: "success"}
        param_list = [user_id, method, url, desc, log_status]

        for i in range(len(param_list)):
            if param_list[i] not in (None, ""):
                db_field = filed_dict[i] + orm_field[7]
                filters[db_field] = param_list[i]

        if log_time not in (None, ""):
            filters["create_time__gte"] = log_time

        print("filters:", filters)

    user_obj = Log.objects.filter(**filters).order_by("-id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    for item in page_data:
        count += 1
        dis_time = str(item.create_time)[:19]
        print(item.id)
        item_data = {
            "id": count,
            "fieldID": item.id,
            "userId": item.uid,
            "method": item.method,
            "url": item.url,
            "ip": item.ip,
            "time": dis_time,
            "userAgent": item.user_agent,
            "success": item.success,
            "desc": item.desc,
        }
        data_list.append(item_data)

    return json_result.table_api(count=len(user_obj), data=data_list)


@authorize(power="log:delete", log=True)
def log_delete(request):
    id = request.POST.get("id")
    Log.objects.filter(id=id).delete()
    return success_api()


def edit(request: HttpRequest):
    if request.method == "GET":
        return render(request, "manage/log_manage/add.html")

    form = get_form(request, ["id", ""])
    Log.objects.filter(id=form["id"]).update(**form)
    return success_api()
