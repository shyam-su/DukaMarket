from django.contrib import admin
from .models import *

# Register your models here.
# Register your models here.
admin.site.site_title='DukaMarket '
admin.site.site_header='Welcome Our Duka Market !'
admin.site.index_title='Duka Market Management System'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display=('name','email','address','phone_number','logo',)
    
@admin.register(FooterWidget)
class FooterWidgetAdmin(admin.ModelAdmin):
    list_display=('title','url')

@admin.register(SocialMediaLink)
class SocialMediaLinkAdmin(admin.ModelAdmin):
    list_display=('name','url','icon')
    
@admin.register(CustomerService)
class CustomerServiceAdmin(admin.ModelAdmin):
    list_display=('title','url')
    

    
@admin.register(Download_App)
class Download_AppAdmin(admin.ModelAdmin):
    list_display=('name','image','link',)


    
