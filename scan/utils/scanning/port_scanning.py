"""
端口扫描
"""
import nmap


def scan_ports(host_name: str, range_start=1, range_end=65535):
    """端口扫描"""
    nm = nmap.PortScanner()
    nm.scan(host_name, "{0}-{1}".format(range_start, range_end))
    ports = nm[host]["tcp"]
    data_list = []
    for port in ports:
        data_list.append({
            "port": port,
            "state": ports[port]["state"]
        })
    return ports


def start_port_scan():
    host = "192.168.2.109"
    ports = scan_ports(host)
    port_list = []
    for port in ports:
        print(f"Port {port}: {ports[port]['state']}")
        port_list.append(port)
    return [{"host": host, "ports": ",".join(port_list)}]
    # return ports


if __name__ == "__main__":
    start_port_scan()
