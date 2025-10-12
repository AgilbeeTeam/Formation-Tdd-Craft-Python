from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Item

# Create your views here.
def admin_home(request):
    return render(request, "shop_admin/home.html")


class ItemsListView(ListView):
    model = Item
    context_object_name = "items"
    paginate_by = 10  # if pagination is desired
    template_name = "shop_admin/catalog.html"
    ordering = "name"

def admin_orders(request):
    return render(request, "shop_admin/orders.html")

def admin_customers(request):
    return render(request, "shop_admin/customers.html")