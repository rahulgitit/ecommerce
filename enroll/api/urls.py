from django.contrib import admin
from django.urls import path,include
from enroll.api.views import UserViewSet, CustomerViewSet
from rest_framework.routers import DefaultRouter





router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'customers', CustomerViewSet, basename='customer')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    
]
