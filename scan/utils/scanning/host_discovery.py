"""
主机发现
"""

from scapy.all import ARP, Ether, srp


def discover_hosts(network):
    arp = ARP(pdst=network)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether / arp

    result = srp(packet, timeout=2, verbose=False)[0]

    hosts = []
    for sent, received in result:
        hosts.append({"ip": received.psrc, "mac": received.hwsrc})

    return hosts


# 使用示例
network = "192.168.2.109"
hosts = discover_hosts(network)
for host in hosts:
    print(f"IP: {host['ip']}, MAC: {host['mac']}")
