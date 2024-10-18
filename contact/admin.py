from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(BannerArea)
class BannerAreaAdmin(admin.ModelAdmin):
    list_display=('title','image',)
    
    
@admin.register(ContactForm)
class ContactFormAdmin(admin.ModelAdmin):
    list_display=('name','email','phone','message')
    
    

    

    

    
