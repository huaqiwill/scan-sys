from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "scan/index.html")


def scan(request: HttpRequest):
    return render(request, "scan/web-scan/bug-scan-index.html")


def scan_add(request: HttpRequest):
    return render(request, "scan/web-scan/bug-scan-add.html")
