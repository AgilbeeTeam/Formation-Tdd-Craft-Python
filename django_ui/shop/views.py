from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Item


#from shop.models import Item

# Create your views here.
def home(request):
    url_name = getattr(getattr(request, "resolver_match", None), "url_name", "")
    return render(request, "buyer/buyer_home.html", {"title": "Accueil boutique", "auth_menu_active": url_name in ("login", "profile")})


class ItemsListView(ListView):
    model = Item
    context_object_name = "items"
    paginate_by = 10  # if pagination is desired
    template_name = "buyer/catalog.html"
    ordering = "name"


def not_yet(request):
    return render(request, "not_yet_implemented.html")