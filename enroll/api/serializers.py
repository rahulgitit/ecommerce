from rest_framework import serializers
from enroll.models import product,cart,customer,orderplace
from django.contrib.auth.models import User
from django.contrib.auth import authenticate


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email','password','Password_confirmation']
        extra_kwargs = {
            'password': {'write_only': True},
            'Password confirmation': {'write_only': True}
        }
        def create(self, validated_data):
            user = User.objects.create_user(**validated_data)
            username = validated_data['username']
            email = validated_data['email']
            password = validated_data['password']
            user.set_password(password)
            user.save() 
            return user
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()
    def validate(self, attrs):
        user = authenticate(**attrs)
        if user and user.is_active:
            return user
        raise serializers.ValidationError("Incorrect Credentials")
    

class CustomerSerializer(serializers.ModelSerializer):
    class Meta:
        model = customer
        fields = ['id', 'user', 'name', 'phone', 'email', 'city', 'state', 'pincode']

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = product
        fields = ['id', 'title', 'selling_price', 'discount_price', 'discriptions', 'brand', 'category', 'product_images']

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = cart
        fields = ['id', 'user', 'product', 'quantity']


class OrderPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = orderplace
        fields = ['id', 'user', 'customer', 'product', 'quantity']