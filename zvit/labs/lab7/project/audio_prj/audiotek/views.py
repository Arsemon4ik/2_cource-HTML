from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.
from .models import Song

class Audioteka(ListView):
    model = Song
    template_name = 'default.html'
    context_object_name = 'audioteka'

