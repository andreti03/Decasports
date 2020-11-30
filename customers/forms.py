from django import forms
from .models import Customer
from address.models import Address

class Update_customer(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ['first_name', 'last_name', 'birthdate', 'phone_number']

        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'birthdate': forms.DateInput(format ='%m/%d/%Y', attrs={'class': 'form-control'}),
            'phone_number': forms.TextInput(attrs={'class': 'form-control'}),
        }

class Update_address(forms.ModelForm):

    class Meta:
        model = Address
        fields = ['address']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
        }