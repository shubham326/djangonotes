----------------------------------------Github commands-----------------------------------------
    #git
    #POST
    select folder
    git init
    git add .
    git commit -m 'first commit'
    git remote add origin https://github.com/shubham326/djangonotes.git       #project post/upload on github
    git push origin master

    #Update
    git status
    git add .
    git commit -m 'updates'
    *****git remote add origin https://github.com/shubham326/djangonotes.git      #update push on github
    git push -u origin master


    #get 
    git remote -v
    git remote set-url origin
    git remote -v                                                             #get project from github repository
    git pull https://github.com/shubham326/djangonotes.git                  




-------------------------------------------------------------------------------------------------
----------------------------------------Requirements.txt------------------------------------
    #requirements.txt
    pip freeze                                                  #To see all dependencies
    pip freeze > requirments.txt                                #To create requirements.txt
    pip install -r requirements.txt                             #To install requirements.txt




------------------------------------------------------------------------------------------------
----------------------------------------Check Version---------------------------------------------
    #check version
    python --version
    pip --version
    django-admin --version




------------------------------------------------------------------------------------------------
----------------------------------------Quick start---------------------------------------------

    pip install django
    django-admin startproject project_name
    cd project_name
    python manage.py startapp name          ---or    django-admin startapp name
    python manage.py runserver 
    python manage.py runserver 5555         ---custom port 5555
    python manage.py createsuperuser        #To create super user
    cd ..                                   #to come out from project folder 




---------------------------------------------------------------------------------------------------
----------------------------------------setting--------------------------------------------------

    Debug = True    ---should true on developer site while should always false on server/production site
    ALLOWED_HOSTS = []  --- www.example.com




---------------------------------------------------------------------------------------------------
----------------------------------------Default DATABASES-------------------------------------------

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
    #Customize
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            'NAME': "book",
            "user": "-----",
            "password": "-----",
            "HOST": "127.0.0.1",
            "port": "5432",
        }
    }




------------------------------------------------------------------------------------------------------
----------------------------------------ORM Models----------------------------------------------------

    #design of django model and use of query set
    #models.py
    #syntax 
    from django.db import models
    class model_name(models.Model):
        field_name = models.FieldType(arg, options)                             #filed option (primary_key = True)
        name = models.CharField(max_length=50, unique=True, primary_key=True)   #filed argument (max_length = 50)
    #Example
    from django.db import models
    class skill(models.Model):
        stud_id = models.IntegerField()
        name = models.CharField(max_length=50)
        def __str__(self):
            return self.name
        def __str__(self):
            return str(self.stud_id)                                            #to convert int into str



    ############################################################################################
    # specifying choices
    Roles = (
        ("founder", "Founder"),
        ("c", "C Suite"),
        ("business_leader", "Business_leader"),
        ("Manger", "Manager"),
        ("Team_lead", "Team_lead"),
    )


    ############################################################################################
    #custom user model using AbstractUser
    from django.db import models
    from django.contrib.auth.models import AbstractUser
    from .manager import UserManager
    class User(AbstractUser):
        username = None 
        email = models.EmailField(unique=True)
        mobile = models.IntegerField()        
        company_name = models.CharField(max_length=100)                            #in CharFiled length is required
        company_website = models.URLField(max_length=100)
        work_build = models.CharField(max_length=100, choices=work, default='Select')
        role = models.CharField(max_length=50, choices=Roles, default='Find Your Role')
        industry = models.CharField(max_length=100, choices=industry, default='Industry')
        team_member = models.CharField(max_length=50, choices=Employees, default='Find Your Role')

        objects = UserManager()
        USERNAME_FIELD = 'email'
        REQUIRED_FIELDS = []
        def __str__(self):
            return self.username



    ############################################################################################
    #migrations
    #Syntax 
    1. showmigartions :to display status of changes in models
    2. makemigrations :use to convert model class into sql statements and also create a file contains all sql statements(0001),
        located in application.
    3. migrate :to execute sql commands and to create table in database.
    4. sqlmigrate :to display sql statements
    #Example
    1. python manage.py showmigartions
    2. python manage.py makemigrations
    3. python manage.py migrate
    4. python manage.py sqlmigrate app_name migration_filename(0001)
    5.  python manage.py createsuperuser




    ############################################################################################
    #QuerySet
        All objects created in django models
        queryset allow to read the data from the database, filter it and order it.
        user.objects.all()
        users.objects.get(id=9)
        users.objects.get(id=69)
        users.objects.filter(name="shubham")




