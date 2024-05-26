from django import forms
from .models import Notify, SubEmail


class NotifyForm(forms.ModelForm):
    class Meta:
        model = Notify
        fields = [
            "notify_type",
            "notify_mail",
            "notify_subject",
            "notify_content",
            "notify_time",
            "notify_status",
        ]


class SubEmailForm(forms.ModelForm):
    class Meta:
        model = SubEmail
        fields = [
            "sub_email",
            "sub_status",
            "sub_name",
        ]
