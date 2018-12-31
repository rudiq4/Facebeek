from django.shortcuts import render, render_to_response
from .models import *


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def catering(request):
    return render(request, 'catering.html')


def tastes(request,):
    template = 'general/templates/catering.html'
    taste_type = Tastes.objects.filter(available=True)
    context = {
        'taste_type': taste_type,
    }
    return render(request, template, context)
