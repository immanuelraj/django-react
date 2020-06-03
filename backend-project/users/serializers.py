from rest_framework import serializers
from .models import Customer, Vender
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('__all__')


class VenderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Vender
        fields = ('__all__')


class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ('__all__')