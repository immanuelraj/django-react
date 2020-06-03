from rest_framework import serializers
from .models import Category, Product, Shop


class CategoryListSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name

    def get_image(self, obj):
        return obj.image.url

    class Meta:
        model = Category
        fields = ('name', 'image',)


class ProductListSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    product_image = serializers.SerializerMethodField()
    category_id = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    discont = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name

    def get_product_image(self, obj):
        return obj.product_image.url

    def get_category_id(self, obj):
        return obj.category.id

    def get_phone_number(self, obj):
        return obj.phone_number

    def get_price(self, obj):
        return obj.price

    def get_discont(self, obj):
        return obj.discont

    class Meta:
        model = Category
        fields = ('name', 'product_image', 'category_id', 'phone_number', 'price', 'discont')


class ShopListSerializer(serializers.Serializer):
    name = serializers.SerializerMethodField()
    shop_image = serializers.SerializerMethodField()
    user_id = serializers.SerializerMethodField()
    phone_number = serializers.SerializerMethodField()
    gstin = serializers.SerializerMethodField()
    referral_code = serializers.SerializerMethodField()

    def get_name(self, obj):
        return obj.name

    def get_shop_image(self, obj):
        return obj.shop_image.url

    def get_user_id(self, obj):
        return obj.user.id

    def get_phone_number(self, obj):
        return obj.phone_number

    def get_gstin(self, obj):
        return obj.gstin

    def get_referral_code(self, obj):
        return obj.referral_code

    class Meta:
        model = Category
        fields = ('name', 'shop_image', 'user_id', 'phone_number', 'gstin', 'referral_code')


class CategorySerializer(serializers.Serializer):

    class Meta:
        model = Category
        fields = ('__all__')


class ProductSerializer(serializers.Serializer):

    class Meta:
        model = Product
        fields = ('__all__')


class ShopSerializer(serializers.Serializer):

    class Meta:
        model = Shop
        fields = ('__all__')