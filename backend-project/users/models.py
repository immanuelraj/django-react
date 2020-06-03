from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Vender(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, help_text='Vender Name')
    phone_number = PhoneNumberField(null=True, blank=True)
    staled = models.BooleanField()

    def __str__(self):
        return self.user.username


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, help_text='Customer Name')
    phone_number = PhoneNumberField(null=True, blank=True)
    staled = models.BooleanField()

    def __str__(self):
        return self.user.username

