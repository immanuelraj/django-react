from django.db import models
from django.conf import settings
from .generate import generate_unique_ext
from django.contrib.auth.models import User
from users.models import Customer, Vender
from phonenumber_field.modelfields import PhoneNumberField


class Category(models.Model):
    name = models.CharField(max_length=50, help_text='Category Name')
    image = models.ImageField(upload_to='categories')
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.name

    def check_unique(self, ext_id):
        return not Category.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Category, self).save(*args, **kwargs)

class Product(models.Model):

    MODE = (
        ('A', 'Available'),
        ('N', 'Not Available'),
    )

    name = models.CharField(max_length=50, help_text='Product Name')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product_category')
    image = models.ImageField(upload_to='products')
    availability = models.CharField(max_length=1, choices=MODE,default='A')
    price = models.DecimalField(max_digits=15, decimal_places=5, help_text='Product Price for per unit')
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.name

    def check_unique(self, ext_id):
        return not Product.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Product, self).save(*args, **kwargs)


class OrderedProduct(models.Model):

    MODE = (
        ('A', 'Available'),
        ('N', 'Not Available'),
    )

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='order_summary_customer')
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE, related_name='order_summary_vender')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='ordered_product_product')
    quantity = models.IntegerField(null=True, blank=True)
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.name

    def check_unique(self, ext_id):
        return not Product.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Product, self).save(*args, **kwargs)


class OrderSummary(models.Model):

    MODE = (
        ('P', 'Pickup'),
        ('D', 'Delivery'),
    )

    name = models.CharField(max_length=50, help_text='Product Name')
    ordered_item = models.ManyToManyField(OrderedProduct, blank=True, related_name='ordered_items')
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, related_name='OrderSummary_customer')
    vender = models.ForeignKey(Vender, on_delete=models.CASCADE, related_name='OrderSummary_customer')
    status = models.CharField(max_length=1, choices=MODE)
    transport_mode = models.CharField(max_length=1, choices=MODE)
    total_price = models.DecimalField(max_digits=15, decimal_places=5, help_text='Product Price for per unit')
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.name

    def check_unique(self, ext_id):
        return not Product.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Product, self).save(*args, **kwargs)