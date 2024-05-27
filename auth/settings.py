import os
from pathlib import Path
import configparser

config = configparser.ConfigParser()
config.read(os.path.join(os.getcwd(), "config.ini"), encoding="utf8")
db_config = config["sql"]
email_config = config["mail"]

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-@g^5499a$7@l^$0i^gg@2aa_b8k^vzf#*r3r4@u^pjhw761)f5"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["*"]

# Application definition

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "login",
    "monitor",
    "manage",
    "rest_framework",
    # 访问频率限制
    "ratelimit",
    # XSS攻击检测
    # "xss_protector",
    "django_crontab",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    # 'django.middleware.csrf.CsrfViewMiddleware', # csrf验证
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    # "monitor.middlewares.StrongCsrfViewMiddleware",
    "monitor.middlewares.SqlInjectionMiddleware",
    # "monitor.middlewares.CustomXssProtectorMiddleware"
]

ROOT_URLCONF = "auth.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [os.path.join(BASE_DIR, "templates")],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "auth.wsgi.application"

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": db_config["database"],
        "USER": db_config["user"],
        "PASSWORD": db_config["password"],
        "PORT": db_config["port"],
        "HOST": db_config["host"],
    },
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "zh-hans"

TIME_ZONE = "Asia/Shanghai"

USE_I18N = True

USE_TZ = False

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = "static/"

STATICFILES_DIRS = [(os.path.join(BASE_DIR, "static"))]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

X_FRAME_OPTIONS = "SAMEORIGIN"

"""访问频率限制工具"""
RATELIMIT_ENABLE = True  # 启用速率限制功能
RATELIMIT_USE_CACHE = "default"  # 使用默认缓存设置
RATELIMIT_VIEW = "monitor.views.ratelimit_handler"  # 自定义速率限制处理视图函数
RATELIMIT_RATE = "10/m"  # 允许每分钟10个请求
"""XSS攻击检测"""
# XSS_PROTECTION_ENABLED = True


"""邮件配置"""
EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = email_config["host"]
EMAIL_PORT = email_config["port"]
EMAIL_HOST_USER = email_config["from_addr"]
EMAIL_HOST_PASSWORD = email_config["password"]
# DEFAULT_FROM_EMAIL = ""
EMAIL_USE_TLS = False

# 定时任务
"""
*    *    *    *    * ：分别表示 分(0-59)、时(0-23)、天(1 - 31)、月(1 - 12) 、周(星期中星期几 (0 - 7) (0 7 均为周天))
crontab范例：
每五分钟执行    */5 * * * *
每小时执行     0 * * * *
每天执行       0 0 * * *
每周一执行       0 0 * * 1
每月执行       0 0 1 * *
每天23点执行   0 23 * * *
"""
CRONJOBS = [
    (
        "*/1 * * * *",
        "base.crontabs.confdict_handle",
        " >> /tmp/logs/confdict_handle.log",
    ),  # 注意：/tmp/base_api 目录要手动创建
]
