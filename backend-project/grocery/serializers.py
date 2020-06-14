from rest_framework import serializers
from .models import Category, Product


class CategoryListSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('id', 'name',)


class ProductListSerializer(serializers.ModelSerializer):
    availability = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()


    def get_availability(self, obj):
        return obj.get_availability_display()

    def get_category(self, obj):
        return obj.category.name


    class Meta:
        model = Product
        fields = ('name', 'image', 'category', 'price', 'availability', 'ext_id')


class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('name', 'category', 'image', 'availability', 'price',)