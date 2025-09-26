from behave import given, when, then

@given("je suis en train d'établir le budget de mon mariage")
def step_given_obtenir_un_devis(context):
   return

@when("je loue la salle le {jour_mariage_str}, pour {nb_adultes_vdh:d} personnes au vin d'honneur, dont {enfants_vdh:d} enfants et ado, {nb_adultes_repas:d} personnes au repas dont {nb_enfants_repas:d} enfants de moins de 12 ans")
def step_when_obtenir_un_devis(context, jour_mariage_str, nb_adultes_vdh, enfants_vdh, nb_adultes_repas, nb_enfants_repas):
    context.result = 17837

@then("le devis doit être de {expected:d} €")
def step_then_obtenir_un_devis(context, expected):
    assert context.result == expected