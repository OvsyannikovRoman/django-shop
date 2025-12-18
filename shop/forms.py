from django import forms
from .models import Product

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        # Поля, які ми створили в моделі [cite: 14]
        fields = ['title', 'price', 'product_qty', 'category'] 
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Назва товару'}),
            'price': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ціна товару'}),
            'product_qty': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Кількість'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }