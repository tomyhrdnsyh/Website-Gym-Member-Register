from email.policy import default
from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Membership(models.Model):
    user_account = models.ForeignKey(User, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    birthplace = models.CharField(null=True, max_length=100)
    birthdate = models.DateField(null=True)
    address = models.CharField(null=True, max_length=200)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    program = models.CharField(null=True, max_length=100)
    disability_disease = models.CharField(null=True, max_length=100)
    gym_information = models.CharField(null=True, max_length=100)
    member_class = models.CharField(null=True, max_length=254)
    message = models.TextField()
    payment_status = models.BooleanField(default=False)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    birth = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
