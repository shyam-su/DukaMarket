from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(ShopBanner)
class ShopBannerAdmin(admin.ModelAdmin):
    list_display=('text','button','image',)
   
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin): 
    list_display = ('name', 'description', 'additional_information', 'price', 'availability', 'sku','discount', 'image','features',)
    list_per_page=10


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(Size)
class SizeAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(Reviews)
class ReviewsAdmin(admin.ModelAdmin):
    list_display=('product','review','name','email','comment',)

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display=('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name',)
    
    
@admin.register(Cart_banner)
class Cart_bannerAdmin(admin.ModelAdmin):
    list_display=('title','Bg_image',)
    
    

@admin.register(CartItem)
class CartItemAdmin(admin.ModelAdmin):
    list_display=('product','quantity','unitprice','total','user','date_added',)
    
@admin.register(Checkout_banner)
class Checkout_bannerAdmin(admin.ModelAdmin):
    list_display=('title','image',)
    
@admin.register(Checkout)
class CheckoutAdmin(admin.ModelAdmin):
    list_display=('user','first_name','last_name','email','address','city','postal_code','phone',)
    
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display=('product','price','quantity','total_price','payment_method','status',)
