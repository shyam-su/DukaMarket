from django.shortcuts import render,get_object_or_404,redirect
from django.contrib import messages
from django.core.cache import cache
from .models import *
from home.models import *
from decimal import Decimal
from django.contrib import messages
from .forms import *
from django.db import transaction


# Create your views here.
def shop_view(request):
    try: 
        cach_data =cache.get('shop_page_data')
        if cach_data:
            context = cach_data
        else:   
            shopbanner=ShopBanner.objects.all()
            products = Product.objects.all()
            category = Category.objects.all()
            brand=Brand.objects.all()
            size=Size.objects.all()
            top_deals=Top_deals.objects.all()
            context={
                'shopbanner':shopbanner,
                'products':products,
                'category':category,
                'size':size,
                'brand':brand,
                'top_deals':top_deals,
                
            }
            cache.set('shop_page_data',context, 60 * 60 * 24)
        return render(request, 'shop/shop.html',context)
    except Exception as e:
        print(f"unknown error: {e}")
        messages.error('An error occurred while loading the Shop page. Please try again later.')
        return render(request, 'errors/404.html')
             
# def shop_view(request):
#     shopbanner=ShopBanner.objects.all()
#     products = Product.objects.all()
#     category = Category.objects.all()
#     brand=Brand.objects.all()
#     size=Size.objects.all()
#     top_deals=Top_deals.objects.all()
#     context={
#         'shopbanner':shopbanner,
#         'products':products,
#         'category':category,
#         'size':size,
#         'brand':brand,
#         'top_deals':top_deals,
        
#     }
#     return render(request, 'shop/shop.html',context)


def product(request,id):
    try:
        cache_data =cache.get('product_page_data')
        if cache_data:
            context = cache_data
        else:   
            product = get_object_or_404(Product, id=id)
            context = {
                'product': product
            }
            cache.set('product_page_data',context, 60 * 60 * 24)
        return render(request, 'shop/product.html',context)
    except Exception as e:
        print(f"unknown error: {e}")
        messages.error(request,'An error occurred while loading the Shop page. Please try again later.')
        return render(request, 'errors/404.html')

# def product(request,id):
#     product = get_object_or_404(Product, id=id)
#     print(f"Product: {product}")
#     context = {
#         'product': product 
#     }
#     return render(request, 'shop/product.html', context)

def search_view(request):
    try:
        # Try to get cached data
        cache_data = cache.get('search_page_data')
        query = request.GET.get('query', '')  # Get the query from the request

        if cache_data and query == '':  # Only use cache if there's no search query
            context = cache_data
        else:
            # If query is provided or cache is not used, fetch results
            results = Product.objects.filter(name__icontains=query) if query else []
            context = {'query': query, 'results': results}
            
            # Cache the results for 24 hours
            if query == '':  # Cache only for non-query pages (avoid caching search results)
                cache.set('search_page_data', context, 60 * 60 * 24)

        # Render the search page with the context
        return render(request, 'shop/search.html', context)

    except Exception as e:
        # Log the error for debugging
        print(f"An error occurred: {e}")
        messages.error(request, 'An error occurred while processing your search. Please try again later.')
        return render(request, 'errors/404.html')

    
# def Search(request):
#     query = request.GET.get('query', '')
#     print(query)
#     results = Product.objects.filter(name__icontains=query) if query else []
#     return render(request, 'shop/search.html', {'query': query, 'results': results})
    


def Add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    user = request.user

    # Get the quantity from the request POST data
    quantity = int(request.POST.get('quantity', 1))

    # Check if the product is already in the cart for the current user
    cart_item, created = CartItem.objects.get_or_create(
        product=product,
        user=user,
    )

    if created:
        # If the cart item was created, set the initial quantity
        cart_item.quantity = quantity
    else:
        # If the cart item already exists, update the quantity
        cart_item.quantity += quantity

    cart_item.save()
    return redirect('shop:cart')

