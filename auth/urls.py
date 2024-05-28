from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("manage.urls")),
    path("", include("login.urls")),
    path("", include("monitor.urls")),
    path("", include("scan.urls")),
]
