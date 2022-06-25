from django.http import HttpResponse
from django.shortcuts import render
from app.models import *
from .forms import *


#-----------------------------------------------HttpResponse--------------------------------------------------------
#return httpresponse 
def app(request):
    return HttpResponse("Welcome to app1")


#------------------------------------------------templates----------------------------------------------------------
#render html templates
def index(request):
    #return HttpResponse("Welcome To Homepage of app")
    #return render(request, 'app_index.html')
    #return render(request, 'app/app_index.html')
    dict = {"app_name":"app2"}       #dictionary
    return render(request, 'app/app_index.html', context=dict)


#######################################################################################################
#if tag
def if_tag(request):
    app_name = 'app'
    app_size = '100%'
    app_created_on = '8-jun-2022'
    app_created_by = 'Shubham'
    dictionary = {'an':app_name, 'az':app_size}
    dictionary2 = {'app_name':'shubham', 'app_size':'stable'}
    return render(request, 'app/app_index.html', context=dictionary2)


######################################################################################################
#forloop tag
def forloop(request):
    student = {"names":['Rahul', 'Shubham', 'Rohit', 'Krishan']}
    return render(request, 'app/app_index.html', context = student)

    stu =  {'stu1':{'name':'shubham', 'roll':'103'},
            'stu2':{'name':'rohit', 'roll':'102'},
            'stu3':{'name':'krishan', 'roll':'101'},
            'stu4':{'name':'golu', 'roll':'104'},
        }
    students = {'student':stu}
    return render(request, 'app/app_index.html', context = students)


#-------------------------------------------------models-------------------------------------------------------
#app/app.html
def show_data(request):
    stud_all = student.objects.all
    stud = student.objects.get(pk=1)
    print(stud)
    return render(request, 'app/app_index.html', {'sti':stud, 'sta':stud_all})   


#-------------------------------------------------form api-------------------------------------------------------
#forms.py
#from .forms import * 
def stu_register(request):
    #fm = student()                                                              #student is an here object
    fm = student(auto_id=True, label_suffix=' ', initial={'name':'shubham'})     #auto_id refers to id , label changes the name, initial value
    fm.order_fields(field_order=['email', 'name'])                               #ordering form fields
    return render(request, 'app/app_index.html', {'from':fm})


############################################################################################
#Field Arguments
