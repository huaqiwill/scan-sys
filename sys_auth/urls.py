from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("sys_manage.urls")),
    path("", include("sys_login.urls")),
    path("", include("sys_student.urls")),
    path("", include("sys_monitor.urls")),
]
