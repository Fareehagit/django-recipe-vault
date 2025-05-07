from django.db import models

# Create your models here.
class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField() 
    email = models.EmailField(null=True)
    address = models.TextField(null=True, blank=True)


class Car(models.Model):
    car_name = models.CharField(max_length=500)
    speed = models.IntegerField(default=50)

    def __str__(self) -> str:
        return f" {self.car_name} - {self.speed}"

    

