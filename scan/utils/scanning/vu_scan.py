from zapv2 import ZAPv2
import time

# 配置ZAP代理的地址和端口
zap = ZAPv2(proxies={'http': 'http://localhost:8001', 'https': 'http://localhost:8001'})

target = 'http://127.0.0.1:8001/'  # 要扫描的目标URL

# 开始扫描目标
print('Accessing target {}'.format(target))
zap.urlopen(target)
time.sleep(2)  # 等待目标响应

print('Spidering target {}'.format(target))
zap.spider.scan(target)
time.sleep(2)

while (int(zap.spider.status()) < 100):
    print('Spider progress %: {}'.format(zap.spider.status()))
    time.sleep(2)

print('Spider completed')
time.sleep(5)

print('Scanning target {}'.format(target))
zap.ascan.scan(target)
while (int(zap.ascan.status()) < 100):
    print('Scan progress %: {}'.format(zap.ascan.status()))
    time.sleep(5)

print('Scan completed')

# 打印发现的漏洞
alerts = zap.core.alerts()
for alert in alerts:
    print('Alert: {}'.format(alert))
