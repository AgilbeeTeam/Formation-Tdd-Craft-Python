from django import forms
from shop.models import Item

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ["name", "sell_in", "quality"]
        labels = {
            "name": "Nom de l’article",
            "sell_in": "Sell In",
            "quality": "Qualité"
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Nom du produit"}),
            "sell_in": forms.NumberInput(attrs={"class": "form-control"}),
            "quality": forms.NumberInput(attrs={"class": "form-control"}),
        }