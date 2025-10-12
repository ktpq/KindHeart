from django.shortcuts import render
from user.models import *
from django.http import Http404
from .serializers import UserSerializer, ChangePasswordSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

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

class UserDetail(APIView):
    def get(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user)
        return Response(serializer.data)
    
    def put(self, request, id):
        user = User.objects.get(id=id)
        serializer = UserSerializer(user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    



class ChangePasswordView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def put(self, request, id):

        if request.user.id != id:
            return Response("คุณไม่ใช่เจ้าของบัญชีนี้")
        
        user = User.objects.get(id=id)
        serializer = ChangePasswordSerializer(instance = user, data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Change Password success", status=200)
        return Response(serializer.errors, status=400)

