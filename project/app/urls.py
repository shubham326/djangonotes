from django.contrib import admin
from django.urls import path
from app import views

urlpatterns = [
    path('', views.index),
    path('app1', views.app),
    path('if/', views.if_tag),
    path('forloop/', views.forloop),
    path('get/', views.show_data),                                      #get data
    path('post/', views.post_data),                                     #post data
    path('register/', views.stu_reg_form),                              #student register from
]