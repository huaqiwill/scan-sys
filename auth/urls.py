from django.urls import path, include

urlpatterns = [
    path("", include("manage.urls")),
    path("", include("login.urls")),
    path("", include("monitor.urls")),
    path("", include("scan.urls")),
]
