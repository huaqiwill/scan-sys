"""
服务识别
"""
import nmap


def identify_services(host):
    nm = nmap.PortScanner()
    nm.scan(host, arguments="-sV")
    services = []
    for port in nm[host]["tcp"]:
        service = nm[host]["tcp"][port]["name"]
        version = nm[host]["tcp"][port]["version"]
        services.append({"port": port, "service": service, "version": version})
    return services


if __name__ == "__main__":
    hosts = [{"ip": "192.168.2.109"}]
    # 使用示例
    for host in hosts:
        services = identify_services(host["ip"])
        for service in services:
            print(
                f"Host: {host['ip']}, Port: {service['port']}, Service: {service['service']}, Version: {service['version']}"
            )
