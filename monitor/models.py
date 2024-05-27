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

    SubStaus = (
        ("enable", "启用"),
        ("disable", "禁用"),
    )
    sub_email = models.CharField("订阅者邮件", max_length=200)
    sub_status = models.CharField("订阅状态", max_length=50, choices=SubStaus)
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
        ("success", "success"),
        ("falied", "falied"),
    )
    status_yes_no = (
        ("yes", "yes"),
        ("no,", "no"),
    )
    attack_type = (
        ("qss", "QSS"),
        ("sql", "sql"),
        ("xss", "XSS"),
        ("csrf", "CSRF"),
    )
    handle_event = models.CharField("处置事件", max_length=100)
    handle_attack_type = models.CharField(
        "处理攻击类型", max_length=100, choices=attack_type
    )
    handle_auto = models.CharField(
        "是否自动处理", max_length=100, choices=status_yes_no
    )
    handle_action = models.CharField("处理动作", max_length=100)
    handle_ip = models.CharField("源IP", max_length=100)
    handle_file = models.CharField("处理文件", max_length=100)
    handle_detail = models.CharField("处理详情", max_length=100)
    handle_status = models.CharField("是否处理", max_length=100, choices=status_yes_no)
    handle_restore = models.CharField("是否恢复", max_length=100, choices=status_yes_no)
    handle_backup_time = models.DateTimeField("备份时间", auto_now_add=True)
    handle_restore_time = models.DateTimeField("还原时间", auto_now_add=True)
