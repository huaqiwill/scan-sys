import datetime
import json
import random

from django.core.paginator import Paginator
from django.http import HttpRequest
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from common.API.json_result import success_api, fail_api
from scan.models import BugLog
from scan.utils import get_filters, get_datetime, print_params, table_data, get_form, get_item, get_delete_param, \
    get_batch_delete_param
from scan.utils.scanning import get_local_ip, get_os_name_and_version, generate_random_url

result_fields = [
    "id",
    "name",
    "os",
    "found_by",
    "found_time",
    "bug_type",
    "bug_name",
    "bug_level",
    "bug_url",
    "bug_status",
    "notes",
]


@require_http_methods(["GET"])
def index(request: HttpRequest):
    return render(request, "scan/bug/index.html")


def start_sql(form: dict, host, port, username, password, database):
    size = random.randint(1, 10)
    name_list = ["MySQL", "Redis", "ElasticSearch", "Oracle", "PostgreSQL"]
    bug_type_list = ["轻微", "严重", "中等", "高等", "建议"]
    for i in range(0, size):
        save_form = json.dumps(form)
        load_form = json.loads(save_form)
        load_form["name"] = random.choice(name_list)
        load_form["os"] = get_os_name_and_version()
        load_form["found_by"] = get_local_ip()
        load_form["found_time"] = datetime.datetime.now()
        load_form["bug_type"] = random.choice(bug_type_list)
        load_form["bug_name"] = load_form["type"]
        load_form["bug_level"] = "低级"
        load_form["bug_url"] = generate_random_url()
        load_form["bug_status"] = "unknown"
        load_form[
            "notes"] = "主机名称：" + host + "\n端口号：" + port + "\n用户名：" + username + "\n密码：" + password + "\n数据库：" + database
        remove_others(load_form)
        BugLog.objects.create(**load_form)


def start_stmp(form: dict, server, username, password):
    size = random.randint(1, 10)
    name_list = ["STMP", "QQ邮箱", "网易邮箱"]
    bug_type_list = ["轻微", "严重", "中等", "高等", "建议"]
    bug_type = ["端口暴露", "弱口令", "命令击中"]
    for i in range(0, size):
        save_form = json.dumps(form)
        load_form = json.loads(save_form)
        load_form["name"] = random.choice(name_list)
        load_form["os"] = get_os_name_and_version()
        load_form["found_by"] = get_local_ip()
        load_form["found_time"] = datetime.datetime.now()
        load_form["bug_type"] = random.choice(bug_type)
        load_form["bug_name"] = load_form["type"]
        load_form["bug_level"] = random.choice(bug_type_list)
        load_form["bug_url"] = generate_random_url()
        load_form["bug_status"] = "unknown"
        load_form["notes"] = "服务器：" + server + "\n用户名：" + username + "\n密码：" + password
        remove_others(load_form)
        BugLog.objects.create(**load_form)


def start_web(form: dict, url):
    size = random.randint(1, 10)
    name_list = ["HTTP", "HTTPS", "WebSocket", "AGH", "NACO"]
    bug_type_list = ["轻微", "严重", "中等", "高等", "建议"]
    for i in range(0, size):
        save_form = json.dumps(form)
        load_form = json.loads(save_form)
        load_form["name"] = random.choice(name_list)
        load_form["os"] = get_os_name_and_version()
        load_form["found_by"] = get_local_ip()
        load_form["found_time"] = datetime.datetime.now()
        load_form["bug_type"] = random.choice(bug_type_list)
        load_form["bug_name"] = load_form["type"]
        load_form["bug_level"] = "低级"
        load_form["bug_url"] = generate_random_url()
        load_form["bug_status"] = "unknown"
        load_form["notes"] = load_form["token"]
        remove_others(load_form)
        BugLog.objects.create(**load_form)


def start_file(form: dict):
    size = random.randint(1, 10)
    name_list = ["FTP", "SFTP", "FileSystem"]
    bug_type_list = ["轻微", "严重", "中等", "高等", "建议"]
    bug_type = ["关闭匿名用户的上传数据权利，并提供下载数据文件的校验文件", "使用无特权账号和组 (比如 nobody)来启动 FTP daemon",
                "给匿名 FTP 账号使用假的 shell (/bin/false or /bin/true)", "限制 FTP 账号在一定时间段内的登录次数", "FTP弱口令", "FTP命令注入",
                "FTP服务端扫描"]
    for i in range(0, size):
        save_form = json.dumps(form)
        load_form = json.loads(save_form)
        load_form["name"] = random.choice(name_list)
        load_form["os"] = get_os_name_and_version()
        load_form["found_by"] = get_local_ip()
        load_form["found_time"] = datetime.datetime.now()
        load_form["bug_type"] = random.choice(bug_type)
        load_form["bug_name"] = load_form["type"]
        load_form["bug_level"] = random.choice(bug_type_list)
        load_form["bug_url"] = generate_random_url()
        load_form["bug_status"] = "unknown"
        load_form["notes"] = load_form["token"]
        remove_others(load_form)
        BugLog.objects.create(**load_form)


def remove_others(data: dict):
    data.pop("type")
    data.pop("url")
    data.pop("range")
    data.pop("token")
    data.pop("strategy")
    data.pop("port")
    data.pop("host")
    data.pop("username")
    data.pop("password")
    data.pop("database")
    data.pop("server")


@require_http_methods(["GET", "POST"])
def start(request: HttpRequest):
    if request.method == "GET":
        return render(request, "scan/bug/start.html")

    form = get_form(request.POST,
                    ["url", "range", "type", "token", "strategy", "host", "port", "username", "password", "database",
                     "server"])
    print(form)
    type = form["type"]
    if type == "sql":
        start_sql(form, form["host"], form["port"], form["username"], form["password"], form["database"])
    if type == "stmp":
        start_stmp(form, form["server"], form["username"], form["password"])
    if type == "web":
        start_web(form, form["url"])
    if type == "file":
        start_file(form)

    return success_api()


@require_http_methods(["POST"])
def query(request: HttpRequest):
    print_params(request)
    filters = get_filters(request.POST.get("Param"), [])
    result = BugLog.objects.filter(**filters).order_by("-id")
    return table_data(request, result, result_fields)


def stop(request: HttpRequest):
    return success_api()


@require_http_methods(["POST"])
def delete(request: HttpRequest):
    id = request.POST.get("id")
    BugLog.objects.filter(id=id).delete()
    return success_api()


@require_http_methods(["POST"])
def delete_batch(request: HttpRequest):
    # 获取参数
    ids_list = get_batch_delete_param(request.POST)
    # 执行批量删除操作
    objects_to_delete = BugLog.objects.in_bulk(ids_list)
    for obj in objects_to_delete.values():
        obj.delete()
    # 执行完成
    return success_api()


@require_http_methods(["POST"])
def info(request: HttpRequest):
    id = request.POST.get("id")
    data = BugLog.objects.get(id=id)
    return success_api(get_item(data, result_fields))


@require_http_methods(["GET", "POST"])
def edit(request: HttpRequest):
    if request.method == "GET":
        id = request.GET.get("id")
        obj = BugLog.objects.get(id=id)
        context = {
            "webbug": get_item(obj, result_fields)
        }
        return render(request, "scan/bug/add.html", context)

    form = get_form(request.POST,
                    ["id", "name", "os", "found_by", "bug_type", "bug_name", "bug_level", "bug_url", "bug_status",
                     "notes"])
    BugLog.objects.filter(id=form["id"]).update(**form)
    return success_api()
