# Formation Agilbee - Support technique
License : LICENSE.txt

Objectif : TDD, Clean Code, Architecture, Refactoring

## Configuration de son environnement

### Les commandes docker à lancer pour initier son environnement de dev

La Stack VueJS, FastAPI, MongoDB 
   
    docker compose up -d --force-recreate db db-ui
    docker compose up --watch api ui

La Stack Django, Postgresql 
    
    docker compose up -d --force-recreate db db-ui
    docker compose up --watch 

    python manage.py migrate
    python manage.py createsuperuser --username=admin --email=admin@example.com
    python manage.py loaddata catalogue.json
    
    python manage.py runserver

Ouvrir la page : http://127.0.0.1:8000/shop/catalogue 
Vous devez avoir une liste de 9 "items"

ATTENTION n'oubliez de définir un mot de passe (ex : admin)

## Ressources

Lien vers les repos qui ont servi à construire les exercices : 

### GildedRose Refactoring Kata
https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main

### Docker et Vue.js 
https://github.com/kristiyan-velkov/docker-vuejs-sample
et https://docs.docker.com/guides/vuejs/

### Docker et Django
https://www.docker.com/blog/how-to-dockerize-django-app/

---

# Les instructions des exercices

---

## Thème TU - PyTest ou unittest - Mise en jambe

> Objectif principal : découvrir le fonctionnement de la bibliothèque de test (unittest ou pytest) et aussi des bonnes pratiques (FIRST et Right - BICEPs)
> Objectif secondaire : Découvrir le mode "Dojo"
 
### Exercice 1 : le cadre de test

A faire dans le répertoire "Exercice"

créer une fonction de fibonacci 
- f(0) = 0
- f(1) = 1
- f(N) = f(n-1)+f(n-2)

Votre choix : 
- réaliser l'algorithme directement puis faire les tests
- réaliser un test et puis le code (forme TDD)
- réaliser tout les tests et coder l'algorithme
- ou toutes autres façons qui vous plait 

***Contraintes*** : les tests ne doivent pas être liés entre eux, ils sont indépendants des uns et des autres

### Exercice 2 : que devons-nous tester ?

Implementer les tests et les correctifs pour respecter le BICEPs
- Bondaries (**B**) : Testez les limites (0, vide, max, null…).
- Inverse (**I**) : Testez le comportement inverse (ajouter → retirer, encoder → décoder) 
- Cross Check (**C**) : Vérifiez un résultat par un autre moyen indépendant (par exemple comparer la somme et le total calculé) : Usage d'une autre librairie ? d'une autre méthode de calcul ?
- Error condition (**E**) : Testez les cas d’erreurs, exceptions, entrées invalides.
- Performance (**P**) : Vérifiez les performances et le temps d’exécution si c’est critique. |
- set (**s**) : Assurez-vous d’avoir testé l’ensemble des cas pertinents : valeurs valides, invalides, inverses, limites, erreurs, performances. 

***Contraintes*** : le résultat ne doit prendre plus de 1 ms pour un N = 1000 

### Exercice 3 : Mes premiers refactoring de code

1. Détecter tous les doublons de codes (copy / paste), y compris dans les tests.
2. Supprimer le plus de doublons de code ou code similaire
3. Renommer les tests unitaires (un bon nommage de tests unitaires est aussi important que le test lui-même,  car il transforme la suite de tests en documentation vivante du comportement fonctionnel du projet.)

***Contraintes*** :  Vous allez mettre à jour soit un test, soit le code mais jamais les deux en même temps 
***Tips*** : La Formule →  [Méthode ou Comportement]_[Contexte]_[RésultatAttendu]
> test_ajout_article_panier_vide_nouveau_panier_cree

### Exercice 4 : Application de FIRST
- Fast (**F**) : Le test doit s’exécuter très rapidement (moins d’une seconde). Si les tests sont lents, on ne les lancera pas souvent.
- Independent (**I**) : Chaque test doit être indépendant des autres (pas d’ordre d’exécution, pas de partage d’état global).
- Repeatable (**R**) : Le test doit donner le même résultat à chaque exécution, sur n’importe quelle machine, à n’importe quelle heure. Pas de dépendance à l’environnement.
- Self-Validating (**S**) :  Le test doit se valider lui-même (succès/échec clair, sans lecture manuelle d’un log ou d’un print).
- Timely (**T**) : Le test doit être écrit au bon moment, idéalement avant le code de production (TDD), ou du moins juste après.

- Rédiger les tests et le code permettant de lire des indices N d'un fichier et écrire le résultat dans le même fichier

