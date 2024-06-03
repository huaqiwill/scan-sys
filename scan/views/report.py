from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "scan/report/report-index.html")


def add(request: HttpRequest):
    return render(request, "scan/report/report-add.html")
