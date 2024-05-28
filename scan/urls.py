from django.urls import path
from .views import db_manage, host_scan, report, suggestion, web_scan

urlpatterns = [
    path("host", host_scan.index, name="监控预警"),
    path("host/check", host_scan.check, name="监控查询"),
    path("host/found", host_scan.found, name="get_system_data"),
    path("host/server", host_scan.server, name="index"),
    path("host/port", host_scan.port, name="system_info"),
    
    path("web", web_scan.index, name="监控预警"),
    path("web/scan", web_scan.scan, name="监控预警"),
    
    path("db", db_manage.index, name="监控预警"),
    path("db/config", db_manage.config, name="监控预警"),
    
    path("report", report.index, name="监控预警"),
    
    path("suggestion", suggestion.index, name="监控预警")
]
