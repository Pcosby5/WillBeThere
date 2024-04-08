from django.urls import path
from .views import AddEventCreateView, AddRSVPCreateView, EventDetailView

urlpatterns = [
    path('add_event/', AddEventCreateView.as_view(), name='add_event'),
    path('add_rsvp/', AddRSVPCreateView.as_view(), name='add_rsvp'),
    path('event/<int:pk>/', EventDetailView.as_view(), name='event_detail'),
]
