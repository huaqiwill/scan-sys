from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "scan/scanning/bug-index.html")


def start(request: HttpRequest):
    return render(request, "scan/scanning/bug-index.html")


def add(request: HttpRequest):
    return render(request, "scan/scanning/bug-start.html")
