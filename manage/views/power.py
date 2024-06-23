# encoding:utf-8
"""
@file = manage
@author = Administrator
@create_time = 2022/8/16- 15:21

"""
from django.shortcuts import render

from common.API import json_result
from common.API.auth import login_required, authorize
from manage.models import Power, RolePower
from scan.utils import get_filters, get_menu_tree, get_item_list, success_api, get_batch_delete_param, \
    get_form

result_fields = ["id", "name", "code", "type", "parent_id", "enable", "icon", "sort"]


@login_required
def power_manage(request):
    return render(request, "manage/power/index.html")


@login_required
def power_query(request):
    filters = get_filters(request.POST.get("Params"), ["name", "code", "type", "parent_id", "enable"])
    data = Power.objects.filter(**filters).order_by("id")
    data_list = get_item_list(data, result_fields)
    tree = get_menu_tree(data_list)
    count = len(tree)
    return json_result.table_api(count=count, data=tree)


@authorize(power="power:add", log=True)
def power_add(request):
    if request.method == "GET":
        return render(request, "manage/power/add.html")
    form = get_form(request.POST, ["name", "code", "type", "parent_id", "icon", "sort", "enable"])
    # type_dict = {"0": "目录", "1": "菜单", "2": "按钮", "3": "其他"}
    Power.objects.create(**form)
    max_id_obj = Power.objects.all().order_by("-id").first()
    RolePower.objects.create(role_id=2, power_id=max_id_obj.id, power_type=form["type"])
    return success_api()


@login_required
def power_sub_query(request):
    form = get_form(request.POST, ["type_value"])
    type_value = form["type_value"]
    if type_value not in ["0", "1", "2"]:
        type_value = "1"
    data = Power.objects.filter(type=type_value)
    data_list = get_item_list(data, ["id", "name"])
    return json_result.table_api(data=data_list, count=len(data_list))


@authorize(power="power:delete", log=True)
def power_delete(request):
    id = request.POST.get("id")
    Power.objects.filter(id=id).delete()
    return success_api()


@authorize(power="power:delete", log=True)
def power_multi_delete(request):
    ids_list = get_batch_delete_param(request.POST)
    objects_to_delete = Power.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    return success_api()


@login_required
def power_cell_edit(request):
    form = get_form(request.POST, ["id", "name", "code", "parent_id", "icon", "sort"])
    Power.objects.filter(id=form["id"]).update(**form)
    return success_api()


@authorize(power="power:enable", log=True)
def power_enable(request):
    form = get_form(request.POST, ["id", "enable"])
    item_obj = Power.objects.filter(id=form["id"])
    item_obj.update(enable=form["enable"])
    return success_api()
