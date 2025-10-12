# urls.py
from django.urls import path
from . import views
from .views import ItemsListView

urlpatterns = [
    path("", views.admin_home, name="admin_home"),
    path("catalog/", ItemsListView.as_view(), name="shop_admin_catalog"),
    #    path("catalogue/", views.admin_catalog, name="shop_admin_catalog"),
    path("commandes/", views.admin_orders, name="shop_admin_orders"),
    path("clients/", views.admin_customers, name="shop_admin_customers"),
]