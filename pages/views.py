from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# from django.http import HttpResponse

# Create your views here.

@login_required
def home(request):

    return render(request, 'pages/home.html')


def about(request):

    return render(request, 'pages/about.html')


def contact(request):

    return render(request, 'pages/contact.html')


# def services(request):

#     return render(request, 'pages/services.html')
