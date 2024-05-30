from django.db import models

# Create your models here.


class Vulnerability(models.Model):
    """漏洞"""

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


class Host(models.Model):
    """主机"""

    host_id = models.AutoField(primary_key=True)
    hostname = models.CharField(max_length=255)
    host_type = models.CharField(max_length=255)
    operating_system = models.CharField(max_length=255)
    network_location = models.CharField(max_length=255)
    scan_time = models.DateTimeField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.hostname


class Service(models.Model):
    """服务识别"""

    service_id = models.AutoField(primary_key=True)
    service_name = models.CharField(max_length=255)
    service_type = models.CharField(max_length=255)
    port_number = models.IntegerField()
    protocol_type = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.service_name


class PortScan(models.Model):
    """端口扫描"""

    scan_id = models.AutoField(primary_key=True)
    target_ip = models.CharField(max_length=255)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=255)
    result = models.TextField()
    notes = models.TextField(blank=True)

    def __str__(self):
        return self.target_ip
