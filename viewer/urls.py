from django.contrib import admin
from django.urls import path
from . import views
from .views import create_schedule, generate_schedule, schedule_list
from django.urls import path


urlpatterns = [
    path('base/', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('schedule/', views.create_schedule, name='create_schedule', ),
    path('enter_availability/', views.enter_availability, name='enter_availability'),
    path('home/', views.home, name='home'),
    path('', views.root, name='root'),
    path('availability_list', views.availability_list, name='availability_list'),
    path('generate_schedule/', views.generate_schedule, name='generate_schedule'),
    path('schedule_list/', views.schedule_list, name='schedule_list'),


]