-------------------------------------------------------------------------------------------------------
----------------------------------------admin.py-------------------------------------------------
    #admin.py 
    #Syntax
    from django.contrib import admin
    from .models import *
    #Syntax
    from django.contrib import admin
    from .models import student
    #admin.site.register(student)
    #OR
    @admin.register(student)
    class studentAdmin(admin.ModelAdmin):
        list_display = ('id','name','email','mobile_no')
    #Example
    from django.contrib import admin
    from .models import *
    @admin.register(skill)
    class skillAdmin(admin.ModelAdmin):
        list_display = ('id','name')
    #Example2
    from .models import candidate, skill
    @admin.register(candidate)
    class candidateAdmin(admin.ModelAdmin):
        list_display = ('id','name','email','mobile_no', 'Role', 'Experience', 'Available', 'get')

        def get(self, obj):
            return "\n".join([p.name for p in obj.skills.all()]) 




-------------------------------------------------------------------------------------------------------
----------------------------------------view.py------------------------------------------------
    #Syntax
    #HttpResponse views.py (static)
    from django.http import HttpResponse
    def function_name(request):
        return HttpResponse("Content")
    #Example
    from django.http import HttpResponse
    def static(request):
        return HttpResponse("Welcome To Homepage")


    ############################################################################################
    #syntax
    #render views.py (dynamic)                                  
    from django.shortcuts import render
    def function_name(request):
        return render(request, template_name, context = dictionary_name, status=None, using=None)
    #Example
    from django.shortcuts import render
    def dynamic(request):
        return render(request, 'app_index.html')
        return render(request, 'app/app_index.html')                    #for specifying the particular app folder 
    #fNote: or every view their should be URL with the name of view


    ############################################################################################
    #sending context=dictionary{"key":"value"}
    dict = {"app_name":"app2"}                                        #dictionary
    return render(request, 'app/app_index.html', context=dict)        #pass 'dict_name' in context
    <h2>The name of app is : {{app_name}}</h2>                        #access by key_name(app_name)

    d = datetime.now()                                                #variable=value
    return render(request, 'app/app_index.html', {'dt':d})            #direct pass key:value
    <h1>{{dt}}</h1>                                                   #then access by key_name {{dt}}
    #OR
    date = {'dt':d}                                                   #make dictionary with value (d = datetime.now())
    return render(request, 'app/app_index.html', date)                #and pass dictionary_name in context/directly
    <h1>{{dt}}</h1>                                                   #then access by key_name {{dt}}
    #Note: pass dictionary_name in context and operate by key_name in html_templates




--------------------------------------------------------------------------------------------------------
----------------------------------------url.py------------------------------------------------

    from django.contrib import admin
    from django.urls import path, include
    #from app import views                          ---so (views.index)
    #from app import views as cv                    ---so (cv.index)
    from app.views import *                         #so we can directly use function
    #Syntax
    urlpatterns = [
        #path(route,view,kwargs=None, name=None),                                #syntax
        #path('home'/, views.function_name, {"check": "ok"}, name="home"),       #example
        #path('home/', views.function_name),
    ]
    #Example
    urlpatterns = [
        path('admin/', admin.site.urls),
        path('', index),
        path('route_name', include(app.urls)),
        path('route_name', include(app2.urls)),
    ]
    #for every URL there should be a view with similar name and also views_function should import from views




