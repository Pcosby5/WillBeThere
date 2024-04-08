from django.views.generic import CreateView, DetailView
from .models import Event, RSVP
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddEventForm, AddRSVPForm

class AddEventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = AddEventForm
    # fields = ['organizer', 'name', 'time', 'item', 'date', 'location', 'eventImageUrl']
    template_name = 'eventsPlanner/add_events.html'
    success_url = reverse_lazy('event_detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class AddRSVPCreateView(LoginRequiredMixin, CreateView):
    model = RSVP
    form_class = AddRSVPForm
    # fields = ['organizer', 'name', 'time', 'item', 'date', 'location', 'eventImageUrl']
    template_name = 'eventsPlanner/add_rsvp.html'
    success_url = reverse_lazy('event_detail')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'eventsPlanner/event_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = self.get_object()
        rsvps = RSVP.objects.filter(event=event, attending=True)

        context['rsvps'] = rsvps
        context['total_guests'] = rsvps.count()
        return context
