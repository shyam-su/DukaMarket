from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import CustomUser
from django.contrib.auth.forms import UserChangeForm

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Re-enter password...'}),
        }

class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Username'})
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password...'})
    )
    

class CustomUserForm(forms.ModelForm):
    class Meta:
        model = CustomUser 
        fields = ['email', 'phone_number','profile_image', 'gender',  'bio', 'location', 'birth_date']

# class ProfileForm(UserChangeForm):
#     class Meta:
#         model = CustomUser
#         fields = ['email', 'phone_number', 'gender', 'profile_image', 'bio', 'location', 'birth_date', 'role']
#         widgets = {
#             'email': forms.EmailInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your email'
#             }),
#             'phone_number': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your phone number'
#             }),
#             'gender': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#             'profile_image': forms.ClearableFileInput(attrs={
#                 'class': 'form-control-file'
#             }),
#             'bio': forms.Textarea(attrs={
#                 'class': 'form-control',
#                 'rows': 3,
#                 'placeholder': 'Tell us about yourself'
#             }),
#             'location': forms.TextInput(attrs={
#                 'class': 'form-control',
#                 'placeholder': 'Enter your location'
#             }),
#             'birth_date': forms.DateInput(attrs={
#                 'type': 'date',
#                 'class': 'form-control'
#             }),
#             'role': forms.Select(attrs={
#                 'class': 'form-control',
#             }),
#         }
