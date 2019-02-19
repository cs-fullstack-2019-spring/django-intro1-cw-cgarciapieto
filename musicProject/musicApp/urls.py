
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('kendricklamar', views.kendrick, name='kenny'),
    path('dannybrown', views.danny, name='danny'),
    path('chancetherapper', views.chance, name='chance'),
]