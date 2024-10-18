from django.contrib import admin
from .models import *


@admin.register(Deals)
class DealsAdmin(admin.ModelAdmin):
    list_display=("delas",)
    
@admin.register(Navbar_text)
class Navbar_textAdmin(admin.ModelAdmin):
    list_display=("text",)
    

@admin.register(Slider)
class SliderAdmin(admin.ModelAdmin):
    list_display =('barnd_name','discount','sales','discount_deals','link',)
    
@admin.register(FeaturesArea)
class FeaturesAreaAdmin(admin.ModelAdmin):
    list_display =('icon','title','description',)
    
    
@admin.register(Banner_Top)
class Banner_TopAdmin(admin.ModelAdmin):
    list_display=('deals','discount','quote','link',)
    list_editable=('discount',)
    
@admin.register(Banner_Middle)
class Banner_MiddleAdmin(admin.ModelAdmin):
    list_display=('deals','discount','quote','link',)
    list_editable=('discount',)
    
@admin.register(Banner_Button)
class Banner_ButtonAdmin(admin.ModelAdmin):
    list_display=('title','deals','discount','link',)
    
@admin.register(Banner_Bottom_middle)
class Banner_Bottom_middleAdmin(admin.ModelAdmin):
    list_display=('title','deals','link',)

    
    
@admin.register(Moveing_text)
class Moveing_textAdmin(admin.ModelAdmin):
    list_display=('text1','text2','text3',)
    
@admin.register(Top_deals)
class Top_dealsAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(Top_sell)
class Top_sellAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(Special_offer)
class Special_offerAdmin(admin.ModelAdmin):
    list_display=('name',)
    
@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display=('name','url','icon')
    
@admin.register(CustomerCare)
class CustomerCareAdmin(admin.ModelAdmin):
    list_display=('name','link',)
    
    
@admin.register(CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):
    list_display=('name','link',)
    
    
@admin.register(Myaccount)
class MyaccountAdmin(admin.ModelAdmin):
    list_display=('name','link',)    
    
@admin.register(Quicklinks)
class QuicklinksAdmin(admin.ModelAdmin):
    list_display=('name','link',)    
    
@admin.register(Aboutstore)
class AboutstoreAdmin(admin.ModelAdmin):
    list_display=('descr','icon','number','address',)  
    
@admin.register(Footerlinks)
class FooterlinksAdmin(admin.ModelAdmin):
    list_display=('name','link',)
    
@admin.register(payment_img)
class payment_imgAdmin(admin.ModelAdmin):
    list_display=('image','link',)
    

