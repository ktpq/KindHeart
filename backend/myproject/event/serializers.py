from rest_framework import serializers
from .models import *

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class EventSerializer(serializers.ModelSerializer):
    createdBy = serializers.ReadOnlyField(source='createdBy.id')
    category = serializers.PrimaryKeyRelatedField(queryset=Category.objects.all())
    category_name = CategorySerializer(source = 'category', read_only=True)
    
    class Meta:
        model = Event
        fields = "__all__"

class EventEditSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Participation
        fields = '__all__'