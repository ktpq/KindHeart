from django.urls import path
from .views import *

urlpatterns = [
    path('event/', EventListView.as_view(), name="event-list"),
    path('event/owner/<int:owner_id>/', EventByOwnerView.as_view(), name="event-owner-list"),
    path('event/<int:id>/', EventById.as_view(), name="event-by-id"),
    path('participation/', ParticipationView.as_view(), name="participation-view")
]