from django.http import HttpResponse


def json_response(data, status=200):
    json_data = {
        "code": "",
        "msg": "",
        data: data
    }
    return HttpResponse(json_data, content_type="application/json")
