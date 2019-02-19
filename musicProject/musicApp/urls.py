
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('music/kendricklamar', views.kendrick, name='kenny'),
    path('music/dannybrown', views.danny, name='danny'),
    path('music/chancetherapper', views.chance, name='chance'),
]