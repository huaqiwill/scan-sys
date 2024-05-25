from django.db import models
from django.utils import timezone


class Logo(models.Model):
    objects = None
    name = models.CharField("菜单名称", max_length=50, null=True)
    desc = models.CharField("菜单描述", max_length=50, null=True)
    type = models.IntegerField("菜单类型", null=True)
    url = models.CharField("菜单url", max_length=50, null=True)
    parent_id = models.IntegerField("父级id", null=True)
    icon = models.CharField("图标", max_length=50, null=True)
    sort = models.IntegerField("排序", null=True)

    class Meta:
        db_table = "web_logo"


class Log(models.Model):
    objects = None
    method = models.CharField("请求方法", max_length=10)
    uid = models.CharField("用户ID", max_length=10)
    url = models.CharField("请求URL", max_length=50, null=True)
    desc = models.TextField("备注", null=True)
    ip = models.CharField("请求方法", max_length=30, null=True)
    success = models.IntegerField("是否成功", null=True)
    user_agent = models.CharField("请求方法", max_length=255, null=True)
    create_time = models.DateTimeField("创建时间", default=timezone.now)

    class Meta:
        db_table = "sys_log"
