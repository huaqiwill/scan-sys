from login.models import Log
from monitor.models import Monitor
from django.utils import timezone
from monitor.utils import notify


def check_sql(request):
    if request.method == "GET":
        request_data = request.GET
    elif request.method == "POST":
        request_data = request.POST
    else:
        request_data = ""

    print("添加notify==================================")
    request_data_str = str(request_data).replace("<QueryDict: {}", "").replace(">", "")
    notify.notify_add(
        notify_content=request_data_str,
        notify_type="可疑的SQL注入攻击",
        notify_subjet="可疑的SQL注入工具",
    )


def check_xss(request):
    if request.method == "GET":
        request_data = request.GET
    elif request.method == "POST":
        request_data = request.POST
    else:
        request_data = ""

    print("添加notify==================================")
    request_data_str = str(request_data).replace("<QueryDict: {}", "").replace(">", "")
    notify.notify_add(
        notify_content=request_data_str,
        notify_type="可疑的XSS脚本注入攻击",
        notify_subjet="可疑的XSS脚本注入工具",
    )


def check_crsf(request):
    if request.method == "GET":
        request_data = request.GET
    elif request.method == "POST":
        request_data = request.POST
    else:
        request_data = ""

    print("添加notify==================================")
    request_data_str = str(request_data).replace("<QueryDict: {}", "").replace(">", "")
    notify.notify_add(
        notify_content=request_data_str,
        notify_type="可疑的CRFS注入攻击",
        notify_subjet="可疑的CRFS注入工具",
    )


def xss_escape(s: str):
    if s is None:
        return None
    else:
        return (
            s.replace("&", "&amp;")
            .replace(">", "&gt;")
            .replace("<", "&lt;")
            .replace("'", "&#39;")
            .replace('"', "&#34;")
        )


def login_log(request, uid, is_access, desc):
    info = {
        "method": request.method,
        "url": request.path,
        "ip": request.META.get("REMOTE_ADDR"),
        "user_agent": xss_escape(request.headers.get("User-Agent")),
        "desc": desc,
        "uid": uid,
        "success": int(is_access),
    }

    if request.method == "GET":
        request_data = request.GET
    elif request.method == "POST":
        request_data = request.POST
    else:
        request_data = ""

    log = Log(
        url=info.get("url"),
        ip=info.get("ip"),
        user_agent=info.get("user_agent"),
        desc=info.get("desc"),
        uid=info.get("uid"),
        method=info.get("method"),
        success=info.get("success"),
    )
    monitor = Monitor(
        request_url=info.get("url"),
        request_method=info.get("method"),
        request_data=request_data,
        request_ip=info.get("ip"),
        attack_type="XSS",
        attack_time=timezone.now(),
        description=info.get("desc"),
    )
    monitor.save()
    log.save()

    check_sql(request)
    check_crsf(request)
    check_xss(request)

    return log


def exec_log(request, is_access, desc):
    user_id = request.session.get("user_id")
    if user_id in (None, ""):
        user_id = "admin"
        
    # desc = str(dict(request.values).get('Params'))
    print("desc:", desc)
    info = {
        "method": request.method,
        "url": request.path,
        "ip": request.META.get("REMOTE_ADDR"),
        "user_agent": xss_escape(request.headers.get("User-Agent")),
        "desc": desc,
        "uid": user_id,
        "success": int(is_access),
    }

    if request.method == "GET":
        request_data = request.GET
    elif request.method == "POST":
        request_data = request.POST
    else:
        request_data = ""

    log = Log(
        url=info.get("url"),
        ip=info.get("ip"),
        user_agent=info.get("user_agent"),
        desc=info.get("desc"),
        uid=info.get("uid"),
        method=info.get("method"),
        success=info.get("success"),
    )
    log.save()
    monitor = Monitor(
        user_id=info.get("uid"),
        request_url=info.get("url"),
        request_method=info.get("method"),
        request_data=request_data,
        request_ip=info.get("ip"),
        attack_type="XSS",
        attack_time=timezone.now(),
        description=info.get("desc"),
    )
    monitor.save()

    check_sql(request)
    check_crsf(request)
    check_xss(request)

    return log
