from django.contrib import admin
from .models import Order, OrderProduct
# Register your models here.

# Este es para que muestre los productos para uno agregar a la orden
class OrderProductInlineAdmin(admin.TabularInline):
    # Modelo que se quiere mostrar para agregar en la orden
    model = OrderProduct
    # Para que no haga extra lineas
    extra = 0

# Sirve para personalizar cada uno de los orders
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderProductInlineAdmin
    ]


# Se pasa el modelo y la clase de configuracion
admin.site.register(Order, OrderAdmin)