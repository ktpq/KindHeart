from rest_framework import serializers
from .models import *
from user.serializers import *
import random, string

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    createdBy = serializers.ReadOnlyField(source='createdBy.id')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = CategorySerializer(source='category', read_only=True)
    created_by = UserSerializer(source="createdBy", read_only=True)

    # ฟิลด์ใหม่สำหรับวันที่และเวลาที่อ่านง่าย
    start_date = serializers.SerializerMethodField()
    start_datetime = serializers.SerializerMethodField()
    end_datetime = serializers.SerializerMethodField()

    class Meta:
        model = Event
        fields = "__all__"

    def get_start_date(self, obj):
        return obj.start_time.strftime("%d/%m/%Y")  # วัน/เดือน/ปี

    def get_start_datetime(self, obj):
        return obj.start_time.strftime("%d/%m/%Y %H:%M")  # วัน/เดือน/ปี + เวลา

    def get_end_datetime(self, obj):
        return obj.end_time.strftime("%d/%m/%Y %H:%M")  # วัน/เดือน/ปี + เวลา


class EventEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"



class ParticipationSerializer(serializers.ModelSerializer):
    ticket_code = serializers.CharField(read_only=True)
    user = UserSerializer(read_only=True)

    class Meta:
        model = Participation
        fields = ['event', 'ticket_code', 'user']

    def generate_ticket_code(self, length=10):
        characters = string.ascii_uppercase + string.digits
        return ''.join(random.choices(characters, k=length))
    

    # use join participation
    def create(self, validated_data):
        validated_data['ticket_code'] = self.generate_ticket_code()
        participation = super().create(validated_data)

        # เพิ่ม now_capacity ของ event
        event = participation.event
        event.now_capacity += 1
        event.save()

        return participation
    
    
class MyParticipationSerializer(serializers.ModelSerializer):
    event = EventSerializer(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Participation
        fields = "__all__"