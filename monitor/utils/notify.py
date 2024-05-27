from ..models import Notify
from django.core.mail import send_mail
from django.utils import timezone
from .mail import EMail
from ..models import SubEmail
from threading import Thread


def add_back(notify_type: str, notify_subjet: str, notify_content: str):
    print("任务有启动")
    subemails = SubEmail.objects.filter(sub_status="enable").all()
    notify_mail_list = ["3173484026@qq.com"]
    for sub in subemails:
        notify_mail_list.append(sub.sub_email)
    notify_mail_list = set(notify_mail_list)

    print("notify_add")
    print("待发送列表：", notify_mail_list)
    for notify_mail in notify_mail_list:
        status = "failed"
        try:
            print(notify_content, notify_type, notify_mail)
            EMail().send_email(
                subject=notify_subjet, content=notify_content, to_addr=notify_mail
            )
            status = "success"
            print("邮件发送成功")
        except:
            status = "failed"
            print("邮件发送失败")
        notify = Notify(
            notify_type=notify_type,
            notify_mail=notify_mail,
            notify_subject=notify_subjet,
            notify_content=notify_content,
            notify_time=timezone.now(),
            notify_status=status,
        )
        notify.save()


def notify_add(notify_type: str, notify_subjet: str, notify_content: str):
    print("邮件后台发送")
    t1 = Thread(target=add_back, args=(notify_type, notify_subjet, notify_content))
    t1.start()
