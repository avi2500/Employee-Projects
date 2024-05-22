from django.db import models



class Employee(models.Model):
    first_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50,blank=True)
    last_name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')
    designation= models.CharField(max_length=50)
    email_address = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(max_length=12, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self) -> str:
        return f'{self.first_name} and {self.last_name}'

