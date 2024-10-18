from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Blog_Banner)
class Blog_BannerAdmin(admin.ModelAdmin):
    list_display=('title','image')
    
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display=('title','author','image','content','category','slug','date','status')
    
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display=('post','name','email','comment','date',)
    
@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display=('name','link')

    
    
@admin.register(Blog_Details_Banner)
class Blog_Details_BannerAdmin(admin.ModelAdmin):
    list_display=('title','image')
    

    