------------------------------------------------------------------------------------------------------------
----------------------------------------Templates----------------------------------------------------


    #setting for templates
    TEMPLATE_DIR = BASE_DIR / 'templates'
    STATIC_DIR = BASE_DIR / 'static'

    'BACKEND': 'django.template.backends.django.DjangoTemplates',
            'DIRS': [TEMPLATE_DIR],
            'APP_DIRS': True,


    ############################################################################################
    #templates
    #views.py
    from django.shortcuts import render
    from django.http import HttpResponse
    def index(request):
        #return HttpResponse("Welcome To Homepage of app")
        #return render(request, template_name, context = dictionary_name, status=None, using=None)
        return render(request, 'app_index.html')
        return render(request, 'app/app_index.html')  ----for specifying the particular app folder 




    ############################################################################################
    #Dynamic Template 
    #views.py
    from django.shortcuts import render

        #Syntax
        def index(request):
        #return render(request, template_name, context = dictionary_name, status=None, using=None)
    Note: pass dictionary_name in context and operate by key_name in html_templates

        dict = {"app_name":"app2"}                                       #dictionary
        return render(request, 'app/app_index.html', context=dict)       #pass 'dict' in context which is an dict_name
        <h2>The name of app is : {{app_name}}</h2>                       #access by 'app_name' which is an key_name


        app_name = 'app'
        app_size = '100%'
        app_created_on = '8-jun-2022'
        app_created_by = 'Shubham'                                                              #variables

        dictionary = {'an':app_name, 'as':app_size}                                             #make dictionary for variables
        dictionary2 = {'app_name':'shubham', 'app_size':'stable'}                               #make dictionary for variables

        return render(request, 'app/app_index.html', context=dictionary2)                       #pass dictionary_name in context

        <h2>The name of app is : {{app_name}} and the size is : {{app_size}}</h2>               #finally access by key_name {{app_name}}


        d = datetime.now()                                                #variable=value
        return render(request, 'app/app_index.html', {'dt':d})            #direct pass key:value
        <h1>{{dt}}</h1>                                                   #then access by key_name {{dt}}
        #OR
        date = {'dt':d}                                                   #make dictionary with value (d = datetime.now())
        return render(request, 'app/app_index.html', date)                #and pass dictionary_name in context/directly
        <h1>{{dt}}</h1>                                                   #then access by key_name {{dt}}




    ############################################################################################
    #Filters in django templates language
    Syntax: {{variable|filter}}
    Example: {{app_name|upper}},  {{app_size|int}}
    #types
    {{app_name|upper}},
    {{article|truncateword:40}}   #truncateword means limiting the words
    {{article|upper|truncateword:40}}

    #builtin Filters
    filter...............




    ############################################################################################
    #if tag in Templates    
    #Syntax: 
    {% if condition %}
        ........
    {% endif %}
    #Example:
    {% if nm=django %}
        <h1>Hello {{nm}}</h1>
    {% endif %}
    #Example:
    {% if nm|length>=6 %}
        <h1>Hello {{nm}}</h1>
    {% endif %}
    #Example:
    <!--if tag-->
    {% if app_name or app_created_on %}
        <h1> Here one key exist in dictionary </h1>
    {% endif %}
    {% if app_name and app_size %}
        <h1> Here both keys are available in dictionary </h1>
    {% endif %}



    ############################################################################################
    #for loop in templates
    #Syntax
    {% for variable in variables %}
        {{variable}}
    {% endfor %}
    #Example
    {% for nm in names %}                               <!--here names is a key | and nm is a variable-->
    {{nm}}<br>
    {% endfor %}
    #Example
    {% for variable in variables %}
        {{variable}}
    {% empty %}
        <h1> write anything u want to display on web pages. </h1>
    {% endfor %}
    #Example
    <!--forloop tag-->
        {% for nm in names %}
        {{nm}}
        {% endfor %}
    <!--predefine forloop-->
    {% for nm in names %}
    {{forloop.counter}}{{nm}}<br>
    {% endfor %}
    <!--predefine ForLoop-->
        .......

    <!--ForLoop with advance dictionary data-->
    {% for stu in student %}                            <!--here student is key | and stu is variable-->
    {{stu}}<br>
    {% endfor %}
    {{student}}



    ############################################################################################
    #templates inheritance (base.html)
    #base.html                                   <!--in this we will create block -->
    #Syntax
    {% block block_name %}{% endblock %}
    #Example
    {% block title %}.....{% endblock %}
    {% block title %}other{% endblock %}
    {% block content %}{% endblock %}            <!--it's ur choice that u want to use to any block or not-->
    <!--if u will give a default value to a block so it will reflect automatically | on other hand u can overwrite this-->
    {% block content2 %}if you give default value to a block so,
    it will reflect to the html page on which u will extend it.....{% endblock %}


    #Example
    #home.html
    {% extend base.html %}                                <!--extend the base html-->
    <h1>hello welcome to our website</h1>
    {% block title %}Home{% endblock %}                   <!--Copy the block from base.html which one u want to use-->
    {% block title %}{% block.super%}Home{% endblock %}   <!--{block.super} can be used when u need both the default one or overwrite-->
    {% block content %}{% endblock %}
    {% block content2 %}.....{% endblock %}               <!--it is ur choice to use this block or not-->



    ############################################################################################
    #static files use with templates inheritance (base.html)

    To use static file i django templates u just have to create first static folder in main project root or application 
    and then create the file css , js , images or other as u requires 
    then u have to {% load static %} 
    then <link rel="stylesheet" href="{% static 'css/style.css' %}">
    then u can easily use this in base.html
    if u want a specifying css for application so u have to create a specify static folder in application
    and the a css , js , image files in that static folder
    then link that static folder to the same application html file as then <link rel="stylesheet" href="{% static 'app/css/style.css' %}">
    and then if u want both project and the app css file in the app.html
    so u have to create a block in the base.html 
    as {% block css %}<link rel="stylesheet" href="{% static 'css/style.css' %}">{% endblock %}

    then extend it in app.html and overwrite this 
    {% block css %}
    {% block.super%}                          <!--{block.super} can be used when u need both the default one or overwrite-->
    <link rel="stylesheet" href="{% static 'app/css/style.css' %}">
    {% endblock %}



    ############################################################################################
    #templates inside the app/application 
    #setting for templates inside the app/application 
    TEMPLATE_DIR = BASE_DIR / 'templates'
    STATIC_DIR = BASE_DIR / 'static'

    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'DIRS': [TEMPLATE_DIR],

                'APP_DIRS': True,               <!--only required this should  to be True-->



    ############################################################################################
    #url tag in templates
    .html
    #Syntax
    {% url 'aboutus' %}
    #Example
    <link rel="stylesheet" href="{% url 'aboutus' %}">

    and mention this ulr name in url.py as url_name 
    urlpatterns = [
        #path('home'/, views.function_name, {"check": "ok"}, name="home"),                     <!--Syntax-->
        path('admin/', admin.site.urls),
        path('', index),
        path('route_name', include(app.urls)),
        path('route_name', include(app2.urls)),
        path('about/', views.about, name='aboutus'),                                           <!--#Example-->
    ]



    ############################################################################################
    #include tag in templates
    <!--use to include any template file i.e 'one.html' into another template file "another.html"-->
    #Syntax
    #another.html
    {% include 'one.html' %}
    {% include 'one.html' with p='python' %}




