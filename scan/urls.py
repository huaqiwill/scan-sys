from django.urls import path
from .views import host, report, suggestion, web_scan, bug, service, port

urlpatterns = [
    # 主机发现
    path("scan/host", host.index, name="主机发现"),
    path("scan/host/start", host.start, name="开始主机发现任务"),
    path("scan/host/stop", host.stop, name="停止主机发现任务"),
    path("scan/host/query", host.query, name="主机发现数据库查询"),
    # 服务识别
    path("scan/service", service.index, name="服务识别"),
    path("scan/service/start", service.start, name="开始服务识别任务"),
    path("scan/service/stop", service.start, name="停止服务识别任务"),
    path("scan/service/query", service.query, name="服务识别数据库查询"),
    # 端口扫描
    path("scan/port", port.index, name="端口扫描"),
    path("scan/port/start", port.start, name="开始端口扫描任务"),
    path("scan/port/stop", port.start, name="停止端口扫描任务"),
    path("scan/port/query", port.query, name="端口扫描数据库拆线呢"),
    # 漏洞扫描
    path("scan/bug", bug.index, name="漏洞检测"),
    path("scan/bug/start", bug.start, name="开始漏洞检测服务"),
    path("scan/bug/stop", bug.start, name="停止漏洞检测服务"),
    path("scan/bug/add", bug.add, name="漏洞检测数据库查询"),

    path("web/scan", web_scan.scan, name="漏洞扫描记录"),
    path("web/scan/add", web_scan.scan_add, name="网页漏洞扫描"),

    path("web/report", report.index, name="报告生成记录"),
    path("web/report/add", report.add, name="漏洞报告生成"),

    path("web/suggestion", suggestion.index, name="修复评估建议"),
    path("web/suggestion/add", suggestion.add, name="监控预警"),
]
