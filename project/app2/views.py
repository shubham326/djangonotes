from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Welcome To Homepage of app2")


def app2(request):
    return HttpResponse("Welcome to app2")
