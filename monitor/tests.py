from django.test import TestCase

# Create your tests here.
from .utils.mail import EMail
from .models import Monitor
from .utils import sqlbak


class SqlTest(TestCase):
    def setUp(self):
        pass

    def test_backup(self):
        print("备份数据库")
        sqlbak.backup()

    def test_restore(self):
        print("还原数据库")
        sqlbak.restore()


class Test():

    def setUp(self):
        # 这个方法在每个测试方法执行之前运行
        Monitor.objects.create(
            user_id="1", request_method="post", request_url="basiu", ip="127.0.0.1"
        )

    def test_create_monitor(self):
        # 测试创建 Monitor 实例
        monitor = Monitor.objects.get(request_url="basiu")
        self.assertEqual(monitor.user_id, "1")
        self.assertEqual(monitor.request_method, "post")
        self.assertEqual(monitor.ip, "127.0.0.1")

    def test_query_all_monitors(self):
        # 测试查询所有 Monitor 实例
        list_data = Monitor.objects.all()
        self.assertEqual(list_data.count(), 1)
        print(list_data)
