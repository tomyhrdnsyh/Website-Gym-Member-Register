from django.db import models


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    name = models.CharField(max_length=100)
    birthplace = models.CharField(null=True, max_length=100)
    birthdate = models.DateField(null=True)
    address = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    program = models.CharField(null=True, max_length=100)
    disability_disease = models.CharField(null=True, max_length=100)
    gym_information = models.CharField(null=True, max_length=100)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
