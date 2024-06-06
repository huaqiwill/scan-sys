from django.db import models

"""
notes 用户可以编辑

主机发现记录、服务识别记录、端口扫描记录、漏洞检测记录
网页漏洞扫描记录
报告生成记录
修复评估建议管理
"""


class BugLog(models.Model):
    name = models.CharField("漏洞名称", max_length=255)
    type = models.CharField("漏洞类型", max_length=255)
    affected_host = models.CharField("影响主机", max_length=255)
    affected_port = models.IntegerField("影响端口")
    level = models.CharField("漏洞等级", max_length=255)
    discovery_time = models.DateTimeField("发现时间")
    fix_status = models.CharField("修复状态", max_length=255)
    fix_time = models.DateTimeField("修复时间", null=True, blank=True)
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = 'scan_bug_log'


class HostLog(models.Model):
    ip = models.CharField("主机名称", max_length=255)
    mac = models.CharField("主机类型", max_length=255)
    os = models.CharField("操作系统", max_length=255)
    supplier = models.CharField("操作系统", max_length=255)
    start_time = models.DateTimeField("扫描开始时间")
    end_time = models.DateTimeField("扫描结束时间")
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = 'scan_host_log'


class ServiceLog(models.Model):
    """服务识别记录"""
    ip = models.CharField("IP地址", max_length=255)
    port = models.CharField("端口号", max_length=255)
    protocol = models.CharField("协议", max_length=255)
    service = models.CharField("服务名称", max_length=255)
    version = models.CharField("版本", max_length=255)
    state = models.CharField("状态", max_length=255)
    product = models.CharField("产品名称", max_length=255)
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = 'scan_service_log'


class PortLog(models.Model):
    host = models.CharField("目标IP", max_length=255)
    ports = models.TextField("扫描结果", max_length=255)
    start_time = models.DateTimeField("开始时间")
    end_time = models.DateTimeField("结束时间")
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = 'scan_port_log'


class WebBugLog(models.Model):
    class Meta:
        db_table = "scan_web_bug_log"


class ReportLog(models.Model):
    class Meta:
        db_table = "scan_report_log"


class SuggestLog(models.Model):
    class Meta:
        db_table = "scan_suggest_log"
