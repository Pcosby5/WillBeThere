from django.urls import path
from . import views
from .views import HomeListView


urlpatterns = [
    path('', HomeListView.as_view(), name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    # path('services/', views.services, name='services'),

]
