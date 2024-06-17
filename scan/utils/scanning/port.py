"""
端口扫描
"""
import json

import nmap
import socket
import threading

from scan.models import PortLog


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def fast_and_comprehensive_scan(target_ip: str, range_start=1, range_end=65536):
    print("开始执行端口扫描...")
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments=f'-p {range_start}-{range_end} -T4 -A -v')
    scan_result = nm[target_ip]
    ports = []
    for port in scan_result['tcp']:
        ports.append(str(port))
    data = {
        "host": target_ip,
        "ports": ",".join(ports)
    }
    PortLog.objects.create(**data)
    print("端口扫描执行结束！")


def start_port_scan(host: str, start_port=1, end_port=65535):
    """开始端口扫描"""
    if host in [None, ""]:
        host = get_local_ip()
    t1 = threading.Thread(target=fast_and_comprehensive_scan, args=(host, start_port, end_port))
    t1.start()


def stop_port_scan():
    pass


if __name__ == "__main__":
    start_port_scan("127.0.0.1")
