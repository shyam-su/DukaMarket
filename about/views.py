from django.shortcuts import render
from django.core.cache import cache
from django.contrib import messages
from .models import Banner, AboutSection, Service, TechnologyIndex, TeamMember, Location

# Create your views here.
def about_view(request):
    try:
        # Check if the cached data exists
        cached_data = cache.get('about_page_data')
        
        if cached_data:
            context = cached_data
        else:
            # Fetch data from the database
            banner = Banner.objects.all()
            aboutsection = AboutSection.objects.all()
            service = Service.objects.all().order_by('step_number')
            technologyindex = TechnologyIndex.objects.all()
            teammember = TeamMember.objects.all()
            location = Location.objects.all()
            
            # Handling the case where services may be empty
            if service.exists():
                services_area_title = service[0].services_area_title
                services_area_description = service[0].services_area_description
            else:
                services_area_title = "Default Title"
                services_area_description = "Default Description"
            
            # Prepare the context dictionary
            context = {
                'banner': banner,
                'aboutsection': aboutsection,
                'service': service,
                'services_area_title': services_area_title,
                'services_area_description': services_area_description,
                'technologyindex': technologyindex,
                'teammember': teammember,
                'locations': location,
            }
            
            # Cache the context for 10 minutes
            cache.set('about_page_data', context, 600)

        return render(request, 'about/about.html', context)
    
    except Exception as e:
        # Log the exception for debugging purposes (optional)
        print(f"Error occurred: {e}")
        
        # Display a user-friendly message
        messages.error(request, "An error occurred while loading the About page. Please try again later.")
        
        # Return a fallback response or a custom error page
        return render(request, 'errors/404.html')





# from django.shortcuts import render
# from .models import *

# # Create your views here.
# def about_view(request):
#     banner=Banner.objects.all()
#     aboutsection=AboutSection.objects.all()
#     service=Service.objects.all().order_by('step_number')
#     technologyindex=TechnologyIndex.objects.all()
#     teammember=TeamMember.objects.all()
#     location=Location.objects.all()
#     if service.exists():
#         services_area_title = service[0].services_area_title
#         services_area_description = service[0].services_area_description
#     else:
#         services_area_title = "Default Title"
#         services_area_description = "Default Description"
    
#     context={
#         'banner':banner,
#         'aboutsection':aboutsection,
#         'service':service,
#         'services_area_title': services_area_title,
#         'services_area_description': services_area_description,
#         'technologyindex':technologyindex,
#         'teammember':teammember,
#         'locations':location,
             
#              }
    
#     return render(request,'about/about.html',context)