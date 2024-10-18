from django.shortcuts import render,redirect,get_object_or_404
from django.contrib import messages
from django.core.cache import cache
from .models import *
from shop.models import *



def home_view(request):
    try:
        catch_data =cache.get('home_page_data')
        if catch_data:
            context = catch_data
        else:
            category=Category.objects.all()
            sliders = Slider.objects.all()
            featuresarea = FeaturesArea.objects.all()
            banner_top=Banner_Top.objects.all()
            banner_middle=Banner_Middle.objects.all()
            moveing_text=Moveing_text.objects.all()
            banner_button=Banner_Button.objects.all()
            bannerbottommiddle=Banner_Bottom_middle.objects.all()
            brand=Brand.objects.all()
            deals=Top_deals.objects.all()
            topsell=Top_sell.objects.all()
            specialoffer=Special_offer.objects.all()
            category=Category.objects.all()

            

            context = {
                'category': category,
                'sliders': sliders,
                'featuresarea': featuresarea,
                'banner_top': banner_top,
                'banner_middle': banner_middle,
                'moveing_text': moveing_text,
                'banner_button': banner_button,
                'bannerbottommiddle': bannerbottommiddle,
                'brand': brand,
                'deals': deals,
                'topsell': topsell,
                'category': category,
                'specialoffer': specialoffer,

            }
            cache.set('home_page_data', context, 3600)
        return render(request, 'home/home.html', context)
        
    
    except Exception as e:
        print(f"An error occurred: {e}")
        messages.error('An error occurred while loading the Home page. Please try again later.')
        return render(request, 'errors/404.html')
    
    
# def home_view(request): 
#     category=Category.objects.all()
#     sliders = Slider.objects.all()
#     featuresarea = FeaturesArea.objects.all()
#     banner_top=Banner_Top.objects.all()
#     banner_middle=Banner_Middle.objects.all()
#     moveing_text=Moveing_text.objects.all()
#     banner_button=Banner_Button.objects.all()
#     bannerbottommiddle=Banner_Bottom_middle.objects.all()
#     brand=Brand.objects.all()
#     deals=Top_deals.objects.all()
#     topsell=Top_sell.objects.all()
#     specialoffer=Special_offer.objects.all()
#     category=Category.objects.all()

    

#     context = {
#         'category': category,
#         'sliders': sliders,
#         'featuresarea': featuresarea,
#         'banner_top': banner_top,
#         'banner_middle': banner_middle,
#         'moveing_text': moveing_text,
#         'banner_button': banner_button,
#         'bannerbottommiddle': bannerbottommiddle,
#         'brand': brand,
#         'deals': deals,
#         'topsell': topsell,
#         'category': category,
#         'specialoffer': specialoffer,

#     }
#     return render(request, 'home/home.html', context)











 

