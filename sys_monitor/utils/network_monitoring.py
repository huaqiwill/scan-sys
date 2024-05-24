"""
网络监控模块
"""

import subprocess


def check_ip(ip):
    result = subprocess.run(["whois", ip], capture_output=True, text=True)
    whois_data = result.stdout
    if "Bad IP" in whois_data:
        block_ip(ip)


def block_ip(ip):
    subprocess.run(["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"])
    print(f"已封锁恶意IP地址：{ip}")


# 模拟检测IP并封锁
check_ip("1.2.3.4")
