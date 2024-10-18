from django.shortcuts import render,redirect
from .models import *

def login(request):
    return render(request,'user/login.html')

def success(request):
    return render(request,'user/success.html')

def Profile(request):
    if request.user.is_authenticated:
        # Try to retrieve the user's profile
        try:
            user_profile = UserProfile.objects.get(user=request.user)
        except UserProfile.DoesNotExist:
            # If the profile doesn't exist, create it
            user_profile = UserProfile.objects.create(user=request.user)

        context = {
            'user_profile': user_profile
        }
        return render(request, 'user/profile.html', context)
    else:
        return redirect('login')


