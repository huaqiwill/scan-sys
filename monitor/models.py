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
    id = models.AutoField(primary_key=True)
    notify_type = models.CharField(max_length=200)
    mail_from = models.CharField(max_length=200)
    mail_to = models.CharField(max_length=200)
    mail_content = models.CharField(max_length=200)

    class Meta:
        db_table = "mon_notify"


# class HandleLog(models):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     notify = models.CharField(max_length=200)

#     class Meta:
#         db_table = "mon_handle"


# class RecoverLog(models):
#     id = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     handle = models.CharField(max_length=200)

#     class Meta:
#         db_table = "mon_recover"
