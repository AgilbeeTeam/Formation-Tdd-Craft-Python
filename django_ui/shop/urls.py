from django.urls import path

from . import views
from .views import ItemsListView

urlpatterns = [
    path("", views.home, name="buyer_home"),
    path("catalogue", ItemsListView.as_view(), name="catalogue"),
    path("cart", views.not_yet, name="cart"),
    path("login", views.not_yet, name="login"),
]