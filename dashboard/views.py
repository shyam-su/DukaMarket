from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from user.models import *
from shop.models import *
from blog.models import *
from home.models import *


# Create your views here.
@login_required
def dashboard(request):
    # total_user=UserProfile.objects.all().count()
    total_product=Product.objects.all().count()
    total_order=Checkout.objects.all().count()
    context={
        # 'total_user':total_user,
        'total_product':total_product,
        'total_order':total_order,
    }
    return render(request, 'dashboard/includes/dashboard.html',context)

def Slider_view(request):
    slide = Slider.objects.all()
    brands = Brand.objects.all()
    deals=Deals.objects.all()

    context = {
        'slide': slide,
        'brands': brands,  
        'deals': deals  
    }

    return render(request, 'dashboard/homes/sliders/slider.html', context)


def add_slider(request):
    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        discount = request.POST.get('discount')
        sales = request.POST.get('sales')
        discount_deals_id = request.POST.get('discount_deals')
        slider_image = request.FILES.get('slider_image')
        link = request.POST.get('link')

        brand = Brand.objects.get(id=brand_id)
        discount_deals = Deals.objects.get(id=discount_deals_id)

        slider = Slider(
            barnd_name=brand,
            discount=discount,
            sales=sales,
            discount_deals=discount_deals,
            image=slider_image,
            link=link
        )
        slider.save()

        return redirect('dashboard:slider') 
    brands = Brand.objects.all()
    deals = Deals.objects.all()
    return render(request, 'dashboard/homes/sliders/slider_create.html', {'brands': brands, 'deals': deals})

    
def edit_slider(request, id):
    slider = get_object_or_404(Slider, id=id)

    if request.method == 'POST':
        brand_id = request.POST.get('brand_id')
        discount = request.POST.get('discount')
        sales = request.POST.get('sales')
        discount_deals_id = request.POST.get('discount_deals')
        link = request.POST.get('link')

        brand = Brand.objects.get(id=brand_id)
        discount_deals = Deals.objects.get(id=discount_deals_id)

        slider.barnd_name = brand
        slider.discount = discount
        slider.sales = sales
        slider.discount_deals = discount_deals
        slider.link = link

        if 'slider_image' in request.FILES:
            slider.image = request.FILES['slider_image']

        slider.save()

        return redirect('dashboard:slider')

    brands = Brand.objects.all()
    deals = Deals.objects.all()
    return render(request, 'dashboard/homes/sliders/slider_edit.html', {'slider': slider, 'brands': brands, 'deals': deals})

def delete_slider(request, id):
    slider = get_object_or_404(Slider, id=id)
    slider.delete()

    return redirect('dashboard:slider')


def feature_view(request):
    data=FeaturesArea.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/features/feature.html',context)

