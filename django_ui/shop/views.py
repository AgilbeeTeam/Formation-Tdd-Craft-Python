from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView

from shop.models import Item


#from shop.models import Item

# Create your views here.
def index(request):
    return HttpResponse("Hello, world. You're at the shop index.")


class ItemsListView(ListView):
    model = Item
    context_object_name = "items"
    paginate_by = 10  # if pagination is desired
    template_name = "items.html"
    ordering = "name"

