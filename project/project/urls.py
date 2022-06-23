from django.contrib import admin
from django.urls import path, include
from app import views                      

urlpatterns = [
    path('admin/', admin.site.urls),
    path('app/', include('app.urls')),
    path('app2/', include('app2.urls')),
    path('', views.index),
]
