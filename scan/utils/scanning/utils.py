import os
import subprocess
import socket


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
