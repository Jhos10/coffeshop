from django.contrib import admin
from .models import Product 
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    # Nombre del modelo de la base de datos
    model = Product
    # Lista de atributos que uno quiere que aparezcan en la base de datos
    list_display = ['name', 'price']
    # Barra de busqueda con la cual se van a poder hacer busquedas por el atributo del modelo que uno elija
    search_fields = ['name']

# Registrar en el admin de django, el primero el modelo de la base de datos y el segundo el product admin que va administrar el modelo desde el pane de admin de django
admin.site.register(Product, ProductAdmin)