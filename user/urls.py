from django.urls import path,include
from .views import *

urlpatterns = [
    
    path("",include('allauth.urls')),#http://127.0.0.1:8000/accounts/profile/ final secuss urls
    # path('login/', login, name='login'),
    # path('signup/', user_signup, name='signup'),
    path('profile/', Profile, name="profile"),
    path('profile/update/', update_profile, name='update_profile'),
    path('logout/', logout, name='logout'),
]
