# KindHeart/urls.py
from django.urls import path
from .views import *

urlpatterns = [
    path('', UserList.as_view(), name='user-list'),
    path('user/<int:id>/', UserDetail.as_view(), name='user-detail'),
    path('user/change-password/<int:id>/', ChangePasswordView.as_view(), name="change-password")
]