from django.utils.deprecation import MiddlewareMixin
from django.middleware.csrf import CsrfViewMiddleware
import re
from django.http import HttpResponseBadRequest
from .utils.mail import EMail




class StrongCsrfViewMiddleware(CsrfViewMiddleware):
    def __init__(self, get_response=None):
        super().__init__(get_response)

    def process_request(self, request):
        print("处理请求中间件1")
        super().process_request(request)

    def process_view(self, request, callback, chain):
        print("处理响应中间件1")
        super().process_view(request, callback, chain)


class SqlInjectionMiddleware:
    def __init__(self, get_response):
        print("**************************************************")
        print("SQL注入检测中间件")
        print("**************************************************")
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        # 检查请求参数中是否包含SQL关键字
        if request.method == "GET":
            query_string = request.META["QUERY_STRING"]
        if request.method == "POST":
            query_string = request.body.decode("utf-8")
        if self.is_sql_injection(query_string):
            print("可疑的SQL注入尝试")
            # EMail().send_email_sync("可疑的SQL注入尝试")

    def is_sql_injection(self, value):
        # 检测SQL关键字
        sql_keywords = [
            "SELECT",
            "UPDATE",
            "DELETE",
            "INSERT",
            "DROP",
            "ALTER",
            "CREATE",
            "UNION",
            "--",
            "/*",
            "*/",
        ]
        for keyword in sql_keywords:
            if keyword.lower() in value.lower():
                return True

        # 检测注释符号
        if re.search(r"(--|#)", value):
            return True

        # 检测特殊字符
        special_chars = [";", "&", "<", ">", "=", '"', "'"]
        for char in special_chars:
            if char in value:
                return True

        # 检测括号
        if "(" in value and ")" in value:
            return True

        # 检测OR和AND操作符
        if " OR " in value.upper() or " AND " in value.upper():
            return True

        return False
