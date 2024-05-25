from django.db.models import Q
from django.shortcuts import redirect

from common.API import res_josn_data
from common.API.log import exec_log
from manage.models import RolePower, Power


def add_auth_session(request):
    """
    添加用户权限到session
    :request :请求对象
    :return:
    """
    role_id = request.session.get("role_id")
    # 通过用户ID查询用户操作权限
    auth_list = RolePower.objects.values_list("power_id").filter(
        Q(role_id=role_id) & ~Q(power_type=0)
    )
    auth_list = [i[0] for i in auth_list]

    power_obj = Power.objects.filter(id__in=auth_list)
    code_list = [i.code for i in power_obj]

    print("操作权限ID列表：", auth_list)
    print("操作权限code列表：", code_list)
    # 添加到session
    request.session["permissions"] = code_list
    return code_list


def login_required(info):
    def wrapper(request, *args, **kwargs):
        user_id = request.session.get("user_id")
        if not user_id:
            print("用户session过期, 需重新登陆")
            return redirect("/login")
        return info(request, *args, **kwargs)

    return wrapper


def authorize(power: str, log: bool = False):
    def decorator(func):
        @login_required
        def wrapper(request, *args, **kwargs):
            if not power in request.session.get("permissions"):
                if log:
                    exec_log(request=request, is_access=False, desc="没有权限")
                if request.method == "GET":
                    return res_josn_data.fail_api(msg="权限不足!")
            if log and request.method == "POST":
                exec_log(request=request, is_access=True, desc=str(dict(request.POST)))
            return func(request, *args, **kwargs)

        return wrapper

    return decorator
