from django import forms

from products.models import Product


class ProductForm(forms.ModelForm):
    name = forms.CharField(required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))

    price = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ლარი'}))
    discount = forms.DecimalField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'ლარი'}))
    quantity = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    isbn = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))

    number_of_pages = forms.IntegerField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    language = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    height = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'სმ'}))
    width = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'სმ'}))

    class Meta:
        model = Product
        fields = (
            'name',
            'category',
            'price',
            'discount',
            'quantity',
            'delivery',
            'isbn',
            'cover',
            'number_of_pages',
            'language',
            'height',
            'width',
            'image'
        )
