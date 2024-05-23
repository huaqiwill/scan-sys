from django.db import models


# Create your models here.
# class Monitor(models.Model):
#     id_ = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     ip = models.CharField(max_length=200)
#     port = models.CharField(max_length=200)
#     username = models.CharField(max_length=200)
#     password = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Notify(models.Model):
#     id_ = models.AutoField(primary_key=True)
#     notify_type = models.CharField(max_length=200)
#     mail_from = models.ForeignKey(Monitor, on_delete=models.CASCADE)
#     mail_to = models.ForeignKey(Monitor, on_delete=models.CASCADE)
#     mail_content = models.CharField(max_length=200)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Handle(models.Model):
#     id_ = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     notify = models.ForeignKey(Notify, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)


# class Recover(models.Model):
#     id_ = models.AutoField(primary_key=True)
#     name = models.CharField(max_length=200)
#     handle = models.ForeignKey(Handle, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)
