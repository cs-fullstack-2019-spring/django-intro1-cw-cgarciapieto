"""musicProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('musicApp.urls')),
    # sets path and points to the music app
    path('/music', include('musicApp.urls')),
    path('music/kendricklamar', include('musicApp.urls')),
    path('music/dannybrown', include('musicApp.urls')),
    path('music/chancetherapper', include('musicApp.urls')),
    path('admin/', admin.site.urls),
]
