from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *
from shop.views import *



app_name = 'home'

urlpatterns = [
    path('', home_view, name="home"),      
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