def create_feature(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        icon = request.POST.get('icon')
        print(title, description, icon)
        feature=FeaturesArea(title=title, description=description, icon=icon)
        feature.save()
        return redirect('dashboard:feature')  # Redirect to a list view or another page
    return render(request, 'dashboard/homes/features/feature_create.html')


def edit_feature(request,id):
    feature=FeaturesArea.objects.get(id=id)
    if request.method == 'POST':
        title=request.POST.get('title')
        description=request.POST.get('description')
        icon=request.POST.get('icon')
        feature.title=title
        feature.description=description
        feature.icon=icon
        feature.save()
        return redirect('dashboard:feature')
    return render(request, 'dashboard/homes/features/feature_edit.html',{'feature':feature})

def delete_feature(request,id):
    feature=get_object_or_404(FeaturesArea,id=id)
    feature.delete()
    return redirect('dashboard:feature')

def TopBanner_view(request):
    data=Banner_Top.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/topbanners/topbanner.html',context)

def TopBanner_create(request):
    if request.method == 'POST':
        deals = request.POST.get('deals')
        image = request.FILES.get('image')        
        discount = request.POST.get('discount')
        quote = request.POST.get('quote')
        link = request.POST.get('link')
        deals=Deals.objects.get(id=deals)
        
        topbanner=Banner_Top(deals=deals, image=image, discount=discount,quote=quote,link=link)
        topbanner.save()
        return redirect('dashboard:topbanner') 
    deals = Deals.objects.all()
    return render(request, 'dashboard/homes/topbanners/topbanner_create.html', {'deals': deals})

def TopBanner_edit(request, id):
    banner_top = Banner_Top.objects.get(id=id)
    deals = Deals.objects.all()

    if request.method == 'POST':
        # Get the request data
        deal_id = request.POST.get('deals')
        image = request.FILES.get('image')
        discount = request.POST.get('discount')
        quote = request.POST.get('quote')
        link = request.POST.get('link')

        # Validate the data
        if not deal_id:
            messages.error(request, 'Please select a discount deal')
        elif not image and not banner_top.image:
            messages.error(request, 'Please upload an image')
        elif not discount:
            messages.error(request, 'Please enter a discount')
        elif not quote:
            messages.error(request, 'Please enter a quote')
        elif not link:
            messages.error(request, 'Please enter a link')
        else:
            # Update the banner top instance
            banner_top.deals_id = deal_id
            if image:
                banner_top.image = image
            banner_top.discount = discount
            banner_top.quote = quote
            banner_top.link = link
            banner_top.save()

            messages.success(request, 'Top banner updated successfully')
            return redirect('dashboard:topbanner')  # Replace with your desired redirect URL

    return render(request, 'dashboard/homes/topbanners/topbanner_edit.html', {'banner_top': banner_top, 'deals': deals})
   
   
def TopBanner_delete(request,id):
    topban=get_object_or_404(Banner_Top,id=id)
    topban.delete()
    return redirect('dashboard:topbanner')

def Top_Deals_view(request):
    top=Top_deals.objects.all()
    context={
        'top':top
    }
    return render(request, 'dashboard/homes/topdeals/topdeal.html',context)

def Top_Deals_create(request):
    if request.method == 'POST':
        form = Top_dealsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:topdeals')  # Replace with your actual success URL
    else:
        form = Top_dealsForm()
    
    return render(request, 'dashboard/homes/topdeals/topdeal_create.html', {'form': form})


def Top_Deals_edit(request, id):  # 'id' is passed through the URL
    top_deal = get_object_or_404(Top_deals, id=id)  # Retrieve the existing object
    
    if request.method == 'POST':
        form = Top_dealsForm(request.POST, instance=top_deal)  # Bind the form with the instance
        if form.is_valid():
            form.save()  # Save changes
            return redirect('dashboard:topdeals')  # Redirect after successful save
    else:
        form = Top_dealsForm(instance=top_deal)  # Populate form with existing data

    return render(request, 'dashboard/homes/topdeals/topdeal_edit.html', {'form': form})


def Top_Deals_delete(request,id):
    topdeal=get_object_or_404(Top_deals,id=id)
    topdeal.delete()
    return redirect('dashboard:topdeals')

def Banner_Midle_view(request):
    data=Banner_Middle.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/bannermidles/bannermidle.html',context)

def Banner_Midle_create(request):
    if request.method == 'POST':
        form = Banner_MiddleForm(request.POST, request.FILES)  # Handle file upload with request.FILES
        if form.is_valid():
            form.save()
            return redirect('dashboard:bannermidle')
        else:
            print(form.errors) # Ensure this URL exists
    else:
        form = Banner_MiddleForm()
    
    return render(request, 'dashboard/homes/bannermidles/bannermidle_create.html', {'form': form})


def Banner_Midle_edit(request, id):
    baner_mid = get_object_or_404(Banner_Middle, id=id)  # Retrieve the existing object

    if request.method == 'POST':
        form = Banner_MiddleForm(request.POST, request.FILES, instance=baner_mid)  # Include request.FILES for image upload
        if form.is_valid():
            form.save()  # Save changes
            return redirect('dashboard:bannermidle')  # Redirect after successful save
    else:
        form = Banner_MiddleForm(instance=baner_mid)  # Load the form with the instance data
    
    return render(request, 'dashboard/homes/bannermidles/bannermidle_edit.html', {'form': form, 'baner_mid': baner_mid})


def Banner_Midle_delete(request,id):
    bann_mid=get_object_or_404(Banner_Middle,id=id)
    bann_mid.delete()
    return redirect('dashboard:bannermidle')

def Top_Sells_view(request):
    data=Top_sell.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/topsells/topsell.html',context)

def Top_Sells_create(request):
    if request.method == 'POST':
        form = Top_sellForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:topsells')  # Replace with your actual success URL
    else:
        form = Top_sellForm()
    
    return render(request, 'dashboard/homes/topsells/topsell_create.html', {'form': form})

def Top_Sells_edit(request, id):  # 'id' is passed through the URL
    top_sell = get_object_or_404(Top_sell, id=id)  # Retrieve the existing object
    
    if request.method == 'POST':
        form = Top_sellForm(request.POST, instance=top_sell)  # Bind the form with the instance
        if form.is_valid():
            form.save()  # Save changes
            return redirect('dashboard:topsells')  # Redirect after successful save
    else:
        form = Top_sellForm(instance=top_sell)  # Populate form with existing data

    return render(request, 'dashboard/homes/topsells/topsell_edit.html', {'form': form})

def Top_Sells_delete(request,id):
    topsell=get_object_or_404(Top_sell,id=id)
    topsell.delete()
    return redirect('dashboard:topsells')

def Special_Offers_view(request):
    data=Special_offer.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/specialoffers/specialoffer.html',context)

def Special_Offers_create(request):
    if request.method == 'POST':
        form = Special_OffersForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard:specialoffers')  # Replace with your actual success URL
    else:
        form = Special_OffersForm()
    
    return render(request, 'dashboard/homes/specialoffers/specialoffer_create.html', {'form': form})


def Special_Offers_edit(request, id):
    special_offer = get_object_or_404(Special_offer, id=id)
    
    if request.method == 'POST':
        form = Special_OffersForm(request.POST, instance=special_offer)
        if form.is_valid():
            form.save()
            return redirect('dashboard:specialoffers')  # Replace with your actual success URL
    else:
        form = Special_OffersForm(instance=special_offer)
    
    return render(request, 'dashboard/homes/specialoffers/specialoffer_edit.html', {'form': form})

def Special_Offers_delete(request,id):
    sepcial=get_object_or_404(Special_offer,id=id)
    sepcial.delete()
    return redirect('dashboard:specialoffers')


def Moveing_Texts_view(request):
    mov=Moveing_text.objects.all()
    context={
        'mov':mov
    }
    return render(request, 'dashboard/homes/moveingtexts/moveingtext.html',context)

def Moveing_Texts_create(request):
    if request.method == 'POST':
        form = MovingtextForm(request.POST)
        if form.is_valid():
            # Handle form data manually since it's a regular Form, not ModelForm
            text1 = form.cleaned_data['text1']
            text2 = form.cleaned_data['text2']
            text3 = form.cleaned_data['text3']

            # Create the Moveing_text instance (if it's a model)
            Moveing_text.objects.create(text1=text1, text2=text2, text3=text3)

            return redirect('dashboard:moveingtexts')  # Redirect after saving
    else:
        form = MovingtextForm()

    return render(request, 'dashboard/homes/moveingtexts/moveingtext_create.html', {'form': form})


def Moveing_Texts_edit(request, id):
    moveing_text = get_object_or_404(Moveing_text, pk=id)  # Use 'id' as per URL pattern

    if request.method == 'POST':
        form = MovingtextForm(request.POST, instance=moveing_text)
        if form.is_valid():
            form.save()
            return redirect('dashboard:moveingtexts')  # Redirect after successful update
    else:
        form = MovingtextForm(instance=moveing_text)

    return render(request, 'dashboard/homes/moveingtexts/moveingtext_edit.html', {'form': form, 'moveing_text': moveing_text})

def Moveing_Texts_delete(request,id):
    move=get_object_or_404(Moveing_text,id=id)
    move.delete()
    return redirect('dashboard:moveingtexts')


def Brand_view(request):
    data=Brand.objects.all()
    context={
        'data':data
    }
    return render(request, 'dashboard/homes/brands/brand.html',context)

def Brand_create(request):
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('dashboard:brand')  # Redirect to the brand list view after saving
    else:
        form = BrandForm()
    return render(request, 'dashboard/homes/brands/brand_create.html', {'form': form})


def Brand_edit(request, id):
    brand = get_object_or_404(Brand, id=id)
    if request.method == 'POST':
        form = BrandForm(request.POST, request.FILES, instance=brand)
        if form.is_valid():
            form.save()
            return redirect('dashboard:brand')  # Redirect to the brand list view after saving
    else:
        form = BrandForm(instance=brand)
    return render(request, 'dashboard/homes/brands/brand_edit.html', {'form': form})

def Brand_delete(request,id):
    brand=get_object_or_404(Category,id=id)
    brand.delete()
    return redirect('dashboard:brand')


def Dash_category(request):
    categ=Category.objects.all()
    context={
        'categ':categ
    }
    return render(request, 'dashboard/shops/category/das_category.html',context)



def Dash_category_delete(request,id):
    cat=get_object_or_404(Category,id=id)
    cat.delete()
    return redirect('dashboard:dash_category')