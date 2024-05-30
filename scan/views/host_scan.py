from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "scan/index.html")


def check(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-index.html")


def found(request: HttpRequest):
    return render(request, "scan/scanning/host-found-index.html")


def server(request: HttpRequest):
    return render(request, "scan/scanning/service-found-index.html")


def port(request: HttpRequest):
    return render(request, "scan/scanning/port-found-index.html")
