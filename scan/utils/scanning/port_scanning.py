"""
端口扫描
"""
import nmap


def scan_ports(host):
    """端口扫描"""
    nm = nmap.PortScanner()
    nm.scan(host, "1-65535")
    print(nm.scaninfo())
    return nm[host]["tcp"]


if __name__ == "__main__":
    host = "192.168.2.109"
    ports = scan_ports(host)
    for port in ports:
        print(f"Port {port}: {ports[port]['state']}")
