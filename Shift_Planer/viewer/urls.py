from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('base/', views.base, name='base'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name='logout'),
    path('create_schedule/', views.create_schedule, name='create_schedule'),
    path('user_availability/', views.enter_availability, name='availability'),
]