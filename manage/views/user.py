# encoding:utf-8
import json

from django.contrib.auth.hashers import make_password
from django.core.paginator import Paginator
from django.shortcuts import render

# Create your views here.

from common.API import res_josn_data
from common.API.auth import login_required, authorize
from manage.models import User, Role


@login_required
def user_manage(request):
    return render(request, "manage/user_manage/user_main.html")


@login_required
def user_query(request):
    data_list = []
    page = request.POST.get("page", 1)
    limit = request.POST.get("limit", 10)
    post_data_str = request.POST.get("Params", None)

    if post_data_str is None:
        user_obj = User.objects.all().order_by("id")
        # return res_josn_data.table_api(data=data_list, count=0)
    else:
        post_data = json.loads(post_data_str)
        id_number = post_data["idNumber"]
        user_name = post_data["userName"]
        user_dep = post_data["dep"]
        user_pos = post_data["position"]
        user_status = post_data["status"]
        user_role = post_data["role"]

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
        filed_dict = {
            0: "id_number",
            1: "user_name",
            2: "department",
            3: "position",
            4: "user_status",
            5: "role_id",
        }
        param_list = [id_number, user_name, user_dep, user_pos, user_status, user_role]

        for i in range(len(param_list)):
            if param_list[i] not in (None, ""):
                db_field = filed_dict[i] + orm_field[7]
                filters[db_field] = param_list[i]

        print("filters:", filters)

        user_obj = User.objects.filter(**filters).order_by("id")
    page_data = Paginator(user_obj, limit).page(page)

    # 序号
    count = (int(page) - 1) * int(limit)

    for item in page_data:
        count += 1
        item_data = {
            "id": count,
            "fieldID": item.id,
            "userID": item.id_number,
            "name": item.user_name,
            "department": item.department,
            "position": item.position,
            "email": item.email,
            "status": item.user_status,
            "role": item.role_des,
        }
        data_list.append(item_data)

    return res_josn_data.table_api(count=len(user_obj), data=data_list)


@authorize(power="user:add", log=True)
def user_add(request):
    if request.method == "GET":
        return render(request, "manage/user_manage/user_add.html")
    if request.method == "POST":
        post_data = request.POST
        print(request.POST)
        user_id = post_data["userID"]
        user_password = post_data["password"]
        user_name = post_data["userName"]
        user_dep = post_data["department"]
        user_position = post_data["position"]
        user_email = post_data["email"]
        user_enable = post_data["enable"]
        role_value = post_data["role"]

        user_password_sha256 = make_password(user_password, salt=None, hasher="default")
        role_obj = Role.objects.filter(role_value=role_value).first()

        new_obj = User(
            id_number=user_id,
            id_password=user_password_sha256,
            user_name=user_name,
            department=user_dep,
            position=user_position,
            role_id=role_value,
            role_des=role_obj.name,
            user_status=user_enable,
            email=user_email,
        )
        new_obj.save()
        return res_josn_data.success_api(msg=f"用户:{user_name} 添加成功")


@login_required
def user_role_query(request):
    if request.method == "POST":
        data_list = []
        role_data = Role.objects.all()
        for item in role_data:
            item_data = {"roleID": item.role_value, "roleName": item.name}
            data_list.append(item_data)
        print(data_list)
        return res_josn_data.table_api(data=data_list, count=len(role_data))


@authorize(power="user:delete", log=True)
def user_delete(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        db_id = post_data["fieldID"]
        user_name = post_data["name"]
        User.objects.filter(id=db_id).delete()
        return res_josn_data.success_api(f"用户:{user_name} 删除成功")
    else:
        return res_josn_data.fail_api(msg="请求权限不够!")


@authorize(power="user:delete", log=True)
def user_multi_delete(request):
    if request.method == "POST":
        user_list = []
        post_data_str = request.POST.get("Params", None)
        post_data = json.loads(post_data_str)
        for item in post_data:
            db_id = item["fieldID"]
            user_name = item["name"]
            User.objects.filter(id=db_id).delete()
            user_list.append(user_name)
        return res_josn_data.success_api(f"用户:{user_list} 删除成功")


@login_required
def user_cell_edit(request):
    # 前端字段和数据库字段对应dict
    filed_dict = {
        "userID": "id_number",
        "name": "user_name",
        "department": "department",
        "position": "position",
        "email": "email",
    }
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_name = post_data["field"]
        field_value = post_data["value"]
        field_id = post_data["dbID"]
        User.objects.filter(id=field_id).update(**{filed_dict[field_name]: field_value})
        return res_josn_data.success_api(f"更新成功")


@login_required
def user_role_edit(request):
    if request.method == "GET":
        return render(request, "manage/user_manage/user_role_edit.html")
    if request.method == "POST":
        post_data = request.POST
        print(post_data)
        user_id = post_data["userID"]
        role_id = post_data["role"]
        role_obj = Role.objects.filter(role_value=role_id).first()
        update_dict = {"role_id": role_id, "role_des": role_obj.name}
        User.objects.filter(id_number=user_id).update(**update_dict)
        return res_josn_data.success_api(msg=f"{user_id} 角色更新成功")


@authorize(power="user:enable", log=True)
def user_enable(request):
    if request.method == "POST":
        post_data = request.POST
        print("AJAX数据:", post_data)
        field_id = post_data["userID"]
        enable_value = post_data["enableValue"]  # 0禁用 1启用
        enable_dict = {"enable": 1, "disable": 0}
        enable_dict_cn = {"enable": "启用", "disable": "禁用"}
        role_obj = User.objects.filter(id=field_id)
        role_obj.update(**{"user_status": enable_dict[enable_value]})
        return res_josn_data.success_api(
            msg=f"{role_obj[0].user_name} {enable_dict_cn[enable_value]}成功"
        )
