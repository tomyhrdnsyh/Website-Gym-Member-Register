from email.policy import default
from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField


# Create your models here.
class Review(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class UserActivated(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(null=True, blank=True, max_length=50)

    def __str__(self) -> str:
        return f"{self.user} - {self.status}"


class MembershipDetail(models.Model):
    member_class = models.CharField(null=True, max_length=254)
    price = models.IntegerField(null=True)

    def __str__(self):
        return self.member_class

    class Meta:
        verbose_name_plural = 'price detail'


class Payment(models.Model):
    id_payment = models.CharField(primary_key=True, max_length=250)
    transaction_time = models.DateTimeField()
    gross_amount = models.IntegerField()
    payment_type = models.CharField(max_length=100, null=True)
    payment_status = models.CharField(max_length=100, null=True)

    def __str__(self) -> str:
        return self.payment_status


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
    member_class = models.ForeignKey(MembershipDetail, on_delete=models.CASCADE, null=True)
    message = models.TextField(null=True)
    payment_status = models.ForeignKey(Payment, on_delete=models.CASCADE, null=True)
    start = models.DateField(null=True)
    end = models.DateField(null=True)
    date = models.DateTimeField(auto_now_add=True)
    active_status = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return self.name


SCHEDULE = (
    ('senin', 'Senin'),
    ('selasa', 'Selasa'),
    ('rabu', 'Rabu'),
    ('kamis', 'Kamis'),
    ('jumat', 'Jumat'),
)


class Instructor(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=250)
    birth = models.CharField(max_length=250)
    phone = models.CharField(max_length=20)
    date = models.DateTimeField(auto_now_add=True)
    schedule = MultiSelectField(max_length=250, choices=SCHEDULE, max_choices=5, default='senin')

    def __str__(self) -> str:
        return self.name
