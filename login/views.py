import json
from io import BytesIO
from django.contrib.auth import logout
from django.contrib.auth.hashers import check_password, make_password
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from common.API import res_josn_data
from common.API.auth import add_auth_session
from common.API.captcha import make_captcha
from common.API.code import check_code
from common.API.echarts import echarts_pie, json_response
from common.API.log import login_log
from login.models import Logo, Log
from manage.models import User, Role, Power, RolePower
from common.API.auth import login_required
from django.views.decorators.http import require_http_methods


@login_required
@require_http_methods(["GET"])
def index(request):
    data = {"title": "登录 - 漏洞扫描系统"}
    return render(request, "login/index.html", data)


def home(request):
    if request.method == "GET":
        return render(request, "login/home.html")


def page_not_found(request, exception):
    if request.method == "GET":
        return render(request, "errors/404.html")


def page_error(request):
    if request.method == "GET":
        return render(request, "errors/500.html")


@require_http_methods(["GET", "POST"])
def login(request):
    if request.method == "GET":
        data = {"title": "漏洞扫描系统"}
        return render(request, "login/login.html", data)
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        code = request.POST.get("captcha")

        if not username or not password or not code:
            return res_josn_data.fail_api(msg="用户名或密码没有输入")

        s_code = request.session.get("code", None)
        print("验证码:", code, s_code)
        user_ip = request.META.get("REMOTE_ADDR")
        print(user_ip)

        request.session["code"] = None

        if not all([code, s_code]):
            login_log(
                request, uid=username, is_access=False, desc="验证码错误,请刷新验证码"
            )
            return res_josn_data.fail_api(msg="验证码错误,请刷新验证码!")

        if code != s_code:
            login_log(request, uid=username, is_access=False, desc="验证码错误")
            return res_josn_data.fail_api(msg="验证码错误")

        user = User.objects.filter(id_number=username).first()

        if user is None:
            login_log(request, uid=username, is_access=False, desc="用户不存在")
            return res_josn_data.fail_api(msg="用户不存在!")

        if user.user_status == 0:
            login_log(request, uid=user.id_number, is_access=False, desc="用户被禁用")
            return res_josn_data.fail_api(msg="用户被禁用!")

        if username == user.id_number and check_password(password, user.id_password):
            # 设置session过期时间
            request.session.set_expiry(60 * 60 * 2)
            # 登录
            request.session["user_id"] = user.id_number
            request.session["user_name"] = user.user_name
            request.session["role_id"] = user.role_id
            request.session["role_des"] = user.role_des
            request.session["id"] = user.id
            # 学校名称
            request.session["department"] = user.department
            # 年级
            request.session["position"] = user.position
            # 科目
            request.session["email"] = user.email
            # 记录登录日志
            login_log(request, uid=user.id_number, is_access=True, desc="登录成功")
            # 存入权限
            add_auth_session(request)
            return res_josn_data.success_api(msg="登录成功")
        else:
            login_log(request, uid=user.id_number, is_access=False, desc="密码错误")
            return res_josn_data.fail_api(msg="密码错误")


def image_code(request):
    """生成图片验证码"""

    # 调用pillow函数，生成图片
    img, code_string = check_code()

    # 写入到自己的session中（以便于后续获取验证码再进行校验）
    request.session["image_code"] = code_string
    # 给Session设置60s超时
    request.session.set_expiry(60)

    stream = BytesIO()
    img.save(stream, "png")
    return HttpResponse(stream.getvalue())


def get_captcha(request):
    return make_captcha(request)


@login_required
def login_in(request):
    user_id = request.session.get("user_id")
    if user_id:
        data = {"title": "漏洞扫描系统", "user_id": user_id}
        return render(request, "login/index.html", data)


@login_required
def login_out(request):
    user_id = request.session.get("user_id")
    login_log(request, uid=user_id, is_access=True, desc="退出登录")
    logout(request)
    return redirect("/login")


