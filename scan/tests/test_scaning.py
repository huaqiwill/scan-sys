from scan.utils.scanning import port
from django.test import TestCase


class TestPortScanning(TestCase):
    def test_port_scanning(self):
        print(port_scanning.scan_ports('192.168.1.1', 80))


