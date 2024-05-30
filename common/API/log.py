from login.models import Log
from django.http import HttpRequest


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


def login_log(request: HttpRequest, uid, is_access, desc):
    info = gen_log(request, is_access, desc, uid)
    log = Log(**info)
    log.save()
    return log


def gen_log(request: HttpRequest, is_access, desc, user_id):
    return {
        "method": request.method,
        "url": request.path,
        "ip": request.META.get("REMOTE_ADDR"),
        "user_agent": xss_escape(request.headers.get("User-Agent")),
        "desc": desc,
        "uid": user_id,
        "success": int(is_access),
    }


def exec_log(request: HttpRequest, is_access, desc):
    user_id = request.session.get("user_id")
    log_data = gen_log(request, is_access, desc, user_id)
    log = Log(**log_data)
    log.save()
    return log
