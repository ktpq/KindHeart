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

from datetime import datetime
# Create your views here.

import random, string


class EventListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    # แสดง event ทั้งหมด
    def get(self, request):
        now = datetime.now()
        if not request.user.is_staff:
            return Response({"คุณไม่ใช่เจ้าหน้าที่"})
        events = Event.objects.all()
        events_thismonth = Event.objects.filter(start_time__year= now.year, start_time__month = now.month).order_by('-start_time')
        serializer = EventSerializer(events, many=True)
        return Response({"events": serializer.data, "event_count": events.count(), "event_thismonth_count": events_thismonth.count()}, status=200)

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
        user = request.user
        if request.user.id != owner_id and not user.is_staff:
            return Response({"คุณไม่ใช่เจ้าของ"}, status=404)
        try:
            events = Event.objects.filter(createdBy_id = owner_id).order_by('start_time')
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
        
    def delete(self, request, id):
        try:
            if (request.user.is_staff):
                event = Event.objects.get(id = id)
                event.delete()
                return Response({"detail : delete event successfully"}, status=200)
            return Response({"คุณไม่ใช่ admin"}, status=203)
        except ObjectDoesNotExist:
            return Response({"detail: No events found"}, status=404)
        
class EventUserCanJoin(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self, request):
        user = request.user
        events_not_joined = Event.objects.exclude(
            id__in=Participation.objects.filter(user=user).values_list('event_id', flat=True)
        ).exclude(createdBy=user).order_by('start_time')
            
        serializer = EventSerializer(events_not_joined, many=True)
        return Response(serializer.data, status=200)
    

class ParticipationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # get event ที่ฉันเข้าร่วมเเล้ว
    def get(self, request):
        events = Participation.objects.filter(user = request.user).order_by('-event__end_time', '-event__start_time')
        serializer = MyParticipationSerializer(events, many=True)
        return Response(serializer.data, status=200)

    # join participation
    def post(self, request):
        serializer = ParticipationSerializer(data=request.data)
        
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
class ParticipationEvent(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    # เอาไว้ get user ใน event ต่า่งๆ
    def get(self, request, event_id):
        users = Participation.objects.filter(event_id = event_id)
        serializer = MyParticipationSerializer(users, many=True)
        return Response(serializer.data, status=200)
    
    # เอาไว้เช็คชื่อ user
    def put(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
        except Event.DoesNotExist:
            return Response({"detail": "ไม่พบอีเว้นต์นี้"}, status=404)

        # ตรวจสอบว่า user เป็นเจ้าของ event หรือไม่
        if request.user.id != event.createdBy_id:
            return Response({"detail": "คุณไม่ใช่เจ้าของอีเว้นนี้"}, status=403)

        ticket_code = request.data.get("ticket_code")
        if not ticket_code:
            return Response({"detail": "ต้องระบุ ticket_code"}, status=400)

        try:
            thisPerson = Participation.objects.get(ticket_code=ticket_code, event_id=event.id)
        except Participation.DoesNotExist:
            return Response({"detail": "ไม่พบผู้เข้าร่วมที่มี ticket_code นี้"}, status=404)

        # toggle attended
        if not thisPerson.attended:
            thisPerson.attended = True
            thisPerson.save()

        serializer = MyParticipationSerializer(thisPerson)
        return Response(serializer.data, status=200)

