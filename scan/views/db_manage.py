from django.shortcuts import render
from django.http import HttpRequest


# Create your views here.
def index(request: HttpRequest):
    return render(request, "scan/index.html")


def config(request: HttpRequest):
    return render(request, "scan/db/index.html")
