from django import forms
from .models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'product_for', 'type', 'gender', 'condition', 'category', 'occasion', 'featured', 'image1', 'image2', 'image3', 'image4']
