from django.shortcuts import render,redirect
from .forms import *
from django.core.cache import cache
from django.contrib import messages
from .models import *
from about.models import *

# Create your views here.

def contact_view(request):
    try:
        # Try to get cached data
        catch_data = cache.get('contact_page_data')
        if catch_data:
            context = catch_data
        else:
            bannerarea = BannerArea.objects.all()
            location = Location.objects.all()

            # Create the initial context
            context = {
                'bannerarea': bannerarea,
                'location': location
            }
        
        # Handle the POST request
        if request.method == 'POST':
            form = ContactFormForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect('home:home')
            else:
                print(form.errors)  # Print validation errors to debug
        else:
            form = ContactFormForm()

        # Add the form to the context
        context['form'] = form

        # Cache the context if it was not cached before
        if not catch_data:
            cache.set('contact_page_data', context, 60)

        return render(request, 'contact/contact.html', context)

    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while processing your request. Please try again later.')
        return render(request, 'errors/404.html')






