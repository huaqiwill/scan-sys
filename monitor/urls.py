from django.urls import path
from . import views

urlpatterns = [
    # path("monitor", views.monitor, name="监控预警"),
    path("monitor_query", views.monitor_query, name="监控查询"),
    path("notify", views.notify, name="事件通报"),
    path("handle", views.handle, name="应急处置"),
    # path("recover", views.recover, name="业务恢复"),
    path('monitor', views.dashboard, name='dashboard'),
    path('get_attack_data', views.get_attack_data, name='get_attack_data'),
    path('get_system_data', views.get_system_data, name='get_system_data'),
    path('recover', views.restore_page, name='restore_page'),
    path('get_restore_records/', views.get_restore_records, name='get_restore_records'),
]
