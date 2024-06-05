import socket
import os
import ipaddress


def get_local_ip():
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def get_subnet_mask():
    ip_output = os.popen('ipconfig').readlines()
    for line in ip_output:
        if '子网掩码' in line:
            subnet_mask = line.split(':')[-1].strip()
            return subnet_mask


def scan_network(local_ip, subnet_mask):
    network = ipaddress.IPv4Network(f"{local_ip}/{subnet_mask}", strict=False)
    online_devices = []

    for ip in network.hosts():
        try:
            socket.setdefaulttimeout(0.5)
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            result = sock.connect_ex((str(ip), 80))
            if result == 0:
                online_devices.append((str(ip), socket.getfqdn(str(ip))))
            sock.close()
        except Exception as e:
            pass

    return online_devices


if __name__ == "__main__":
    local_ip = get_local_ip()
    print(local_ip)
    subnet_mask = get_subnet_mask()
    print(subnet_mask)
    online_devices = scan_network(local_ip, subnet_mask)
    print("在线设备：")
    for device in online_devices:
        print(f"IP地址： {device[0]}, 主机名： {device[1]}")
