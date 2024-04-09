from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from eventsPlanner.models import Event, RSVP
# from django.db.models import Prefetch
from django.contrib.auth.mixins import LoginRequiredMixin
# from django.http import HttpResponse


# Create your views here.


class HomeListView(LoginRequiredMixin, ListView):
    model = Event
    template_name = 'pages/home.html'
    context_object_name = 'upcoming_events'
    ordering = ['date']

    def get_queryset(self):
        return Event.objects.all().order_by('date')


def about(request):

    return render(request, 'pages/about.html')


def contact(request):

    return render(request, 'pages/contact.html')


# def services(request):

#     return render(request, 'pages/services.html')
