from django.views.generic import DetailView
from .models import Order
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.
class OrderView(LoginRequiredMixin,DetailView):
    model = Order
    template_name = 'orders.html'
    context_object_name = 'order'

    def get_object(self, queryset = ...):
        user_current = self.request.user
        return Order.objects.filter(user =user_current, is_active = True).first()