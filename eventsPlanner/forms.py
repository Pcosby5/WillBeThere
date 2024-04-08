from django import forms
from .models import Event, RSVP

class AddEventForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = '__all__'

class AddRSVPForm(forms.ModelForm):
    class Meta():
        model = RSVP
        fields = '__all__'
