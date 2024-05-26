from rest_framework import serializers
from ..models import Monitor, Notify, SubEmail


class MonitorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        # exclude = ['is_delete', 'create_time']
        fields = "__all__"
        depth = 1


class NotifySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monitor
        # exclude = ['is_delete', 'create_time']
        fields = "__all__"
        depth = 1


class SubEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubEmail
        # exclude = ['is_delete', 'create_time']
        fields = "__all__"
        depth = 1
