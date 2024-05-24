from django.db import models


# Create your models here.
class Monitor(models.Model):
    user_id = models.CharField(max_length=200)
    request_method = models.CharField(max_length=200)
    request_url = models.CharField(max_length=200)
    ip = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    login_time = models.DateTimeField(auto_now_add=True)
    message = models.CharField(max_length=200)

    class Meta:
        db_table = "mon_montitor"


class Notify(models.Model):
    notify_type = models.CharField("通报类型", max_length=200)
    notify_mail = models.CharField("通报邮箱", max_length=200)
    notify_subject = models.CharField("通报主题", max_length=200)
    notify_content = models.CharField("通报内容", max_length=200)
    notify_time = models.CharField("通报时间", max_length=200)
    notify_status = models.CharField("通报状态", max_length=200)

    class Meta:
        db_table = "mon_notify"


class Attack(models.Model):
    ATTACK_TYPES = (
        ("XSS", "XSS Attack"),
        ("CSRF", "CSRF Attack"),
        ("SQLI", "SQL Injection"),
    )
    attack_type = models.CharField(max_length=10, choices=ATTACK_TYPES)
    timestamp = models.DateTimeField(auto_now_add=True)
    description = models.TextField()


class SystemResource(models.Model):
    resource_type = models.CharField(max_length=50)
    value = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Handle(models.Model):
    request_time = models.DateTimeField()
    request_method = models.CharField(max_length=10)
    request_path = models.CharField(max_length=255)
    response_status = models.IntegerField()
    response_time = models.FloatField()
    disposal_time = models.DateTimeField()
    source_ip = models.GenericIPAddressField()
    attack_type = models.CharField(max_length=10)
    details = models.TextField()
    auto_handled = models.BooleanField()
    handled_status = models.CharField(max_length=20)
    handled_action = models.TextField()
    handled_details = models.TextField()

    class Meta:
        db_table = "mon_handle"


class Recover(models.Model):
    name = models.CharField(max_length=200)
    handle = models.CharField(max_length=200)

    class Meta:
        db_table = "mon_recover"


class RestoreRecord(models.Model):
    status_choices = (
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )
    timestamp = models.DateTimeField(auto_now_add=True)
    filename = models.CharField(max_length=255)
    status = models.CharField(max_length=10, choices=status_choices)
    details = models.TextField()
