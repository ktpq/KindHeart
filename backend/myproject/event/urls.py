from django.urls import path
from .views import *

urlpatterns = [
    path('event/', EventListView.as_view(), name="event-list"),
    path('event/owner/<int:owner_id>/', EventByOwnerView.as_view(), name="event-owner-list")
]