--------------------------------------------------------------------------------------------------------------
----------------------------------------Static Files--------------------------------------------------------

    #setting for static
    TEMPLATE_DIR = BASE_DIR / 'templates'
    STATIC_DIR = BASE_DIR / 'static'

    STATIC_URL = 'static/'
    STATICFILES_DIRS = [STATIC_DIR] 

    #Syntax 
    {% load static %}
    {% static filename %}
    {% static path/filename %}
    {% static path/filename as variable %}
    #Example
    {% load static %}
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
    <img src="{% static 'images/img.jpg' %}" alt="">

    {% static "images/image.jpg" as mylove %}
    <img src="{{mylove}}" alt="">



    ############################################################################################
    #static files use with templates inheritance (base.html)

    To use static file i django templates u just have to create first static folder in main project root or application 
    and then create the file css , js , images or other as u requires 
    then u have to {% load static %} 
    then <link rel="stylesheet" href="{% static 'css/style.css' %}">
    then u can easily use this in base.html
    if u want a specifying css for application so u have to create a specify static folder in application
    and the a css , js , image files in that static folder
    then link that static folder to the same application html file as then <link rel="stylesheet" href="{% static 'app/css/style.css' %}">
    and then if u want both project and the app css file in the app.html
    so u have to create a block in the base.html 
    as {% block css %}<link rel="stylesheet" href="{% static 'css/style.css' %}">{% endblock %}
    then extend it in app.html and overwrite this 
    {% block css %}
    {% block.super%}                          <!--{block.super} can be used when u need both the default one or overwrite-->
    <link rel="stylesheet" href="{% static 'app/css/style.css' %}">
    {% endblock %}



    ############################################################################################
    #statics_files inside the app/application 
    #setting for static
    TEMPLATE_DIR = BASE_DIR / 'templates'
    STATIC_DIR = BASE_DIR / 'static'

                    STATIC_URL = 'static/'              <!--only required this should  to be set as similar as-->
    STATICFILES_DIRS = [STATIC_DIR] 




--------------------------------------------------------------------------------------------------------------
----------------------------------------crud operations-----------------------------------------------

    #GET    (using to show data from database to html page)
    #views.py code                                              
    def show_data(request):
    stud_all = student.objects.all                              #To get all data of model from database
    stud = student.objects.get(pk=1)                            #To get single specific data of model from database
    #print(stud)
    return render(request, 'app/app_index.html', {'sti':stud, 'sta':stud_all}) #sending data to pages in the form of dict.

    #Templates code
    #show all data
        {% if sta %}
            <h1> show all data </h1>
            <table>
                <tr>
                    <th>Id</th>
                    <th>name</th>
                    <th>email</th>
                    <th>mobile</th>
                    <th>company_name</th>
                </tr>
                {% for st in sta %}                              #use of for loop
                <tr>
                    <td>{{st.id}}</td>
                    <td>{{st.name}}</td>
                    <td>{{st.email}}</td>
                    <td>{{st.mobile}}</td>
                    <td>{{st.company_name}}</td>
                </tr>
                {% endfor %}
            </table>
        {% endif %}
    #show single data
        {% if sti %}
            <h1> show single data </h1>
            <table>
                <tr>
                    <th>Id</th>
                    <th>name</th>
                    <th>email</th>
                    <th>mobile</th>
                    <th>company_name</th>
                </tr>
                <tr>
                    <td>{{sti.id}}</td>
                    <td>{{sti.name}}</td>
                    <td>{{sti.email}}</td>
                    <td>{{sti.mobile}}</td>
                    <td>{{sti.company_name}}</td>
                </tr>
            </table>
        {% endif %}



    ############################################################################################
    #POST    (using to post data from html page)
    #views.py                                                   
    def post_data(request):
    if request.method=='POST':                                          #To check method==POST,GET,PATCH,PUT,DELETE
        fm = students(request.POST)                                     #To get form with data
        if fm.is_valid():                                               #To validate data
            print('Success Validation')
            Name = fm.cleaned_data['name']                              #To get cleaned data
            Email = fm.cleaned_data['email']
            print('Name:', Name)
            print('Email:', Email)
        fm = students()
    else:
        fm = students()
    return render(request, 'app/app_index.html', {'from':fm})

    #Templates code
    <form action="" method="POST">
        {% csrf_token %}
        {{from.as_p}}
        <input type="submit" value="Submit">
    </form>





--------------------------------------------------------------------------------------------------------------
----------------------------------------django Form-----------------------------------------------

    #forms.py
    from django import forms
    class student(forms.Form):
        name = forms.CharField(max_length=50)
        email = forms.EmailField()
    #views.py
    from .forms import * 
    def stu_register(request):
    fm = student()                                                              #here student() is an object
    fm = student(
                auto_id=True,                                                   #auto_id changes id=filed_name
                label_suffix=' ',                                               #label_suffix changes the ':'
                initial={'name':'shubham'}                                      #initial value gives filed a initial value
            )
    fm.order_fields(field_order=['email', 'name'])                              #ordering form fields
    return render(request, app/app_index.html, {'from':fm})
    #templates
    #{{from}}
        <form action="">
            <table>
                {{from}}
            </table>
            <input type="submit" value="Submit">
        </form>



    ############################################################################################
    #Field Arguments
    #forms.py
    from django import forms
    class student(forms.Form):
        name = forms.CharField(
                                max_length=50, 
                                label='Your Name',
                                label_suffix=' ',
                                required=False,
                                disabled=True,
                                help_text='limit 70 char',
                                )
        email = forms.EmailField()


    ############################################################################################
    #Field Widgets
    #manly uses for CSS
    #forms.py
    name = forms.CharField(
                            max_length=50, 
                            label='Your Name',
                            #widget=forms.PasswordInput(),
                            #widget=forms.HiddenInput(),
                            #widget=forms.Textarea(),
                            #widget=forms.CheckboxInput(),
                            #widget=forms.FileInput(),
                            widget=forms.TextInput(attrs={'class':'css1', 'id':'unique_id'}),
                            )
    email = forms.EmailField()




--------------------------------------------------------------------------------------------------------------
----------------------------------------Cookies and Caches--------------------------------------------------

    #cache
        it stores on client side or user side .
        stores : logo, images, videos, big data files.

    #cookies 
        it stores on server side or third party database . 
        stores : identity, login info, cart info, address info, ip info, location, add_info, tracking info etc. 




--------------------------------------------------------------------------------------------------------------
----------------------------------------ManytoMany Relation--------------------------------------------

    #for choosing multiple option at a time          <!--multiple skills for user-->
    #manytomany relation model-settings 
        from django.db import models
        class skill(models.Model):
            name = models.CharField(max_length=50)

            def __str__(self):
                return self.name

        class candidate(models.Model):
        email = models.EmailField(max_length=70, unique=True)
        skills = models.ManyToManyField(skill, blank=True)

            def __str__(self):
                return self.name


    ############################################################################################
    #manytomany_admin.py 
        from django.contrib import admin
        from .models import candidate, skill
        @admin.register(skill)
        class skillAdmin(admin.ModelAdmin):
            list_display = ('id','name')

        @admin.register(candidate)
        class candidateAdmin(admin.ModelAdmin):
            list_display = ('id','name','email','mobile_no', 'Role', 'Experience', 'Available', 'get')

            def get(self, obj):
                return "\n".join([p.name for p in obj.skills.all()]) 
        <!--Here {name = name of using primary-model CharField} and {obj.skills.all = field name of ManytoMany }-->
