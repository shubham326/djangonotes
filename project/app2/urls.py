from django.contrib import admin
from django.urls import path
from app2 import views

urlpatterns = [
    path('', views.index),
    path('app2', views.app2),
]