from django.http import JsonResponse


def success_api(data=None, msg: str = "success"):
    """成功响应"""
    res = {"msg": msg, "success": True, "data": data}
    return JsonResponse(res, safe=False)


def fail_api(msg: str = "fail"):
    """失败响应"""
    res = {"msg": msg, "success": False}
    return JsonResponse(res, safe=False)


def table_api(msg: str = "success", count=0, data=None, limit=10):
    """动态表格渲染响应"""
    res = {"msg": msg, "code": 0, "data": data, "count": count, "limit": limit}
    return JsonResponse(res, safe=False)


def user_setting_api(user_id, username, department, position, role, email, data):
    """用户信息响应"""
    res = {
        "id": user_id,
        "code": 0,
        "username": username,
        "dep": department,
        "position": position,
        "role": role,
        "email": email,
        "data": data,
    }
    return JsonResponse(res, safe=False)
