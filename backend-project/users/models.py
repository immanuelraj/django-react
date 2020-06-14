from django.db import models
from grocery import generate
from django.conf import settings
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


class Vender(models.Model):

    STATUS = (
        ('A', 'Approved'),
        ('I', 'In Progress'),
        ('R', 'Rejected'),
    )

    LOCATION = (
        ('B', 'Bangalore'),
        ('C', 'Chennai'),
        ('M', 'Mumbai'),
    )

    MODE = (
        ('P', 'Pickup'),
        ('D', 'Delivery'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, null=True, help_text='Vender Name')
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=280, null=True, help_text='Vender Address')
    Location = models.CharField(max_length=1, null=True, choices=LOCATION,default='B')
    landmark = models.CharField(max_length=80, null=True)
    pincode = models.IntegerField(null=True, blank=True)
    status = models.CharField(max_length=1, null=True, choices=STATUS,default='I')
    shop_image = models.ImageField(upload_to='venders', null=True)
    bank_acc_no = models.IntegerField(null=True, blank=True, help_text='Bank Account Number.')
    ifsc_code = models.CharField(max_length=10, null=True, blank=True)
    document_verification = models.ImageField(upload_to='venders', null=True)
    transport_mode = models.CharField(max_length=1, null=True, choices=STATUS, default='P')
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.user.username

    def check_unique(self, ext_id):
        return not Vender.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Vender, self).save(*args, **kwargs)


class Customer(models.Model):

    LOCATION = (
        ('B', 'Bangalore'),
        ('C', 'Chennai'),
        ('M', 'Mumbai'),
    )

    STATUS = (
        ('A', 'Approved'),
        ('I', 'In Progress'),
        ('R', 'Rejected'),
    )

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=80, help_text='Customer Name')
    phone_number = PhoneNumberField(null=True, blank=True)
    address = models.CharField(max_length=280, help_text='Customer Address')
    Location = models.CharField(max_length=1, choices=LOCATION,default='B')
    landmark = models.CharField(max_length=80)
    status = models.CharField(max_length=1, choices=STATUS,default='I')
    pincode = models.IntegerField(null=True, blank=True)
    staled = models.BooleanField()
    ext_id = models.CharField(max_length=settings.EXT_ID_LENGTH, blank=True)

    def __str__(self):
        return self.user.username

    def check_unique(self, ext_id):
        return not Customer.objects.filter(ext_id=ext_id).exists()

    def save(self, *args, **kwargs):
        if not self.ext_id:
            self.ext_id = generate.generate_unique_ext(
                self, settings.EXT_ID_LENGTH)
        super(Customer, self).save(*args, **kwargs)

