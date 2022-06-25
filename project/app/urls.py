from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('app1', views.app),
    path('if/', views.if_tag),
    path('forloop/', views.forloop),
    path('show_data/', views.show_data),
    path("register/", views.stu_register),
]