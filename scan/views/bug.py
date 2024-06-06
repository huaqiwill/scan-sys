from django.http import HttpRequest
from django.shortcuts import render


def index(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-index.html")


def start(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-index.html")


def add(request: HttpRequest):
    return render(request, "scan/scanning/bug-found-add.html")
