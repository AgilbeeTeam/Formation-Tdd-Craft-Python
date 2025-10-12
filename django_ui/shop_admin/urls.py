# urls.py
from django.urls import path
from . import views
from .views import ItemsListView

urlpatterns = [
    path("", views.admin_home, name="admin_home"),
#    path("catalog/", ItemsListView.as_view(), name="shop_admin_catalog"),
    path("catalog/", views.admin_catalog, name="shop_admin_catalog"),
    path("catalog/add/", views.admin_add_item, name="shop_admin_add_item"),
    path("catalog/update_quality/", views.admin_update_quality, name="shop_admin_update_quality"),
    path("commandes/", views.admin_orders, name="shop_admin_orders"),
    path("clients/", views.admin_customers, name="shop_admin_customers"),
]