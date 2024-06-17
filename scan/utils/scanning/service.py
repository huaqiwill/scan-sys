"""
服务识别
"""
import socket
import threading

import nmap

from scan.models import ServiceLog


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def identify_services(host: str):
    """服务识别"""
    print("开始服务识别...")
    nm = nmap.PortScanner()
    nm.scan(host, arguments="-sV")
    print("---扫描完成---")
    for port in nm[host]["tcp"]:
        protocol = "tcp"
        service = nm[host]["tcp"][port]["name"]
        version = nm[host]["tcp"][port]["version"]
        state = nm[host]["tcp"][port]["state"]
        product = nm[host]["tcp"][port]["product"]
        data = {
            "ip": host,
            "port": port,
            "protocol": protocol,
            "service": service,
            "version": version,
            "state": state,
            "product": product
        }
        ServiceLog.objects.create(**data)
        print(f"服务识别：host={host} port={port} protocol={protocol} service={service}")
    print("服务识别完成！")


def start_service_scan(ip: str):
    if ip in (None, ""):
        ip = get_local_ip()
    t1 = threading.Thread(target=identify_services, args=(ip,))
    t1.start()


def stop_service_scan():
    pass


if __name__ == "__main__":
    start_service_scan("150.158.199.226")
