from django.test import TestCase

# Create your tests here.
from .utils.mail import EMail
from .models import Notify
from .utils import sqlbak

from django.utils import timezone

class SqlTest(TestCase):

    def test_query_all_monitors(self):
        # 测试查询所有 Monitor 实例
        list_data = Notify.objects.all()
        print("查询所有数据")
        print(list_data)

    def test_add(self):
        print("创建Notify")
        notify = Notify.objects.create(
            notify_type="test",
            notify_mail="test",
            notify_subject="test",
            notify_content="test",
            notify_time=timezone.now(),
            notify_status="test",
        )
        print(notify.id)
        print("创建完成")
