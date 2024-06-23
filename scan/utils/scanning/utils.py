import os
import subprocess
import socket
import platform
import random
import string


def is_host_online(ip):
    """
    检测主机是否在线
    """
    try:
        # Windows
        if os.name == 'nt':
            output = subprocess.check_output(['ping', '-n', '1', '-w', '1000', ip])
        # Unix/Linux/Mac
        else:
            output = subprocess.check_output(['ping', '-c', '1', '-W', '1', ip])
        return True
    except subprocess.CalledProcessError:
        return False


def get_local_ip():
    """
    获取当前的ip地址
    """
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    return local_ip


def get_os_name_and_version():
    # 获取操作系统名称
    os_name = platform.system()
    print(f'操作系统名称: {os_name}')

    # 获取操作系统版本
    os_version = platform.version()
    print(f'操作系统版本: {os_version}')

    return os_name + " " + os_version


def generate_random_url():
    # 定义顶级域名列表
    tlds = ['com', 'org', 'net', 'io', 'co']

    # 生成随机域名
    domain_length = random.randint(5, 10)
    domain = ''.join(random.choices(string.ascii_lowercase + string.digits, k=domain_length))

    # 选择随机顶级域名
    tld = random.choice(tlds)

    # 生成随机路径
    path_length = random.randint(3, 10)
    path = ''.join(random.choices(string.ascii_lowercase + string.digits, k=path_length))

    # 组合成完整的网址
    url = f"http://{domain}.{tld}/{path}"

    return url
