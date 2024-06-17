from django.urls import path
from .views import host, report, suggest, web_bug, bug, service, port

urlpatterns = [
    # 主机发现
    path("scan/host", host.index, name="首页"),
    path("scan/host/start", host.start, name="开始"),
    path("scan/host/stop", host.stop, name="停止"),
    path("scan/host/query", host.query, name="查询"),
    path("scan/host/delete", host.delete, name="删除"),
    path("scan/host/deleteBatch", host.deleteBatch, name="批量删除"),
    path("scan/host/info", host.info, name="信息"),
    # 服务识别
    path("scan/service", service.index, name="首页"),
    path("scan/service/start", service.start, name="开始识别"),
    path("scan/service/stop", service.start, name="停止识别"),
    path("scan/service/query", service.query, name="查询"),
    path("scan/service/delete", service.delete, name="删除"),
    path("scan/service/deleteBatch", service.deleteBatch, name="批量删除"),
    path("scan/service/info", service.info, name="信息"),
    # 端口扫描
    path("scan/port", port.index, name="首页"),
    path("scan/port/start", port.start, name="开始扫描"),
    path("scan/port/stop", port.start, name="停止扫描"),
    path("scan/port/query", port.query, name="查询"),
    path("scan/port/delete", port.delete, name="删除"),
    path("scan/port/deleteBatch", port.deleteBatch, name="批量删除"),
    path("scan/port/info", port.info, name="信息"),
    # 漏洞扫描
    path("scan/bug", bug.index, name="首页"),
    path("scan/bug/start", bug.start, name="开始扫描"),
    path("scan/bug/stop", bug.stop, name="停止扫描"),
    path("scan/bug/query", bug.query, name="查询"),
    path("scan/bug/delete", bug.delete, name="删除"),
    path("scan/bug/deleteBatch", bug.deleteBatch, name="批量删除"),
    path("scan/bug/info", bug.info, name="信息"),
    # 网页漏洞扫描
    path("scan/webbug", web_bug.index, name="首页"),
    path("scan/webbug/start", web_bug.start, name="开始扫描"),
    path("scan/webbug/stop", web_bug.stop, name="停止扫描"),
    path("scan/webbug/query", web_bug.query, name="查询"),
    path("scan/webbug/delete", web_bug.delete, name="删除"),
    path("scan/webbug/deleteBatch", web_bug.deleteBatch, name="批量删除"),
    path("scan/webbug/info", web_bug.info, name="信息"),
    # 漏洞报告生成
    path("scan/report", report.index, name="首页"),
    path("scan/report/add", report.add, name="开始扫描"),
    path("scan/report/query", report.query, name="停止扫描"),
    path("scan/report/delete", report.delete, name="删除"),
    path("scan/report/delete", report.deleteBatch, name="批量删除"),
    path("scan/report/info", report.info, name="信息"),
    path("scan/report/download", report.download, name="下载报告"),
    # 修复评估建议
    path("scan/suggest", suggest.index, name="首页"),
    path("scan/suggest/add", suggest.add, name="新增"),
    path("scan/suggest/query", suggest.query, name="查询"),
    path("scan/suggest/delete", suggest.delete, name="删除"),
    path("scan/suggest/deleteBatch", suggest.deleteBatch, name="批量删除"),
    path("scan/suggest/info", suggest.info, name="信息"),
]
