from django.contrib import messages
# from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import UserRegisterForm

class UserRegisterView(FormView):
    template_name = 'Users/signup.html'
    form_class = UserRegisterForm
    success_url = '/login/'  # URL to redirect after successful form submission

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}. You can now login!')
        return super().form_valid(form)

