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
    os = models.CharField("操作系统", max_length=255)
    found_by = models.CharField("发现人", max_length=255)
    found_time = models.DateTimeField("发现时间")
    bug_type = models.CharField("漏洞类型", max_length=255)
    bug_name = models.CharField("漏洞名称", max_length=255)
    bug_level = models.CharField("漏洞等级", max_length=255)
    bug_url = models.CharField("漏洞URL", max_length=255)
    bug_status = models.CharField("漏洞状态", max_length=255)
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
    name = models.CharField("漏洞名称", max_length=255)
    os = models.CharField("操作系统", max_length=255)
    found_by = models.CharField("发现人", max_length=255)
    found_time = models.DateTimeField("发现时间")
    bug_type = models.CharField("漏洞类型", max_length=255)
    bug_name = models.CharField("漏洞名称", max_length=255)
    bug_level = models.CharField("漏洞等级", max_length=255)
    bug_url = models.CharField("漏洞URL", max_length=255)
    bug_status = models.CharField("漏洞状态", max_length=255)
    notes = models.TextField("备注", blank=True)

    class Meta:
        db_table = "scan_web_bug_log"


class ReportLog(models.Model):
    name = models.CharField("报告名称", max_length=255)
    url = models.CharField("报告地址", max_length=255)
    create_time = models.DateTimeField("报告生成时间")

    class Meta:
        db_table = "scan_report_log"


class SuggestLog(models.Model):
    name_en = models.TextField("")
    name_cn = models.TextField("")
    risk = models.TextField("")
    describe = models.TextField("")
    solution = models.TextField("")
    cve = models.TextField("")
    is_update = models.IntegerField("")

    class Meta:
        db_table = "scan_suggest_log"
