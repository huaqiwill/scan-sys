from login.models import Log
from monitor.models import Monitor
from django.utils import timezone


def xss_escape(s: str):
    if s is None:
        return None
    else:
        print("可疑的XSS攻击")
        # Monitor.objects.create(request_url="")

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
        request_data=info.get("desc"),
        request_ip=info.get("ip"),
        attack_type="XSS",
        attack_time=timezone.now(),
        description=info.get("desc"),
    )
    monitor.save()
    log.save()
    return log


def exec_log(request, is_access, desc):
    user_id = request.session.get("user_id")
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
        request_data=info.get("desc"),
        request_ip=info.get("ip"),
        attack_type="XSS",
        attack_time=timezone.now(),
        description=info.get("desc"),
    )
    monitor.save()

    return log
