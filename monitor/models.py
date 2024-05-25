from django.db import models


class Monitor(models.Model):
    """
    监控事件
    """
    ATTACK_TYPES = (
        ("XSS", "XSS Attack"),  # XSS攻击
        ("CSRF", "CSRF Attack"),  # CSRF攻击
        ("SQLI", "SQL Injection"),  # SQL注入
    )
    user_id = models.CharField("用户ID", max_length=200)
    request_url = models.CharField("请求URL", max_length=200)
    request_method = models.CharField("请求方法", max_length=200)
    request_data = models.CharField("携带数据", max_length=200)
    request_ip = models.CharField("请求来源IP", max_length=200)
    attack_type = models.CharField("攻击类型", max_length=10, choices=ATTACK_TYPES)
    attack_time = models.DateTimeField("攻击事件", auto_now_add=True)
    description = models.TextField("事件描述")

    def __str__(self):
        return (
                "{"
                + "id :"
                + str(self.id)
                + "user_id:"
                + self.user_id
                + ", request_method :"
                + self.request_method
                + ", request_url :"
                + self.request_url
                + ", request_ip :"
                + self.request_ip
                + ", attack_type :"
                + self.attack_type
                + ", attack_time :"
                + str(self.attack_time)
                + ", description :"
                + self.description
                + "}"
        )


class Notify(models.Model):
    """
    通报记录
    """
    notify_type = models.CharField("通报类型", max_length=200)
    notify_mail = models.CharField("通报邮箱", max_length=200)
    notify_subject = models.CharField("通报主题", max_length=200)
    notify_content = models.CharField("通报内容", max_length=200)
    notify_time = models.DateTimeField("通报时间", max_length=200)
    notify_status = models.CharField("通报状态", max_length=200)

    def __str__(self) -> str:
        return (
                "{"
                + "notify_type :"
                + self.notify_type
                + ", notify_mail :"
                + self.notify_mail
                + ", notify_subject :"
                + self.notify_subject
                + ", notify_content :"
                + self.notify_content
                + ", notify_time :"
                + str(self.notify_time)
                + ", notify_status :"
                + self.notify_status
                + "}"
        )


class SubEmail(models.Model):
    """
    通知订阅者
    """
    sub_email = models.CharField("订阅者邮件", max_length=200)
    sub_status = models.IntegerField("订阅状态")
    sub_date = models.DateField("订阅日期")
    sub_name = models.CharField("订阅人", max_length=200)
    user_id = models.CharField("当前用户ID", max_length=200)

    def to_dict(self):
        return {
            "sub_email": self.sub_email,
            "sub_status": self.sub_status,
            "sub_date": self.sub_date,
            "sub_name": self.sub_name,
            "user_id": self.user_id,
        }


class Handle(models.Model):
    """
    应急处置记录
    """
    status_choices = (
        ("SUCCESS", "Success"),
        ("FAILED", "Failed"),
    )
    request_time = models.DateTimeField("请求时间")
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
    filename = models.CharField("备份文件名", max_length=255)
    timestamp = models.DateTimeField("备份时间", auto_now_add=True)
    status = models.CharField("处置状态", max_length=10, choices=status_choices)
    is_restore = models.IntegerField("是否恢复")
