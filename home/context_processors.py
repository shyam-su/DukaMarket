# your_app/context_processors.py
from .models import *

def home_context(request):
    cart_items = CartItem.objects.all()
    total_quantity = sum(item.quantity for item in cart_items)
    total_price = sum(item.quantity * item.product.price for item in cart_items)
    
    return {
        'cart': cart_items,
        'total_quantity': total_quantity,
        'cart_total': total_price,
        'cart':CartItem.objects.all(),
        'socialmedialink': SocialMediaLink.objects.all(),
        'customer_care': CustomerCare.objects.all(),
        'customerservice': CustomerService.objects.all(),
        'myaccount': Myaccount.objects.all(),
        'quicklinks': Quicklinks.objects.all(),
        'aboutstore': Aboutstore.objects.all(),
        'footerlinks': Footerlinks.objects.all(),
        'paymentimg': payment_img.objects.all(),
        'navbar_text': Navbar_text.objects.all(), 
    }
