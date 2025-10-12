from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib import messages
from decimal import Decimal
from django.db.models import Sum, F, Q, Count, DecimalField
from django.shortcuts import render

from shop.models import Item
from shop.models import Customer

from .forms import ItemForm


# Create your views here.
def admin_home(request):
    return render(request, "shop_admin/home.html")

def admin_catalog(request):
    items = Item.objects.all().order_by("name")
    form = ItemForm()
    return render(request, "shop_admin/catalog.html", {"items": items, "form": form})

class ItemsListView(ListView):
    model = Item
    form = ItemForm()
    context_object_name = "items"
    paginate_by = 10  # if pagination is desired
    template_name = "shop_admin/catalog.html"
    ordering = "name"

def admin_orders(request):
    return render(request, "shop_admin/orders.html")

def admin_customers(request):
    buyers = (
        Customer.objects
        .annotate(
            total_achats=Sum(
                F("orders__items__quantity") * F("orders__items__unit_price"),
                filter=Q(orders__status="PAID"),
                output_field=DecimalField(max_digits=12, decimal_places=2),
            ),
            cart_count=Count("cart__items"),  # 0 si pas de panier ou vide
        )
        .order_by("name")
    )
    return render(request, "shop_admin/customers.html", {"buyers": buyers})

def admin_add_item(request):
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Article ajouté avec succès !")
    return redirect("shop_admin_catalog")

def admin_update_quality(request):
    if request.method == "POST":
        messages.success(request, "Qualité mise à jour pour tous les articles.")
    return redirect("shop_admin_catalog")