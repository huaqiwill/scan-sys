from django.urls import path
from . import views

urlpatterns = [
    path("monitor", views.monitor, name="监控预警"),
    path("monitor_query", views.monitor_query, name="监控查询"),
    path("notify", views.notify, name="事件通报"),
    path("handle", views.handle, name="应急处置"),
    path("recover", views.recover, name="业务恢复"),
]
