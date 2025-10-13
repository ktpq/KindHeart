from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.response import Response
from rest_framework import status, permissions, parsers
from django.core.exceptions import ObjectDoesNotExist
from .serializers import *
from user.models import *
from .models import *
# Create your views here.

import random, string

class EventListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # แสดง event ทั้งหมด
    def get(self, request):
        events = Event.objects.all()
        serializer = EventSerializer(events, many=True)
        return Response(serializer.data, status=200)

    def post(self, request):
        print("Files", request.FILES)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createdBy = request.user)
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
    
class EventByOwnerView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, owner_id):
        if request.user.id != owner_id:
            return Response({"คุณไม่ใช่เจ้าของ"}, status=404)
        try:
            events = Event.objects.filter(createdBy_id = owner_id)
            serializer = EventSerializer(events, many= True)
            return Response(serializer.data, status = 200)
        except ObjectDoesNotExist:
            return Response({"detail: No events found"}, status=404)
        
class EventById(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, id):
        try:
            event = Event.objects.get(id = id)
            serializer = EventSerializer(event)
            return Response(serializer.data, status = 200)
        except ObjectDoesNotExist:
            return Response({"detail: No events found"}, status=404)
    def put(self, request, id):
        try:
            event = Event.objects.get(id = id)
            serializer = EventSerializer(instance = event, data = request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status = 200)
            return Response(serializer.errors, status=400)
        except ObjectDoesNotExist:
            return Response({"detail: No events found"}, status=404)
        
class EventUserCanJoin(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        events_not_joined = Event.objects.exclude(id__in=Participation.objects.filter(user=user).values_list('event_id', flat=True)
)
        

class ParticipationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # join participation
    def post(self, request):
        serializer = ParticipationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
