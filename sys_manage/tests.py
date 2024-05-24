from django.test import TestCase
from .models import User

# Create your tests here.
class SqlTestCase(TestCase):
    def test_add(self):
        user = User.objects.create( id_number="123456789", id_password="123456", user_name="test", department="test", position="test", role_id=1, role_des="test", user_status=1, email="test@test.com" )
        # 确认用户创建成功
        self.assertIsNotNone(user.id)
        print(user)
    
    def test_list(self):
        user_list = User.objects.all()
        print(user_list)