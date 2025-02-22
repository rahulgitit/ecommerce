from django.contrib import admin
from  enroll.models import product,customer,orderplace,cart
# Register your models here.

@admin.register(product)
class productAdmin(admin.ModelAdmin):
    list_display=["id","title","selling_price","discount_price","discriptions","brand","category","product_images"]

@admin.register(customer)
class customerAdmin(admin.ModelAdmin):
    list_display=["id","user","name","phone","email","city","state","pincode"]

@admin.register(orderplace)
class orderplacerAdmin(admin.ModelAdmin):
    list_display=["id","user","customer","product","quantity","order_date","status"]

@admin.register(cart)
class cartAdmin(admin.ModelAdmin):
    list_display=["id","user","product","quantity"]