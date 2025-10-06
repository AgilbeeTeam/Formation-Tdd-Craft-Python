from django.urls import path

from . import views
from .views import ItemsListView

urlpatterns = [
    path("", views.index, name="index"),
    path("catalogue", ItemsListView.as_view(), name="catalogue"),
]