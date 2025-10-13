# KindHeart/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    # path('user/', UserList.as_view(), name='user-list'),
   path('notification/', NotificationView.as_view(), name="notification-view")
]