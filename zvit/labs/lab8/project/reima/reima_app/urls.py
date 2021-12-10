from django.urls import path,include
from .views import ClothesView,MainView

urlpatterns = [
    path('', MainView.as_view(),name='main'),
    path('catalog/', ClothesView.as_view(),name='clothes')
]