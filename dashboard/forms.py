from django import forms
from home.models import *
from shop.models import *



class Top_dealsForm(forms.ModelForm):
    class Meta:
        model = Top_deals
        fields = ('name',)
        
        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'name',
                'required': True
            }),
        }
        
class Banner_MiddleForm(forms.ModelForm):
    class Meta:
        model = Banner_Middle
        fields = ('deals', 'image', 'quote','discount','link')
        widgets = {
            'deals': forms.Select(attrs={
                'class': 'form-control',
                'id': 'deals',
                'required': True

            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'image',
            }),
            'quote': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'quote',
            }),
            'discount': forms.NumberInput(attrs={
                'class': 'form-control',
                'id': 'discount',
            }),
            'link': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'link',
            }),
        }
        
class Top_sellForm(forms.ModelForm):
    class Meta:
        model = Top_sell
        fields = ('name',)
        
        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'name',
                'required': True
            }),
        }

        
class Special_OffersForm(forms.ModelForm):
    class Meta:
        model = Special_offer
        fields = ('name',)
        
        widgets = {
            'name': forms.Select(attrs={
                'class': 'form-control',
                'id': 'name',
                'required': True
            }),
        }

class MovingtextForm(forms.ModelForm):
    class Meta:
        model = Moveing_text
        fields = ('text1', 'text2', 'text3')
        widgets = {
            'text1': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'text1',
                'required': True

            }),
            'text2': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'text2',
            }),
            'text3': forms.TextInput(attrs={
                'class': 'form-control',
                'id': 'text3',
            }),
        }

class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = ('name', 'image')
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control', 
                'id': 'brandName',
                'required': True
            }),
            'image': forms.ClearableFileInput(attrs={
                'class': 'form-control',
                'id': 'barndImage'
            })
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name',)
