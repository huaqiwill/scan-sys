from mac_vendor_lookup import MacLookup

mac_lookup = MacLookup()
mac_lookup.update_vendors()  # 更新本地供应商数据库


def get_vendor(mac_address):
    try:
        vendor = mac_lookup.lookup(mac_address)
    except KeyError:
        vendor = "Unknown"
    return vendor


# 在scan_network函数中添加
# client_info = {
#     "ip": received.psrc,
#     "mac": received.hwsrc,
#     "vendor": get_vendor(received.hwsrc)
# }

vendor = get_vendor("")
