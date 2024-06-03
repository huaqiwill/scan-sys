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
        service = nm[host]["tcp"][port]["name"]
        version = nm[host]["tcp"][port]["version"]
        services.append({"port": port, "service": service, "version": version})
    return services


def start_service_discovery():
    # hosts = [{"ip": "192.168.2.109"}]
    # for host in hosts:
    #     services = identify_services(host["ip"])
    #     for service in services:
    #         print(
    #             f"Host: {host['ip']}, Port: {service['port']}, Service: {service['service']}, Version: {service['version']}"
    #         )
    ip = "192.168.2.109"
    services = identify_services(ip)
    for service in services:
        print(
            f"Host: {ip}, Port: {service['port']}, Service: {service['service']}, Version: {service['version']}"
        )
        service["ip"] = ip
    return services


if __name__ == "__main__":
    start_service_discovery()
