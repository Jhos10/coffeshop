from django.shortcuts import render
from django.views.generic import TemplateView,FormView,ListView
from django.urls import reverse_lazy
from .models import *
from .forms import *
# Create your views here.

# class ProductList(TemplateView):
#     template_name = 'products/products.html'

#     def get_context_data(self):
#         list_prdoucts = Product.objects.all()
#         return {'list_products': list_prdoucts}
    

class ProductList(ListView):
    model = Product
    template_name = 'products/products.html'
    context_object_name = 'list_products'

class ProductFormView(FormView):
    template_name = 'products/new_product.html'
    form_class = ProductForm
    success_url = reverse_lazy('list_products')

    def form_valid(self, form):
        form.save_product()
        return super().form_valid(form)