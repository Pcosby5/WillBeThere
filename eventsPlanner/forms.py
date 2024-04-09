from django import forms
from .models import Event, RSVP

class AddEventForm(forms.ModelForm):
    class Meta():
        model = Event
        fields = '__all__'


    def clean_items(self):
        input_string = self.cleaned_data['items']
        items_list = input_string.split(',')
        items_list = [item.strip() for item in items_list if item.strip()]
        return items_list

class AddRSVPForm(forms.ModelForm):
    class Meta:
        model = RSVP
        fields = '__all__'

    def clean_items(self):
        input_value = self.cleaned_data['items']
        # If input is already a list
        if isinstance(input_value, list):
            items_list = input_value
        else:
            # Assuming the input is a string that needs to be split into a list
            items_list = input_value.split(',')
        items_list = [item.strip() for item in items_list if item.strip()]
        return items_list

    def clean_additionalPeople(self):
        input_value = self.cleaned_data['additionalPeople']
        # Apply similar checking as done for clean_items
        if isinstance(input_value, list):
            additional_people_list = input_value
        else:
            additional_people_list = input_value.split(',')
        additional_people_list = [item.strip() for item in additional_people_list if item.strip()]
        return additional_people_list
