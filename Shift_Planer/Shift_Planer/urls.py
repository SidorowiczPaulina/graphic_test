"""
URL configuration for Shift_Planer project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
<<<<<<< HEAD

from django.urls import path
from .views import hello_world
=======
from django.urls import path
>>>>>>> b244cbc6e72005f66f382dab19a60cea2e3dc5ec

urlpatterns = [
    path('admin/', admin.site.urls),
]
<<<<<<< HEAD
urlpatterns = [
    path('hello/', hello_world, name='hello_world'),
]
=======
>>>>>>> b244cbc6e72005f66f382dab19a60cea2e3dc5ec
