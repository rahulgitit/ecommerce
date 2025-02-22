from django.contrib import admin
from django.urls import path,include
from enroll.api.views import UserViewSet, CustomerViewSet, ProductViewSet, CartViewSet, OrderPlaceViewSet
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'customers', CustomerViewSet, basename='customer')
router.register(r'products', ProductViewSet, basename='product')
router.register(r'carts', CartViewSet, basename='cart')
router.register(r'orderplaces', OrderPlaceViewSet, basename='orderplace')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
