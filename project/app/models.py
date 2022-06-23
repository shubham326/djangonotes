from django.db import models

class student(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    mobile = models.IntegerField()        
    company_name = models.CharField(max_length=100) 

    def __str__(self):
        return self.name
