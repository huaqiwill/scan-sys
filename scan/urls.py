from django.urls import path
from .views import host, report, suggest, web_bug, bug, service, port

urlpatterns = [
    # 主机发现
    path("scan/host", host.index, name="主机发现"),
    path("scan/host/start", host.start, name="开始主机发现任务"),
    path("scan/host/stop", host.stop, name="停止主机发现任务"),
    path("scan/host/query", host.query, name="主机发现数据库查询"),
    path("scan/host/delete", host.delete, name="主机发现数据库删除"),
    # 服务识别
    path("scan/service", service.index, name="服务识别"),
    path("scan/service/start", service.start, name="开始服务识别任务"),
    path("scan/service/stop", service.start, name="停止服务识别任务"),
    path("scan/service/query", service.query, name="服务识别数据库查询"),
    path("scan/service/delete", service.delete, name="服务识别数据库查询"),
    # 端口扫描
    path("scan/port", port.index, name="端口扫描"),
    path("scan/port/start", port.start, name="开始端口扫描任务"),
    path("scan/port/stop", port.start, name="停止端口扫描任务"),
    path("scan/port/query", port.query, name="端口扫描数据库拆线呢"),
    path("scan/port/delete", port.delete, name="端口扫描数据库拆线呢"),
    # 漏洞扫描
    path("scan/bug", bug.index, name="漏洞检测"),
    path("scan/bug/start", bug.start, name="开始漏洞检测服务"),
    path("scan/bug/stop", bug.stop, name="停止漏洞检测服务"),
    path("scan/bug/query", bug.query, name="漏洞检测数据库查询"),
    path("scan/bug/delete", bug.delete, name="漏洞检测数据库查询"),
    # 网页漏洞扫描
    path("scan/webbug", web_bug.index, name="漏洞扫描记录"),
    path("scan/webbug/start", web_bug.start, name="漏洞扫描记录"),
    path("scan/webbug/stop", web_bug.stop, name="漏洞扫描记录"),
    path("scan/webbug/query", web_bug.query, name="网页漏洞扫描"),
    path("scan/webbug/delete", web_bug.delete, name="网页漏洞扫描"),
    # 漏洞报告生成
    path("scan/report", report.index, name="报告生成记录"),
    path("scan/report/add", report.add, name="漏洞报告生成"),
    path("scan/report/query", report.query, name="漏洞报告数据库查询"),
    path("scan/report/delete", report.delete, name="漏洞报告数据库查询"),
    # 修复评估建议
    path("scan/suggest", suggest.index, name="修复评估建议"),
    path("scan/suggest/add", suggest.add, name="修复评估建议新增"),
    path("scan/suggest/query", suggest.query, name="修复评估建议数据库查询"),
    path("scan/suggest/delete", suggest.delete, name="修复评估建议数据库查询"),
]
