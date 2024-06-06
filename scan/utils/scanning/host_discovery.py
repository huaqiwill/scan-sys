"""
主机发现
识别网络中的活跃设备：确定哪些设备（如计算机、服务器、打印机、路由器等）在网络上是在线的。

ARP扫描：使用地址解析协议（ARP）发送请求，识别同一子网内的活跃设备。
ICMP扫描：使用互联网控制消息协议（ICMP）发送回显请求（ping），检测设备的在线状态。
端口扫描：扫描常用端口，识别运行特定服务的设备。
SNMP扫描：使用简单网络管理协议（SNMP）收集网络设备的状态和配置信息。
Nmap：一个强大的网络扫描工具，支持多种扫描技术，广泛用于主机发现和网络安全审计。

ip地址
mac地址
操作系统信息
供应商信息
"""
import scapy.all as scapy
import netifaces
import subprocess


def get_default_gateway_ip():
    """获取当前网关的IP"""
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default')
    if default_gateway is not None:
        return default_gateway[netifaces.AF_INET][0]
    else:
        raise RuntimeError("Default gateway not index")


def get_network_ip_range():
    """获取网络ip范围"""
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    addresses = netifaces.ifaddresses(interface)
    netmask = addresses[netifaces.AF_INET][0]['netmask']
    ip_address = addresses[netifaces.AF_INET][0]['addr']

    ip_parts = ip_address.split('.')
    mask_parts = netmask.split('.')

    network_parts = [str(int(ip_parts[i]) & int(mask_parts[i])) for i in range(4)]
    network_ip = '.'.join(network_parts)

    return f"{network_ip}/24"


def scan_host(ip_range):
    """主机发现扫描"""
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    device_list = []
    for element in answered_list:
        print(element[0])
        ip = element[1].psrc
        mac = element[1].hwsrc
        os_info, vendor_info = get_os_and_vendor(ip)

        device_list.append({
            'ip': ip,
            'mac': mac,
            'os': os_info,
            'vendor': vendor_info
        })

    return device_list


def get_os_and_vendor(ip):
    cmd = f"nmap -sS -O {ip}"
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
    output = result.stdout
    lines = output.split("\n")
    os_info = "unknown os"
    vendor_info = "unknown vendor"
    for line in lines:
        if "OS details:" in line:
            os_info = line.split(":")[1].strip()
        if "Device type:" in line:
            vendor_info = line.split(":")[1].strip()
    return os_info, vendor_info


def start_host_discovery():
    try:
        network_ip_range = get_network_ip_range()
        devices_list = scan_host(network_ip_range)
        print(devices_list)
        return devices_list
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    devices = start_host_discovery()
