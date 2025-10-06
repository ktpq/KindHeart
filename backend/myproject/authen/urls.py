# KindHeart/urls.py
from django.urls import path
from .views import *

# อย่าลืม appended slash (/) ท้าย path เสมอ
urlpatterns = [
    path('login/', Login.as_view(), name='login'),
    path('register/', Register.as_view(), name='register'),
]