
from user.models import *
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication

# pyright: reportMissingImports=false
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class NotificationView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        allNoti = Notification.objects.all().order_by('-created_at')
        serializer = NotificationSerializer(allNoti, many=True)
        return Response(serializer.data, status = 200)
    
    def post(self, request):
        if not request.user.is_staff:
            return Response({"คุณไม่ใช่เจ้าหน้าที่"})
        serializer = NotificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
