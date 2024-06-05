"""
服务识别
"""
import nmap


def identify_services(host):
    """服务识别"""
    nm = nmap.PortScanner()
    nm.scan(host, arguments="-sV")
    services = []
    for port in nm[host]["tcp"]:
        protocol = "tcp"
        # print(nm[host]["tcp"][port])
        service = nm[host]["tcp"][port]["name"]
        version = nm[host]["tcp"][port]["version"]
        state = nm[host]["tcp"][port]["state"]
        product = nm[host]["tcp"][port]["product"]
        services.append({
            "port": port,
            "service": service,
            "version": version,
            "protocol": protocol,
            "state": state,
            "product": product
        })
    return services


def start_service_discovery():
    # hosts = [{"ip": "192.168.2.109"}]
    # for host in hosts:
    #     services = identify_services(host["ip"])
    #     for service in services:
    #         print(
    #             f"Host: {host['ip']}, Port: {service['port']}, Service: {service['service']}, Version: {service['version']}"
    #         )
    # ip = "192.168.2.109"
    ip = "150.158.199.226"
    services = identify_services(ip)
    for service in services:
        service["ip"] = ip
        print(service)
    return services


if __name__ == "__main__":
    start_service_discovery()
