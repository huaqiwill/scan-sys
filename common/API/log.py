from login.models import Log


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

    return log
