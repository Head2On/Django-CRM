from django.db import models

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email= models.CharField(max_length=50)
    phone =models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=100)
    zipcode= models.CharField(max_length=20)
    state = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f'{self.first_name} {self.last_name}')