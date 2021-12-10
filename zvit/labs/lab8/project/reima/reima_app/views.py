from django.shortcuts import render
from django.views.generic import ListView

from .models import Clothes

# Create your views here.
class ClothesView(ListView):
    model = Clothes
    template_name = 'reima_app/main.html'
    context_object_name = 'clothes'
    queryset = Clothes.objects.all()

class MainView(ListView):
    template_name = 'default.html'
    queryset = Clothes.objects.all()
