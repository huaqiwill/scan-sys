# encoding:utf-8
"""
@file = manage
@author = Administrator
@create_time = 2022/8/16- 15:21

"""
import json

from django.core.paginator import Paginator
from django.shortcuts import render

from common.API import res_josn_data
from common.API.auth import login_required, authorize
from manage.models import Power, RolePower


@login_required
def power_manage(request):
    return render(request, "manage/power_manage/power_main.html")


@login_required
def power_query(request):
    data_list = []
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    post_data_str = request.POST.get("Params", None)
    if post_data_str is None:
        power_obj = Power.objects.all().order_by("id")
        # return res_josn_data.table_api(data=data_list, count=0)
    else:
        post_data = json.loads(post_data_str)
        power_name = post_data["powerName"]
        power_code = post_data["powerCode"]
        power_type = post_data["powerType"]
        parent_id = post_data["parentId"]
        power_enable = post_data["powerEnable"]
        icon = post_data["icon"]

        # 查询参数构造
        filters = {}  # 查询参数构造

        # model或数据库对应字段, 对应查询条件字段
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
        filed_dict = {
            0: "name",
            1: "code",
            2: "type",
            3: "enable",
            4: "icon",
            5: "parent_id",
        }
        param_list = [power_name, power_code, power_type, power_enable, icon, parent_id]

        for i in range(len(param_list)):
            if param_list[i] not in (None, ""):
                db_field = filed_dict[i] + orm_field[7]
                filters[db_field] = param_list[i]

        print("filters:", filters)

        power_obj = Power.objects.filter(**filters).order_by("id")
    page_data = Paginator(power_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    # 对应到前端html的data, key对应前端field, value对应数据库字段
    for item in page_data:
        count += 1
        item_data = {
            "id": count,
            "powerId": item.id,
            "powerName": item.name,
            "powerCode": item.code,
            "powerType": item.open_type,
            "parentId": item.parent_id,
            "icon": item.icon,
            "sort": item.sort,
            "enable": item.enable,
        }
        data_list.append(item_data)

    return res_josn_data.table_api(count=len(power_obj), data=data_list)


@authorize(power="power:add", log=True)
def power_add(request):
    if request.method == "GET":
        return render(request, "manage/power_manage/power_add.html")
    if request.method == "POST":
        type_dict = {"0": "目录", "1": "菜单", "2": "按钮", "3": "其他"}
        # 解析post数据
        post_data = request.POST
        power_name = post_data["powerName"]
        power_code = post_data["powerCode"]
        power_type = post_data["type"]
        parent_name = post_data["parentName"]
        icon = post_data["icon"]
        sort = post_data["sort"]
        power_enable = post_data["enable"]

        # 查询父级id
        power_obj = Power.objects.filter(name=parent_name).first()
        if power_obj is None:
            parent_id = 0
        else:
            parent_id = power_obj.id
        # 写入数据库
        new_obj = Power(
            name=power_name,
            code=power_code,
            type=power_type,
            parent_id=parent_id,
            open_type=type_dict[power_type],
            icon=icon,
            sort=sort,
            enable=power_enable,
        )
        new_obj.save()
        # 写入权限表role_power  role_id=2对应管理员的role_value
        max_id_obj = Power.objects.all().order_by("-id").first()
        role_power_obj = RolePower(
            role_id=2, power_id=max_id_obj.id, power_type=power_type
        )
        role_power_obj.save()
        return res_josn_data.success_api(f"{power_name} 添加成功")


@login_required
def power_sub_query(request):
    if request.method == "POST":
        data_list = []
        p_name = ""
        post_data = request.POST
        print("power-name请求数据:", post_data)
        type_value = post_data["type_value"]
        if type_value == "0":
            return res_josn_data.table_api(data=data_list, count=0)
        elif type_value == "1":
            p_name = Power.objects.filter(type=0).values("name")
        elif type_value == "2":
            p_name = Power.objects.filter(type=1).values("name")
        else:
            p_name = Power.objects.filter(type=1).values("name")

        for item in p_name:
            item_data = {"power_name": item["name"]}
            data_list.append(item_data)
        return res_josn_data.table_api(data=data_list, count=len(p_name))


@authorize(power="power:delete", log=True)
def power_delete(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        db_id = post_data["powerId"]
        user_name = post_data["powerName"]
        Power.objects.filter(id=db_id).delete()
        RolePower.objects.filter(power_id=db_id).delete()  # 对应role_power中的权限删除
        return res_josn_data.success_api(f"{user_name} 删除成功")
    else:
        return res_josn_data.fail_api(msg="请求权限不够!")


@authorize(power="power:delete", log=True)
def power_multi_delete(request):
    if request.method == "POST":
        user_list = []
        post_data_str = request.POST.get("Params", None)
        post_data = json.loads(post_data_str)
        for item in post_data:
            db_id = item["powerId"]
            user_name = item["powerName"]
            Power.objects.filter(id=db_id).delete()
            RolePower.objects.filter(
                power_id=db_id
            ).delete()  # 对应role_power中的权限删除
            user_list.append(user_name)
        return res_josn_data.success_api(f"{user_list} 删除成功")


@login_required
def power_cell_edit(request):
    # 前端字段和数据库字段对应dict
    filed_dict = {
        "powerName": "name",
        "powerCode": "code",
        "parentId": "parent_id",
        "icon": "icon",
        "sort": "sort",
    }
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_name = post_data["field"]
        field_value = post_data["value"]
        field_id = post_data["powerId"]
        Power.objects.filter(id=field_id).update(
            **{filed_dict[field_name]: field_value}
        )
        return res_josn_data.success_api(f"更新成功")


@authorize(power="power:enable", log=True)
def power_enable(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_id = post_data["powerID"]
        enable_value = post_data["enableValue"]  # 0禁用 1启用
        enable_dict = {"enable": 1, "disable": 0}
        enable_dict_cn = {"enable": "启用", "disable": "禁用"}
        item_obj = Power.objects.filter(id=field_id)
        item_obj.update(**{"enable": enable_dict[enable_value]})
        return res_josn_data.success_api(
            msg=f"{item_obj[0].name} {enable_dict_cn[enable_value]}成功"
        )
