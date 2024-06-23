"""
漏洞检测
"""

import requests
from bs4 import BeautifulSoup


def detect_xss(url):
    payload = "<script>alert('XSS')</script>"
    response = requests.get(url + payload)
    if payload in response.text:
        return True
    return False


def detect_sql_injection(url):
    payload = "' OR '1'='1"
    response = requests.get(url + payload)
    if "syntax error" in response.text or "mysql" in response.text:
        return True
    return False


def start_bug_scan():
    pass


def stop_bug_scan():
    pass


if __name__ == "__main__":
    # 使用示例
    test_url = "http://example.com/vulnerable_page.php?param="
    if detect_xss(test_url):
        print("XSS vulnerability detected!")
    if detect_sql_injection(test_url):
        print("SQL Injection vulnerability detected!")
