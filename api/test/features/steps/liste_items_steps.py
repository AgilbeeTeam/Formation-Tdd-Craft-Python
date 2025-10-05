
import requests
from behave import given, when, then

@given("je suis à la recherche d'un item pour ma guilde")
def step_given_items(context):
    items = []

    try :
        # Faire attention, si les tests tournent dans un container, alors cette adresse ne fonctionne pas.
        # mettre en place un moyen de charger la bonne adresse (design pattern candidat : strategy)
        r = requests.get('http://localhost:5172/items')
        context.result = r

    except Exception as e:
        print("ERROR : ",e)
        return


    return

@when("j'appel l'api")
def step_when_appel_api(context):
    return

@then("la liste doit être : {expected:d}")
def step_then_la_liste(context, expected):
    assert len(context.result) == expected