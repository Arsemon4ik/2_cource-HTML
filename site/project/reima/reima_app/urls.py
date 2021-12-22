from django.urls import path,include
from .views import ClothesView,MainView, UkraineView, EnglishView, DetailClothView,SuccessView, ZakazView

urlpatterns = [
    path('', MainView.as_view(),name='main'),
    path('catalog/', ClothesView.as_view(),name='catalog'),
    path('ukr/',UkraineView.as_view(), name='ukr'),
    path('us/',EnglishView.as_view(), name='us'),
    path('<int:pk>/',DetailClothView.as_view(), name='detail'),
    path('success/', SuccessView.as_view(),name='success'),
    path('zakaz/',ZakazView.as_view(), name='zakaz'),
]