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

class EventListView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    parser_classes = [parsers.MultiPartParser, parsers.FormParser]

    def post(self, request):
        print("Files", request.FILES)
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(createdBy = request.user)
            return Response(serializer.data, status=201)
        print(serializer.errors)
        return Response(serializer.errors, status=400)
    
class EventByOwnerView(APIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]

    def get(self, request, owner_id):
        try:
            events = Event.objects.filter(createdBy_id = owner_id)
            serializer = EventSerializer(events, many= True)
            return Response(serializer.data, status = 200)
        except ObjectDoesNotExist:
            return Response({"detail: No events found"}, status=404)
        
        