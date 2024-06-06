from django.db import models

"""
notes 用户可以编辑

主机发现记录、服务识别记录、端口扫描记录、漏洞检测记录
网页漏洞扫描记录
报告生成记录
修复评估建议管理
"""


class Vulnerability(models.Model):
    """漏洞检测记录"""

    name = models.CharField("漏洞名称", max_length=255)
    type = models.CharField("漏洞类型", max_length=255)
    affected_host = models.CharField("影响主机", max_length=255)
    affected_port = models.IntegerField("影响端口")
    level = models.CharField("漏洞等级", max_length=255)
    discovery_time = models.DateTimeField("发现时间")
    fix_status = models.CharField("修复状态", max_length=255)
    fix_time = models.DateTimeField("修复时间", null=True, blank=True)
    notes = models.TextField("备注", blank=True)

    def __str__(self):
        return self.name


class HostLog(models.Model):
    """主机发现记录"""
    ip = models.CharField("主机名称", max_length=255)
    mac = models.CharField("主机类型", max_length=255)
    os = models.CharField("操作系统", max_length=255)
    supplier = models.CharField("操作系统", max_length=255)
    start_time = models.DateTimeField("扫描开始时间")
    end_time = models.DateTimeField("扫描结束时间")
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = 'host_log'


class Service(models.Model):
    """服务识别记录"""
    service_name = models.CharField("服务名称", max_length=255)
    service_type = models.CharField("服务类型", max_length=255)
    port_number = models.IntegerField("端口号")
    protocol_type = models.CharField("协议类型", max_length=255)
    status = models.CharField("运行状态", max_length=255)
    notes = models.TextField("备注", blank=True)

    def __str__(self):
        return self.service_name


class PortScan(models.Model):
    """端口扫描记录"""
    target_ip = models.CharField("目标IP", max_length=255)
    result = models.TextField("扫描结果")
    start_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    status = models.CharField("扫描状态", max_length=255)
    notes = models.TextField("备注", blank=True)

    def __str__(self):
        return self.target_ip
