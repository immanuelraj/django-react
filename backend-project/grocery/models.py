from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=50, help_text='Category Name')
    image = models.ImageField(upload_to='categories')

    def __str__(self):
        return self.name

class Product(models.Model):
    name = models.CharField(max_length=50, help_text='Product Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    product_image = models.ImageField(upload_to='products')
    phone_number = PhoneNumberField(null=True, blank=True)
    price = models.DecimalField(max_digits=15, decimal_places=5, help_text='Product Price for 1 liter/Kg')
    discont = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=50, help_text='Shop Name')
    phone_number = PhoneNumberField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='shop_user')
    opening_time = models.DateTimeField()
    closing_time = models.DateTimeField()
    shop_image = models.ImageField(upload_to='shops')
    gstin = models.CharField(max_length=15, null=True, blank=True)
    referral_code = models.CharField(max_length=6, null=True, blank=True)
    pickup = models.BooleanField()
    delivery = models.BooleanField()

    def __str__(self):
        return self.user.username