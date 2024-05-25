# encoding:utf-8
"""
@file = urls
@author = zouju
@create_time = 2022-08-15- 10:47
"""
import json

from django.core.paginator import Paginator
from django.shortcuts import render

from common.API import res_josn_data
from common.API.auth import login_required, authorize
from manage.models import Role, User, RolePower, Power


@login_required
def role_manage(request):
    return render(request, "manage/role_manage/role_main.html")


@login_required
def role_query(request):
    data_list = []

    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    post_data_str = request.POST.get("Params", None)

    if post_data_str is None:
        user_obj = Role.objects.all().order_by("id")
        # return res_josn_data.table_api(data=data_list, count=0)
    else:
        post_data = json.loads(post_data_str)
        print(post_data)
        role_value = post_data["roleID"]
        code_name = post_data["codeName"]
        role_name = post_data["roleName"]
        role_enable = post_data["enable"]
        role_remark = post_data["remark"]

        filters = {}  # 查询参数构造
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
        filed_dict = {0: "role_value", 1: "name", 2: "code", 3: "enable", 4: "remark"}
        param_list = [role_value, role_name, code_name, role_enable, role_remark]

        for i in range(len(param_list)):
            if param_list[i] not in (None, ""):
                db_field = filed_dict[i] + orm_field[7]
                filters[db_field] = param_list[i]

        print("filters:", filters)

        user_obj = Role.objects.filter(**filters).order_by("id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    for item in page_data:
        count += 1
        item_data = {
            "id": count,
            "roleID": item.id,
            "roleValue": item.role_value,
            "roleCode": item.code,
            "roleName": item.name,
            "remark": item.remark,
            "enable": item.enable,
        }
        data_list.append(item_data)

    return res_josn_data.table_api(count=len(user_obj), data=data_list)


@authorize(power="role:add", log=True)
def role_add(request):
    if request.method == "GET":
        return render(request, "manage/role_manage/role_add.html")
    if request.method == "POST":
        post_data = request.POST
        print(request.POST)
        role_code = post_data["roleCode"]
        role_name = post_data["roleName"]
        role_remark = post_data["remark"]
        role_enable = post_data["enable"]
        role_obj = Role.objects.all().order_by("-role_value").first()

        if role_obj is None:
            role_id_value = 1
        else:
            role_id_value = role_obj.role_value + 1

        new_obj = Role(
            role_value=role_id_value,
            name=role_name,
            code=role_code,
            enable=role_enable,
            remark=role_remark,
        )
        new_obj.save()
        return res_josn_data.success_api(msg=f"角色:{role_code} 添加成功")


@authorize(power="role:delete", log=True)
def role_delete(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        db_id = post_data["roleID"]
        role_code = post_data["roleCode"]
        Role.objects.filter(id=db_id).delete()
        return res_josn_data.success_api(f"角色:{role_code} 删除成功")
    else:
        return res_josn_data.fail_api(msg="请求权限不够!")


@login_required
def role_cell_edit(request):
    # 前端字段和数据库字段对应dict
    filed_dict = {
        "roleValue": "role_value",
        "roleCode": "code",
        "roleName": "name",
        "remark": "remark",
    }
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_name = post_data["field"]
        field_value = post_data["value"]
        field_id = post_data["fieldID"]
        Role.objects.filter(id=field_id).update(**{filed_dict[field_name]: field_value})
        return res_josn_data.success_api(f"更新成功")


@authorize(power="role:enable", log=True)
def role_enable(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_id = post_data["roleID"]
        enable_value = post_data["enableValue"]  # 0禁用 1启用
        enable_dict = {"enable": 1, "disable": 0}
        enable_dict_cn = {"enable": "启用", "disable": "禁用"}
        role_obj = Role.objects.filter(id=field_id)
        role_obj.update(**{"enable": enable_dict[enable_value]})
        return res_josn_data.success_api(
            msg=f"{role_obj[0].code} {enable_dict_cn[enable_value]}成功"
        )


@login_required
def role_power(request):
    if request.method == "GET":
        return render(request, "manage/role_manage/role_power.html")
    if request.method == "POST":
        data_list = []
        post_data = request.POST
        print("table.render数据:", post_data)
        role_id = post_data.get("role_id", None)
        user_id = post_data.get("user_id", None)
        cur_user_role = User.objects.filter(id_number=user_id).first()

        # 获取当前用户的所有权限
        cur_user_obj = RolePower.objects.values_list("power_id").filter(
            role_id=cur_user_role.role_id
        )
        cur_usr_id_list = [i[0] for i in cur_user_obj]
        # 获取当前选择角色的所有权限
        power_id_obj = RolePower.objects.values_list("power_id").filter(role_id=role_id)
        power_id_list = [item[0] for item in power_id_obj]
        # print(cur_user_obj, power_id_list)
        # 目录对象
        power_dir_obj = Power.objects.filter(type=0).order_by("sort")

        for item_dir in power_dir_obj:
            if item_dir.id in cur_usr_id_list:
                dir_id = item_dir.id
                power_menu_obj = Power.objects.filter(parent_id=dir_id).order_by(
                    "sort"
                )  # 通过目录id获取菜单对象
                data_list1 = []
                for item in power_menu_obj:
                    if item.id in cur_usr_id_list:
                        button_checkbox_list = []
                        if item.id in power_id_list:
                            power_check = "checked"
                        else:
                            power_check = ""
                        button_obj = Power.objects.filter(parent_id=item.id).order_by(
                            "sort"
                        )  # 通过菜单id获取按钮对象
                        power_name_list = [i.name for i in button_obj]
                        button_id_list = [i.id for i in button_obj]
                        # 判断按钮是否被选中
                        for button_id in button_id_list:
                            if button_id in power_id_list:
                                button_check = "checked"
                            else:
                                button_check = ""
                            button_checkbox_list.append(button_check)

                        item_data1 = {
                            "menuId": item.id,
                            "menuName": item.name,
                            "menuCheckbox": power_check,
                            "buttonName": power_name_list,
                            "buttonId": button_id_list,
                            "buttonCheckbox": button_checkbox_list,
                        }
                        data_list1.append(item_data1)

                item_data = {
                    "dirId": item_dir.id,
                    "dirName": item_dir.name,
                    "menuInfo": data_list1,
                }
                data_list.append(item_data)
        return res_josn_data.table_api(data=data_list, count=len(data_list))


@authorize(power="role:power", log=True)
def role_power_save(request):
    if request.method == "POST":
        menu_power_list = []
        button_power_list = []
        post_data = request.POST
        print("role-power-save:", post_data)
        role_id = post_data.get("roleId", "")
        for item in post_data:
            if item[:4] == "page":
                page_value = post_data.get(item, "")
                menu_power_list.append(page_value)
            elif item[:6] == "button":
                button_value = post_data.get(item, "")
                button_power_list.append(button_value)
            else:
                pass
        dir_power = Power.objects.filter(id__in=menu_power_list)
        dir_power_list = [item.parent_id for item in dir_power]
        dir_power_list = list(set(dir_power_list))

        print("目录权限ID:", dir_power_list)
        print("菜单权限ID:", menu_power_list)
        print("按钮权限ID:", button_power_list)

        if role_id is None:
            return res_josn_data.fail_api(msg="role_id为空")

        # 删除原有权限
        RolePower.objects.filter(role_id=role_id).delete()

        # 添加新权限,power_type 0目录 1菜单 2按钮
        for item_id in dir_power_list:
            role_obj = RolePower(role_id=role_id, power_id=item_id, power_type="0")
            role_obj.save()
        for item_id in menu_power_list:
            role_obj = RolePower(role_id=role_id, power_id=item_id, power_type="1")
            role_obj.save()
        for item_id in button_power_list:
            role_obj = RolePower(role_id=role_id, power_id=item_id, power_type="2")
            role_obj.save()

        return res_josn_data.success_api("保存成功")
