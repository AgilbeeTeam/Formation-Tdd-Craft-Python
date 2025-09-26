Feature: Obtenir un devis
Scenario: Le devis avec seulement les éléments obligatoires
  Given je suis en train d'établir le budget de mon mariage
  When je loue la salle le 15 aout 2026, pour 125 personnes au vin d'honneur, dont 30 enfants et ado, 37 personnes au repas dont 13 enfants de moins de 12 ans
  Then le devis doit être de 17837 €