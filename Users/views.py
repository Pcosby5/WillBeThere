from django.contrib import messages
from django.shortcuts import redirect, render
from django.views.generic.edit import FormView
from django.contrib import messages
from .forms import UserRegisterForm
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.contrib.auth import logout
from django.views.decorators.csrf import csrf_exempt
# from django.contrib.auth.views import LogoutView

class CustomLogoutView(View):
    @method_decorator(csrf_exempt)  # Disable CSRF token for demonstration purposes
    def get(self, request):
        logout(request)
        return redirect('login')  # Redirect to a login page or your custom logout page

class UserRegisterView(FormView):
    template_name = 'Users/signup.html'
    form_class = UserRegisterForm
    success_url = '/login/'  # URL to redirect after successful form submission

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        messages.success(self.request, f'Account created for {username}. You can now login!')
        return super().form_valid(form)



# class CustomLogoutView(LogoutView):
#     def dispatch(self, request, *args, **kwargs):
#         # Add custom logic here if needed
#         return super().dispatch(request, *args, **kwargs)

#     def get_next_page(self):
#         # Customize the redirect URL after logout
#         return 'logout'  # Example URL
