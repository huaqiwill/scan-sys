from django.shortcuts import render
from .utils.mail import EMail


# Create your views here.
def monitor(request):
    return render(request, "monitor/monitor.html")


def notify(request):
    EMail().send_email()
    return render(request, "monitor/notify.html")


def handle(request):
    return render(request, "monitor/handle.html")


def recover(request):
    return render(request, "monitor/recover.html")
