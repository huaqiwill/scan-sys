from django.urls import path
from . import views

urlpatterns = [
    # 事件监控预警
    path("monitor", views.monitor_dashboard, name="监控预警"),
    path("monitor/query", views.monitor_query, name="监控查询"),
    path("monitor/system_data", views.monitor_get_system_data, name="get_system_data"),
    path("monitor/index", views.index, name="index"),
    path("monitor/system_info", views.get_system_info, name="system_info"),
    # 安全事件通报
    path("notify", views.notify, name="事件通报"),
    path("notify/query", views.notify_query, name="事件通报查询"),
    path("notify/delete", views.notify_delete, name="事件通报删除"),
    # 订阅列表
    path("subemail", views.sub_email, name="订阅列表"),
    path("subemail/query", views.sub_email_query, name="订阅列表查询"),
    path("subemail/add", views.sub_email_add, name="订阅列表添加"),
    path("subemail/edit", views.sub_email_edit, name="订阅列表修改"),
    path("subemail/delete", views.sub_email_delete, name="订阅列表删除"),
    # 应急事件处理
    path("handle", views.handle, name="应急处置页面"),
    path("handle/query", views.handle_query, name="应急处置查询"),
    path("handle/delete", views.handle_delete, name="应急处置记录删除"),
    # 数据业务恢复
    path("restore", views.restore, name="业务恢复"),
    path("restore/query", views.restore_query, name="业务恢复查询"),
    path("restore/delete", views.restore_delete, name="业务恢复记录删除"),
]
