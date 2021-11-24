from django.urls import path
from .views import Audioteka

urlpatterns = [
    path('', Audioteka.as_view(), name='default')
]