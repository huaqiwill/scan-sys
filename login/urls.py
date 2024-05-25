from django.urls import path
from login import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login, name="登录"),
    path("get-captcha", views.get_captcha, name="获取验证码"),
    path("login-in", views.login_in, name="登录成功"),
    path("login-out", views.login_out, name="退出登录"),
    path("web-menu", views.web_menu, name="网页目录"),
    path("home", views.home, name="首页"),
    path("echarts", views.echarts, name="图表"),
    path("user-setting", views.user_setting, name="用户基本资料"),
    path("user-info-query", views.user_info_query, name="用户信息查询"),
    path("user-password", views.user_password, name="用户密码修改"),
]

# handler404 = 'login.views.page_not_found'
# handler500 = 'login.views.page_error'
