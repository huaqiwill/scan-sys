from django.urls import path
from . import views

urlpatterns = [
    # 事件监控预警
    path("monitor", views.dashboard, name="监控预警"),
    path("monitor_query", views.monitor_query, name="监控查询"),
    path("get_attack_data", views.get_attack_data, name="get_attack_data"),
    path("get_system_data", views.get_system_data, name="get_system_data"),
    path("get_restore_records/", views.get_restore_records, name="get_restore_records"),

    # 安全事件通报
    path("notify", views.notify, name="事件通报"),
    path("notify_list", views.notify_list),

    # 应急事件处理
    path("handle", views.handle, name="应急处置"),

    # 数据业务恢复
    path("recover", views.restore_page, name="restore_page"),
]
