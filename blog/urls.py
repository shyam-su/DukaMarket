from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


app_name = 'blog'

urlpatterns = [
    path('', blog_view, name="blog"),
    path('blog_detail/<slug:slug>/', blog_detail, name="blog_detail"),
    path("<slug:slug>/add_comment/", add_comment, name="add_comment"),

]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)