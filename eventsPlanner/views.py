from django.views.generic import CreateView, DetailView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import AddEventForm, AddRSVPForm
from .models import Event, RSVP
from django.contrib.auth.models import User

class AddEventCreateView(LoginRequiredMixin, CreateView):
    model = Event
    form_class = AddEventForm
    template_name = 'eventsPlanner/add_events.html'

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.pk})

    def get_form(self, form_class=None):
        form = super().get_form(form_class)
        form.fields['organizer'].queryset = User.objects.filter(is_active=True)
        return form

class AddRSVPCreateView(LoginRequiredMixin, CreateView):
    model = RSVP
    form_class = AddRSVPForm
    template_name = 'eventsPlanner/add_rsvp.html'

    def get_success_url(self):
        return reverse_lazy('event_detail', kwargs={'pk': self.object.event.pk})

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class EventDetailView(LoginRequiredMixin, DetailView):
    model = Event
    template_name = 'eventsPlanner/event_details.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        event = self.get_object()
        r_s_vps = RSVP.objects.filter(event=event, attending=True)

        context['r_s_vps'] = r_s_vps
        context['total_guests'] = r_s_vps.count()
        return context































# from django.views.generic import CreateView, DetailView
# from .models import Event, RSVP
# from django.urls import reverse_lazy
# from django.contrib.auth.mixins import LoginRequiredMixin
# from .forms import AddEventForm, AddRSVPForm
# from django.contrib.auth.models import User

# class AddEventCreateView(LoginRequiredMixin, CreateView):
#     model = Event
#     form_class = AddEventForm
#     # fields = ['organizer', 'name', 'time', 'item', 'date', 'location', 'eventImageUrl']
#     template_name = 'eventsPlanner/add_events.html'
#     success_url = reverse_lazy('event_detail')

#     def get_form(self, form_class=None):
#         form = super().get_form(form_class)
#         form.fields['organizer'].queryset = User.objects.filter(is_active=True)
#         return form

# class AddRSVPCreateView(LoginRequiredMixin, CreateView):
#     model = RSVP
#     form_class = AddRSVPForm
#     # fields = ['organizer', 'name', 'time', 'item', 'date', 'location', 'eventImageUrl']
#     template_name = 'eventsPlanner/add_rsvp.html'
#     success_url = reverse_lazy('event_detail')

#     def form_valid(self, form):
#         form.instance.user = self.request.user
#         return super().form_valid(form)

# class EventDetailView(LoginRequiredMixin, DetailView):
#     model = Event
#     template_name = 'eventsPlanner/event_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)

#         event = self.get_object()
#         rsvps = RSVP.objects.filter(event=event, attending=True)

#         context['rsvps'] = rsvps
#         context['total_guests'] = rsvps.count()
#         return context
