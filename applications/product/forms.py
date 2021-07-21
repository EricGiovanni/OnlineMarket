from django.contrib.auth import authenticate
from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    '''
    Forms for product requiring:
    - name
    - description
    - owner
    '''
    class Meta:
        model = Product
        fields = [
            'name',
            'description',
        ]
