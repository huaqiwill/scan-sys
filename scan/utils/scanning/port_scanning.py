"""
端口扫描
"""
import json

import nmap


def fast_and_comprehensive_scan(target_ip: str, range_start=1, range_end=65536):
    nm = nmap.PortScanner()
    nm.scan(hosts=target_ip, arguments=f'-p {range_start}-{range_end} -T4 -A -v')
    return nm[target_ip]


def start_port_scan(host: str):
    """开始端口扫描"""
    ports = fast_and_comprehensive_scan(host, 1, 65535)
    print(json.dumps(ports))
    print(ports)


if __name__ == "__main__":
    start_port_scan("127.0.0.1")
