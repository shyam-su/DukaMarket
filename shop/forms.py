from django import forms
from .models import Checkout, Order

class CheckoutForm(forms.ModelForm):
    class Meta:
        model = Checkout
        exclude = ['user']
        
    def __init__(self, *args, **kwargs):
            self.user = kwargs.pop('user', None)  # Extract the user from kwargs
            super().__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super().save(commit=False)
        if self.user:
            instance.user = self.user  # Set the user to the current user
        if commit:
            instance.save()
        return instance
    
    
class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product', 'price', 'quantity', 'payment_method', 'status']


    
    
    