def item_increment(request, id):
    cart_item = get_object_or_404(CartItem, id=id, user=request.user)
    cart_item.quantity += 1
    cart_item.save()
    return redirect("shop:cart")

def item_decrement(request, id):
    cart_item = get_object_or_404(CartItem, id=id, user=request.user)
    if cart_item.quantity > 1:
        cart_item.quantity -= 1
        cart_item.save()
    else:
        cart_item.delete()
    return redirect("shop:cart")

def cart_view(request):
    banner = Cart_banner.objects.all()
    cart_items = []
    total_price = 0

    if request.user.is_authenticated:
        cart_items = CartItem.objects.filter(user=request.user)
        total_price = sum(item.quantity * item.product.price for item in cart_items)
    else:
        messages.warning(request, "Please log in to view your cart.")

    context = {
        'banner': banner,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    return render(request, 'shop/cart.html', context)


def Remove_from_cart(request, item_id):
    cart_item = CartItem.objects.get(id=item_id)
    cart_item.delete()
    return redirect('shop:cart')

def item_clear(request, id):
    cart_item = CartItem.objects.get(id=id)
    cart_item.delete()
    return redirect("shop:cart")


def cart_clear(request):
    CartItem.objects.filter(user=request.user).delete()
    return redirect("shop:cart")

def Product_quick_view(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'product_quick_view.html', {'product': product})


def get_cart_items_from_request(request):
    """Retrieve cart items from POST data."""
    cart_items = request.POST.getlist('cart_items')
    items = []
    for item in cart_items:
        product_id, quantity = item.split(':')
        try:
            product = Product.objects.get(id=product_id)
            items.append({
                'product': product.name,
                'price': product.price,
                'quantity': int(quantity),
            })
        except Product.DoesNotExist:
            continue
    return items

def calculate_total_price(items):
    """Calculate total price from a list of items."""
    total_price = Decimal('0.00')
    for item in items:
        try:
            price = Decimal(item.get('price', '0.00'))
            quantity = int(item.get('quantity', 0))
            total_price += price * quantity
        except (ValueError, TypeError):
            continue
    return total_price

def checkout_view(request):
    if request.method == 'POST':
        form = CheckoutForm(request.POST, user=request.user)
        if form.is_valid():
            form.save()
            return redirect('create_order')
    else:
        form = CheckoutForm()
    return render(request, 'shop/checkout.html', {'form': form})



def create_order(request):
    if request.method == 'POST':
        # Get hidden fields data from the form
        products = request.POST.getlist('product')
        print(products)
        prices = request.POST.getlist('price')
        print(prices)
        quantities = request.POST.getlist('quantity')
        print(quantities)
        total_prices = request.POST.getlist('total_price')
        print(total_prices)
        payment_method = request.POST['payment_method']
        print(payment_method)
        status = request.POST['status']
        print(status)

        # Save order data in the database
        try:
            with transaction.atomic():
                for product, price, quantity, total_price in zip(products, prices, quantities, total_prices):
                    Order.objects.create(
                        product=product,
                        price=price,
                        quantity=quantity,
                        total_price=total_price,
                        payment_method=payment_method,
                        status=status
                    )
            messages.success(request, "Your order has been placed successfully.")
            return redirect('sucess')
        except Exception as e:
            messages.error(request, "There was an error placing your order. Please try again.")
    
    # For GET method
    return render(request, 'shop/order.html')

def sucess_view(request):
    return render(request, 'shop/sucess.html')

def order_confirmation(request):
    try:
        cach_data =cache.get('order_page_data')
        if cach_data:
            context = cach_data
        else:
            order = get_object_or_404(Order)
            cache.set('order_page_data',context, 60 * 60 * 24)
        return render(request, 'shop/order.html', {'order': order})
    except Exception as e:
        print(f"unknown error: {e}")
        messages.error(request,'An error occurred while loading the Shop page. Please try again later.')
        return render(request, 'errors/404.html')