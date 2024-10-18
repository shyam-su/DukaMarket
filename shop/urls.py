from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .views import *


app_name = 'shop'

urlpatterns = [
    path('', shop_view, name="shop"),
    path('product/<int:id>/', product, name='product'),
    path('cart/', cart_view, name="cart"),
    path('add-to-cart/<int:id>/', Add_to_cart, name='add_to_cart'),
    path('remove/<int:item_id>/', Remove_from_cart, name='remove_from_cart'),
    path('cart/item_clear/<int:id>/', item_clear, name='item_clear'),
    path('cart/item_increment/<int:id>/',item_increment, name='item_increment'),
    path('cart/item_decrement/<int:id>/',item_decrement, name='item_decrement'),
    path('cart/cart_clear/', cart_clear, name='cart_clear'),
    path('search/', search_view, name="search"),
    path('checkout/', checkout_view, name="checkout"),
    path('create-order/',create_order, name='create_order'),
    path('sucess/',sucess_view, name='sucess'),
    path('order_confirmation/',order_confirmation, name='order_confirmation'),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

