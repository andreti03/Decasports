from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from customers.models import Customer 
from address.models import Address
from city.models import City 


class CreateUserForm(UserCreationForm):
    password1 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(widget= forms.PasswordInput(attrs={'class': 'form-control'}))
    
    class Meta:
        model = User
        fields =['username','email']

        widgets ={
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Create_customer(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthdate', 'phone_number']
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(format ='%m-%d-%Y', attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Create_address(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }


class Create_city(forms.ModelForm):

    class Meta: 
        model = City
        fields = ['city_name', 'country']
        widgets = {
            'city_name': forms.TextInput(attrs={'class': 'form-control'}),
            'country': forms.TextInput(attrs={'class': 'form-control'}),
        }