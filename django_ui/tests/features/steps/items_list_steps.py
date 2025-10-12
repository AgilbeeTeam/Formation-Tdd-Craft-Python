import requests

from behave import given, when, then, fixture
from behave_django.decorators import fixtures

from shop_admin.services import GildedRose



@fixtures('tests/fixtures/catalog.json')
@given("je suis à la recherche d'un item pour ma guilde")
def step_given_items(context):
    context.service = GildedRose()
    return

@when("je récupère les articles disponible de la taverne")
def step_when_appel_api(context):
    context.list = context.service.list_items()
    print("WHEN", context.list)
    return

@then("la liste doit être de {expected:d}")
def step_then_la_liste(context, expected):
    print("THEN", context.list)
    assert len(context.list) == expected