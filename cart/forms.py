from django import forms
from .models import Cake

class CartAddProductForm(forms.Form):
    quantity = forms.IntegerField(min_value=1, label='Quantity')
    override = forms.BooleanField(required=False, initial=False, widget=forms.HiddenInput)

class CakeForm(forms.ModelForm):
    class Meta:
        model = Cake
        fields = ['name', 'description', 'price', 'image', 'category']  # Include 'category' here i