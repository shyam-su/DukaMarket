from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required



def login(request):
    return render(request,'user/login.html')

@login_required
def Profile(request):
    
    if request.user.is_authenticated:
        user_profile = request.user
        print(user_profile.first_name)

        context = {
            'user_profile': user_profile
        }
        return render(request, 'user/profile.html', context)
    else:
        return redirect('login')
    
@login_required
def update_profile(request):
    user = request.user  # This is now an instance of CustomUser 
    if request.method == 'POST':
        form = CustomUserForm(request.POST, request.FILES, instance=user)
        if form.is_valid():
            form.save()
            return redirect('profile')  # Redirect to a profile view or wherever you prefer
    else:
        form = CustomUserForm(instance=user)

    return render(request, 'user/update_profile.html', {'form': form})


def logout(request):
    pass


