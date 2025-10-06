from django.shortcuts import render
from user.models import *
from django.http import Http404
from user.serializers import *

# pyright: reportMissingImports=false
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class UserList(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)
