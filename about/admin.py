from django.contrib import admin
from .models import *
# Register your models here.
@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display=('title','description','button_link',)
    
@admin.register(AboutSection)
class AboutSectionAdmin(admin.ModelAdmin):
    list_display=('title','description',)
    search_fields = ('title', )
    list_filter = ('title',)
    ordering = ('title',)

    
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display=('title','description','icon_class','step_number')
    
@admin.register(TechnologyIndex)
class TechnologyIndexAdmin(admin.ModelAdmin):
    list_display=('title','description','active_clients','projects_done','team_advisors','users_online',)
    
@admin.register(TeamMember)
class TeamMemberAdmin(admin.ModelAdmin):
    list_display=('title','name','position','facebook','twitter','dribbble','youtube','descr',)
    
@admin.register(Location)
class LocationAdmin(admin.ModelAdmin):
    list_display=('title','address','city','country','map_link','phone','email','descr',)
    list_editable=('descr',)
    