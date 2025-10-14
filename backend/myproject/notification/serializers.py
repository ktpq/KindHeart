from rest_framework import serializers
from .models import *


class NotificationSerializer(serializers.ModelSerializer):
    created_at_display = serializers.SerializerMethodField()

    class Meta:
        model = Notification
        fields = "__all__"  # หรือ list field แล้วเพิ่ม created_at_display

    def get_created_at_display(self, obj):
        return obj.created_at.strftime("%d/%m/%Y %H:%M")

    

