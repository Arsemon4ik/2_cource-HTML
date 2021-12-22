from django.contrib.auth.models import User
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView, TemplateView, DetailView
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives  # импортируем класс для создание объекта

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

class EnglishView(TemplateView):
    template_name = 'reima_app/us_main.html'
    context_object_name = 'clothes'

class UkraineView(TemplateView):
    template_name = 'reima_app/ukr_main.html'
    context_object_name = 'clothes'

class DetailClothView(DetailView):
    model = Clothes
    template_name = 'reima_app/detail.html'
    context_object_name = 'cloth'

class ZakazView(ListView):
    model = Clothes
    template_name = 'reima_app/zakaz.html'
    context_object_name = 'clothes'
    queryset = Clothes.objects.all()
    ordering = ['-id']


    def post(self, request, *args, **kwargs):

        user = request.user
        email = request.POST['email']
        id_cloth = request.POST['cloth']
        cloth = Clothes.objects.get(pk=id_cloth)



        html_content = render_to_string(
                'reima_app/email_buyer.html',
                {
                    'cloth': cloth,
                    'user': user,
                }
            )
        msg = EmailMultiAlternatives(
            subject= f'Заказ!',
            from_email= 'arseniy.reima@gmail.com',
            to=[email],
        )
        msg.attach_alternative(html_content, "text/html")  # добавляем html

        msg.send()  # отсылаем

        return redirect('/success/')

class SuccessView(TemplateView):
    template_name = 'reima_app/success.html'
