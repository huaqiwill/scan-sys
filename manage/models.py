# encoding:utf-8
from django.db import models

# Create your models here.
from django.utils import timezone


class User(models.Model):
    objects = None
    id_number = models.CharField("用户账号", max_length=30)
    id_password = models.CharField("用户密码", max_length=255)
    user_name = models.CharField("用户名称", max_length=30)
    department = models.CharField("部门", max_length=50, blank=True, null=True)
    position = models.CharField("职位", max_length=50, blank=True, null=True)
    role_id = models.IntegerField("角色id", null=True)
    role_des = models.CharField("角色描述", max_length=30, null=True)
    user_status = models.IntegerField("用户状态", default=1)
    email = models.CharField("email", max_length=50, blank=True, null=True)
    create_time = models.DateTimeField("创建时间", default=timezone.now)

    class Meta:
        db_table = "sys_user"


class Role(models.Model):
    objects = None
    role_value = models.IntegerField("角色值")
    name = models.CharField("角色名称", max_length=50, null=True)
    code = models.CharField("角色标识", max_length=50)
    enable = models.IntegerField("是否启用")
    remark = models.CharField("备注", max_length=255, null=True)
    details = models.CharField("详情", max_length=255, null=True)
    sort = models.IntegerField("排序", null=True)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField("更新时间", auto_now=True)  # 更新时间

    class Meta:
        db_table = "sys_role"


class Power(models.Model):
    objects = None
    name = models.CharField("权限名称", max_length=50)
    type = models.IntegerField("权限类型")
    code = models.CharField("权限标识", max_length=30, null=True)
    url = models.CharField("权限路径", max_length=30, null=True)
    open_type = models.CharField("权限类型-中文", max_length=20, null=True)
    parent_id = models.IntegerField("父类编号", null=True)
    icon = models.CharField("图标", max_length=50, null=True)
    sort = models.IntegerField("排序", null=True)
    enable = models.IntegerField("是否开启", default=1)
    create_time = models.DateTimeField("创建时间", auto_now_add=True)  # 创建时间
    update_time = models.DateTimeField("更新时间", auto_now=True)  # 更新时间

    class Meta:
        db_table = "sys_power"  # 系统权限


class RolePower(models.Model):
    objects = None
    role_id = models.IntegerField("角色id")
    power_id = models.IntegerField("权限id")
    power_type = models.IntegerField("类型")  # 0-目录 1-菜单 2-按钮 3-其他

    class Meta:
        db_table = "role_power"  # 角色权限
