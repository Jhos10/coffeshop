from django import forms
from .models import Product
class ProductForm(forms.Form):
    name = forms.CharField(max_length=50, label='nombre')    
    description = forms.CharField(max_length=300, label='descripcion')
    price = forms.DecimalField(max_digits=10, decimal_places=2, label='precio')
    avalible = forms.BooleanField(initial=True, label='Disponible', required=False)
    photo = forms.ImageField(label='Foto', required=False)

    def save_product(self):
        Product.objects.create(
            name = self.cleaned_data['name'],
            description = self.cleaned_data['description'],
            price = self.cleaned_data['price'],
            avalible = self.cleaned_data['avalible'],
            photo = self.cleaned_data['photo'],
        )



