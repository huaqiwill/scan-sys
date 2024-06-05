import nmap


def get_os_info(ip):
    nm = nmap.PortScanner()
    try:
        nm.scan(ip, arguments='-O')
        if 'osclass' in nm[ip]:
            os_info = nm[ip]['osclass'][0]['osfamily']
        else:
            os_info = "Unknown"
    except Exception as e:
        os_info = str(e)
    return os_info


# 在scan_network函数中添加
# client_info = {
#     "ip": received.psrc,
#     "mac": received.hwsrc,
#     "vendor": get_vendor(received.hwsrc),
#     "os": get_os_info(received.psrc)
# }

print(get_os_info("192.168.2.109"))
