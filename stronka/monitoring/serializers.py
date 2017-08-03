from rest_framework import serializers


class Ping_historySerializer(serializers.Serializer):
    device_id = serializers.IntegerField(read_only=True)
    avg = serializers.CharField(required=False, allow_blank=True, max_length=100)
    date = serializers.CharField(required=False, allow_blank=True, max_length=100)
