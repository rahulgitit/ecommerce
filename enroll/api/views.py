from django.shortcuts import render
from django.contrib.auth.models import User
from rest_framework import viewsets
from .serializers import UserSerializer, CustomerSerializer, ProductSerializer, CartSerializer, OrderPlaceSerializer
from enroll.models import customer, product, cart, orderplace
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token

class UserViewSet(viewsets.ModelViewSet):
        queryset = User.objects.all()
        serializer = UserSerializer(queryset, many=True)
        
    
class CustomerViewSet(viewsets.ModelViewSet):
        queryset = customer.objects.all()
        serializer_class = CustomerSerializer

class ProductViewSet(viewsets.ModelViewSet):
        queryset = product.objects.all()
        serializer_class = CustomerSerializer

class CartViewSet(viewsets.ModelViewSet):
        queryset = cart.objects.all()
        serializer_class = CartSerializer

class OrderPlaceViewSet(viewsets.ModelViewSet):
        queryset = orderplace.objects.all()
        serializer_class = OrderPlaceSerializer