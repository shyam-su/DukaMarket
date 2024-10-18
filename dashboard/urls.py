from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import *




app_name = 'dashboard'

urlpatterns = [

    path('', dashboard, name='dashboard'),
    
    path('slider/', Slider_view, name='slider'), 
    path('slider/create/', add_slider, name='add_slider'),
    path('slider/edit/<int:id>/', edit_slider, name='edit_slider'),
    path('slider/delete/<int:id>/', delete_slider, name='delete_slider'),
        
    path('feature/', feature_view, name='feature'),
    path('feature/create/', create_feature, name='create_feature'),
    path('feature/edit/<int:id>/', edit_feature, name='edit_feature'),
    path('feature/delete/<int:id>/', delete_feature, name='delete_feature'), 
      
    path('topbanner/', TopBanner_view, name='topbanner'),
    path('topbanner/create/', TopBanner_create, name='create_topbanner'),
    path('topbanner/edit/<int:id>/', TopBanner_edit, name='edit_topbanner'),
    path('topbanner/delete/<int:id>/', TopBanner_delete, name='delete_topbanner'),
    
    path('topdeals/', Top_Deals_view, name='topdeals'),
    path('topdeals/create/', Top_Deals_create, name='create_topdeals'),
    path('topdeals/edit/<int:id>/', Top_Deals_edit, name='edit_topdeals'),
    path('topdeals/delete/<int:id>/', Top_Deals_delete, name='delete_topdeals'),
    
    path('bannermidle/', Banner_Midle_view, name='bannermidle'),
    path('bannermidle/create/', Banner_Midle_create, name='create_bannermidle'),
    path('bannermidle/edit/<int:id>/', Banner_Midle_edit, name='edit_bannermidle'),
    path('bannermidle/delete/<int:id>/', Banner_Midle_delete, name='delete_bannermidle'),
    
    path('topsells/', Top_Sells_view, name='topsells'),
    path('topsells/create/', Top_Sells_create, name='create_topsells'),
    path('topsells/edit/<int:id>/', Top_Sells_edit, name='edit_topsells'),
    path('topsells/delete/<int:id>/', Top_Sells_delete, name='delete_topsells'),
    
    path('specialoffers/', Special_Offers_view, name='specialoffers'),
    path('specialoffers/create/', Special_Offers_create, name='create_specialoffers'),
    path('specialoffers/edit/<int:id>/', Special_Offers_edit, name='edit_specialoffers'),
    path('specialoffers/delete/<int:id>/', Special_Offers_delete, name='delete_specialoffers'),
    
    path('moveingtexts/', Moveing_Texts_view, name='moveingtexts'),
    path('moveingtexts/create/', Moveing_Texts_create, name='create_moveingtexts'),
    path('moveingtexts/edit/<int:id>/', Moveing_Texts_edit, name='edit_moveingtexts'),
    path('moveingtexts/delete/<int:id>/', Moveing_Texts_delete, name='delete_moveingtexts'),
    
    path('brand/', Brand_view, name='brand'),
    path('brand/create/', Brand_create, name='create_brand'),
    path('brand/edit/<int:id>/', Brand_edit, name='edit_brand'),
    path('brand/delete/<int:id>/', Brand_delete, name='delete_brand'),
    
    
    path('dash_category/', Dash_category, name='dash_category'),
    # path('dash_category/brand/create/', Dash_category_create, name='createdash_category'),
    # path('dash_category/edit/<int:id>/', Dash_category_edit, name='editdash_category'),
    path('dash_category/delete/<int:id>/', Dash_category_delete, name='deletedash_category'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
