import logging

from behave import given, when, then

from pymongo_get_database import get_database
from gilded_rose import Item, GildedRose


@given("je suis à la recherche d'un item pour ma guilde")
def step_given_items(context):
    items = []
    try :
        for item in get_database().items.find({}) :
            print("item : " , item)
            items.append(Item(name=item["name"], sell_in=item["sell_in"], quality=item["quality"]))
    except Exception as e:
        print(e)
        return

    context.result = items

    return

@when("j'appel l'api")
def step_when_appel_api(context):
    return

@then("la liste doit être : {expected:d}")
def step_then_la_liste(context, expected):
    assert len(context.result) == expected