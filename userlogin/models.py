from django.db import models

# Create your models here.
class Details(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField(max_length=100)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=200)

    def __str__(self):
        return self.name