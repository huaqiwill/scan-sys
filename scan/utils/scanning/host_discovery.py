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


def get_default_gateway_ip():
    gateways = netifaces.gateways()
    default_gateway = gateways.get('default')
    if default_gateway is not None:
        return default_gateway[netifaces.AF_INET][0]
    else:
        raise RuntimeError("Default gateway not found")


def get_network_ip_range():
    interface = netifaces.gateways()['default'][netifaces.AF_INET][1]
    addresses = netifaces.ifaddresses(interface)
    netmask = addresses[netifaces.AF_INET][0]['netmask']
    ip_address = addresses[netifaces.AF_INET][0]['addr']

    ip_parts = ip_address.split('.')
    mask_parts = netmask.split('.')

    network_parts = [str(int(ip_parts[i]) & int(mask_parts[i])) for i in range(4)]
    network_ip = '.'.join(network_parts)

    return f"{network_ip}/24"


def scan(ip_range):
    arp_request = scapy.ARP(pdst=ip_range)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast / arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]

    devices = []
    for element in answered_list:
        print(element[0])
        devices.append({
            'ip': element[1].psrc,
            'mac': element[1].hwsrc
        })

    return devices


def print_devices(devices):
    print("IP\t\t\tMAC Address\n-----------------------------------------")
    for device in devices:
        print(f"{device['ip']}\t\t{device['mac']}")


def start_host_discovery():
    try:
        default_gateway_ip = get_default_gateway_ip()
        network_ip_range = get_network_ip_range()
        devices = scan(network_ip_range)
        print_devices(devices)
        return devices
    except Exception as e:
        print(f"Error: {e}")
        return []


if __name__ == "__main__":
    devices = start_host_discovery()