@login_required
def web_menu(request):
    home_info = Logo.objects.filter(type="0").first()
    logo_info = Logo.objects.filter(type="1").first()
    title_info = Logo.objects.filter(type="2").first()
    menu_info = Power.objects.filter(type=0, enable=1).order_by("sort")  # 目录
    # 查询权限ID
    menu_id = RolePower.objects.values_list("power_id").filter(
        role_id=request.session.get("role_id")
    )
    permission_id = [i[0] for i in menu_id]
    print(f"当前用户权限ID:{permission_id}")

    menu_data = {
        "homeInfo": {"title": f"{home_info.name}", "href": f"{home_info.url}"},
        "logoInfo": {
            "title": f"{logo_info.name}",
            "image": f"{logo_info.icon}",
            "href": f"{logo_info.url}",
        },
        "menuInfo": [
            {
                "title": f"{title_info.name}",
                "icon": f"{title_info.icon}",
                "href": f"{title_info.url}",
                "target": "_self",
                "child": [],
            }
        ],
    }
    for item in menu_info:
        if item.id in permission_id:
            menu_data["menuInfo"][0]["child"].append(
                {
                    "title": f"{item.name}",
                    "icon": f"{item.icon}",
                    "href": f"{item.code}",
                    "target": "_self",
                    "child": [],
                }
            )
            # 查询子菜单
            sub_menu_info = Power.objects.filter(parent_id=item.id, enable=1).order_by(
                "sort"
            )
            for sub_item in sub_menu_info:
                if sub_item.id in permission_id:
                    menu_data["menuInfo"][0]["child"][-1]["child"].append(
                        {
                            "title": f"{sub_item.name}",
                            "icon": f"{sub_item.icon}",
                            "href": f"{sub_item.code}",
                            "target": "_self",
                        }
                    )

    return JsonResponse(menu_data, safe=False)


@login_required
def echarts(request):
    if request.method == "POST":
        n_type = ["用户", "角色", "权限", "日志"]
        user_count = User.objects.count()
        role_count = Role.objects.count()
        role_power_count = RolePower.objects.count()
        log_count = Log.objects.count()
        data_list = [user_count, role_count, role_power_count, log_count]
        title = "1.数量统计"
        c = echarts_pie(n_type, data_list, title)
        return json_response(json.loads(c))


@login_required
def user_setting(request):
    if request.method == "GET":
        return render(request, "login/user_setting.html")
    if request.method == "POST":
        post_data = request.POST
        print(post_data)
        field_user_id = post_data["userID"]
        field_name = post_data["userName"]
        field_dep = post_data["department"]
        field_pos = post_data["position"]
        field_email = post_data["email"]
        update_dict = {
            "user_name": field_name,
            "department": field_dep,
            "position": field_pos,
            "email": field_email,
        }
        User.objects.filter(id_number=field_user_id).update(**update_dict)
        return res_josn_data.success_api(msg=f"用户:{field_user_id} 更新成功")


@login_required
def user_info_query(request):
    data_list = []
    post_data = request.POST
    print("AJAX数据:", post_data)
    login_id = post_data["login_id"].strip()
    user_info = User.objects.filter(id_number=login_id).first()
    role_info = Role.objects.filter(role_value=user_info.role_id).first()

    return res_josn_data.user_setting_api(
        login_id,
        user_info.user_name,
        user_info.department,
        user_info.position,
        role_info.name,
        user_info.email,
        data_list,
    )


@login_required
def user_password(request):
    if request.method == "GET":
        return render(request, "login/user_password.html")
    if request.method == "POST":
        post_data = request.POST
        print(post_data)
        login_id = post_data["login_id"].strip()
        old_password = post_data["Param[old_password]"]
        new_password = post_data["Param[new_password]"]
        again_password = post_data["Param[again_password]"]
        user_obj = User.objects.filter(id_number=login_id).first()
        if not user_obj:
            return res_josn_data.fail_api(msg="用户不存在!")
        if not check_password(old_password, user_obj.id_password):
            return res_josn_data.fail_api(msg="旧密码错误!")
        if new_password != again_password:
            return res_josn_data.fail_api(msg="两次密码不一致!")
        User.objects.filter(id_number=login_id).update(
            **{"id_password": make_password(new_password)}
        )
        return res_josn_data.success_api(msg="修改成功!")


# def page_not_found(request, exception):
#     return render(request, "errors/404.html", exception)
#
#
# def page_error(request):
#     return render(request, "errors/500.html")
