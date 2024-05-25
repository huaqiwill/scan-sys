from django.test import TestCase

# Create your tests here.
from .utils.mail import EMail
from .models import Notify
from .utils import sqlbak

from django.utils import timezone
from .utils import sys_monitor_m


class SqlTest(TestCase):
    def test_mon(self):
        sys_monitor_m.network()
