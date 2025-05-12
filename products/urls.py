from django.urls import path
from .views import *

urlpatterns  = [
    path('', ProductList.as_view() ,name = 'list_products'),
    path('formulario_producto/', ProductFormView.as_view(), name='new_product')
]