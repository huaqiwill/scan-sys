from django.urls import path
from .views import db_manage, host_scan, report, suggestion, web_scan

urlpatterns = [
    path("host", host_scan.index, name="监控预警"),
    path("host/check", host_scan.check, name="漏洞检测"),
    path("host/check/add", host_scan.check_add, name="漏洞检测（add）"),
    path("host/found", host_scan.found, name="主机发现"),
    path("host/found/add", host_scan.found_add, name="主机发现（add）"),
    path("host/found/query", host_scan.found_query, name="主机发现（add）"),
    path("host/service", host_scan.server, name="服务识别"),
    path("host/service/add", host_scan.server_add, name="服务识别_add"),
    path("host/service/query", host_scan.server_query, name="服务识别_query"),
    path("host/port", host_scan.port, name="端口识别"),
    path("host/port/add", host_scan.port_add, name="端口识别（add）"),
    path("host/port/query", host_scan.port_query, name="端口识别"),

    path("web", web_scan.index, name="漏洞扫描"),

    path("web/scan", web_scan.scan, name="漏洞扫描记录"),
    path("web/scan/add", web_scan.scan_add, name="网页漏洞扫描"),

    path("web/report", report.index, name="报告生成记录"),
    path("web/report/add", report.add, name="漏洞报告生成"),

    path("web/suggestion", suggestion.index, name="修复评估建议"),
    path("web/suggestion/add", suggestion.add, name="监控预警"),
]
