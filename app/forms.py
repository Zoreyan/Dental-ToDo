from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Имя...',
            }),
            'text': forms.TextInput(attrs={
                'class': 'form-control mb-2',
                'placeholder': 'Описание...'
            }),
            'payment': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Стоимость...',
                'type': 'number'
            }),
        }