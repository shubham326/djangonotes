from django.contrib import admin
from .models import *

@admin.register(student)
class studentAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'email', 'mobile', 'company_name')