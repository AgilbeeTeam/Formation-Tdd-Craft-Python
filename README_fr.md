# Formation Agilbee - Support technique
License : LICENSE.txt

Objectif : TDD, Clean Code, Architecture, Refactoring

## Configuration de son environnement

### les outils à installer : 

	pip install -r ./django_ui/requirements.txt
	pip install -r ./api/requirements.txt


### Les commandes docker à lancer pour initier son environnement de dev

La Stack VueJS, FastAPI, MongoDB 
   
    docker compose up -d --force-recreate db db-ui
    docker compose up --watch api ui

La Stack Django, Postgresql 
    
    docker compose up -d db-postgresql

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

## Thème TU - PyTest ou unittest - Les Techniques de base

> Objectif principal : découvrir le fonctionnement de la bibliothèque de test (unittest ou pytest) et aussi des bonnes pratiques (FIRST et Right - BICEPs)
> Objectif secondaire : Découvrir le mode "Dojo"
 
Références
- unittest : https://docs.python.org/3/library/unittest.html
- pytest : https://docs.pytest.org/en/stable/

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

***Contraintes*** : 
- Les tests ne doivent pas être liés entre eux, 
- Ils sont indépendants des uns et des autres
- Ils suivent une structure 3A (Acteur, Action, Assertion)

### Exercice 2 : que devons-nous tester ?

Implementer les tests et les correctifs pour respecter le BICEPs
- Bondaries (**B**) : Testez les limites (0, vide, max, null…).
- Inverse (**I**) : Testez le comportement inverse (ajouter → retirer, encoder → décoder) 
- Cross Check (**C**) : Vérifiez un résultat par un autre moyen indépendant (par exemple comparer la somme et le total calculé) : Usage d'une autre librairie ? d'une autre méthode de calcul ?
- Error condition (**E**) : Testez les cas d’erreurs, exceptions, entrées invalides.
- Performance (**P**) : Vérifiez les performances et le temps d’exécution si c’est critique. |
- set (**s**) : Assurez-vous d’avoir testé l’ensemble des cas pertinents : valeurs valides, invalides, inverses, limites, erreurs, performances. 

***Contraintes*** : le résultat ne doit prendre plus de 1 ms pour un N = 1000 

### Exercice 3 : Application de FIRST
- Fast (**F**) : Le test doit s’exécuter très rapidement (moins d’une seconde). Si les tests sont lents, on ne les lancera pas souvent.
- Independent (**I**) : Chaque test doit être indépendant des autres (pas d’ordre d’exécution, pas de partage d’état global).
- Repeatable (**R**) : Le test doit donner le même résultat à chaque exécution, sur n’importe quelle machine, à n’importe quelle heure. Pas de dépendance à l’environnement.
- Self-Validating (**S**) :  Le test doit se valider lui-même (succès/échec clair, sans lecture manuelle d’un log ou d’un print).
- Timely (**T**) : Le test doit être écrit au bon moment, idéalement avant le code de production (TDD), ou du moins juste après.

- Rédiger les tests et le code permettant de lire des indices N d'un fichier et écrire le résultat dans le même fichier

### Exercice 4 : Mes premiers refactoring de code

1. Détecter tous les doublons de codes (copy / paste), y compris dans les tests.
2. Supprimer le plus de doublons de code ou code similaire
3. Renommer les tests unitaires (un bon nommage de tests unitaires est aussi important que le test lui-même,  car il transforme la suite de tests en documentation vivante du comportement fonctionnel du projet.)

***Contraintes*** :  Vous allez mettre à jour soit un test, soit le code mais jamais les deux en même temps 
***Tips*** : La Formule →  [Méthode ou Comportement]_[Contexte]_[RésultatAttendu]
> test_ajout_article_panier_vide_nouveau_panier_cree


## Thème TDD - Methode - Les Techniques de base

> Objectif principal : Applique le cycle de développement TDD, la redaction d'un Test = Conception  / design de son code
> Objectif secondaire : 
 
Références
- unittest : https://docs.python.org/3/library/unittest.html
- pytest : https://docs.pytest.org/en/stable/

### Exercice 5 : Kata Bowling
Temps : 40 à 60 min max 

Implémenter une fonction qui calcul le score **TOTAL** d'une partie de Bowling

---

**Les règles de calcul** :
- Le jeu se découpe en **10 manches** (“frame”)
- A chaque partie, le joueur a **2 jets** pour faire tomber les 10 quilles.
- Le score pour la manche est le total du nombre de quilles tombées, plus des bonus pour les Strikes et les Spares.

- Un Spare arrive lorsque le joueur fait tomber les 10 quilles en 2 fois. 
- Le bonus à ajouter est alors le nombre de quilles tombées lors du prochain jet de la prochaine partie

- Un Strike arrive lorsque le joueur fait tomber les 10 quilles en une seule fois lors du 1er jet d'une manche.
- Le bonus pour cette partie est la valeur des 2 prochains lancés.

- Dans la 10ème manche, un joueur qui réalise un Spare ou un Strike est autorisé à réaliser un jet supplémentaire pour compléter la partie.
- pas + de 3 jets peuvent être réalisés dans la 10ème manche.

---


***Contraintes*** :  
- Cycle de pair-programming de 5 min (8 à 12 cycles)
- En TDD :)

## Thème TU - Api - DB - Mock - Techniques avancés

> Objectif principal : Découvrir des activités de tests plus avancés et proche d'une situation réelle de développement.
> Objectif secondaire : Les tests avec les BD, les API et les mocks
 
Références
- unittest.mock : https://docs.python.org/fr//3/library/unittest.mock-examples.html
- pytest-mock : https://pytest-mock.readthedocs.io/en/latest/ 
- mockito-python : (inspiré de la bibliothèque Java Mockito) https://mockito-python.readthedocs.io/en/latest/

### Exercice 6 : 

A partir Gilderose shop, metter en place un appel API fournisseur pour faire un réapprovisionner la boutique.

***Contraintes*** : 

***Tips*** : pouvez mettre en place un réassort automatique avec un design pattern de type Observeur et / ou Command


### Exercice 7 : 

Bonjour et bienvenue dans l'équipe de la Gilded Rose.

Comme vous le savez, notre petite taverne située à proximité d'une cité importante est dirigée par l'aubergiste amicale Allison.

Nous achetons et vendons uniquement les meilleurs produits.
Malheureusement, la qualité de nos marchandises se dégrade constamment à l'approche de leur date de péremption.

Un système a été mis en place pour mettre à jour notre inventaire.
Il a été développé par Leeroy, une personne pleine de bon sens qui est partie pour de nouvelles aventures.

Votre mission est d'ajouter une nouvelle fonctionnalité à notre système pour que nous puissions commencer à vendre un nouveau type de produits.

Mais d'abord, laissez-moi vous présenter notre système :

- Tous les éléments ont une valeur `sellIn` qui désigne le nombre de jours restant pour vendre l'article.
- Tous les articles ont une valeur `quality` qui dénote combien l'article est précieux.
- À la fin de chaque journée, notre système diminue ces deux valeurs pour chaque produit.

Plutôt simple, non ?

Attendez, ça devient intéressant :

- Une fois que la date de péremption est passée, la qualité se dégrade deux fois plus rapidement.
- La qualité (`quality`) d'un produit ne peut jamais être négative.
- "Aged Brie" augmente sa qualité (`quality`) plus le temps passe.
- La qualité d'un produit n'est jamais de plus de 50.
- "Sulfuras", étant un objet légendaire, n'a pas de date de péremption et ne perd jamais en qualité (`quality`)
- "Backstage passes", comme le "Aged Brie", augmente sa qualité (`quality`) plus le temps passe (`sellIn`) ; La qualité augmente de 2 quand il reste 10 jours ou moins et de 3 quand il reste 5 jours ou moins, mais la qualité tombe à 0 après le concert.


A partir Gilderose shop, dans l'application coté marchand, ajouter un service pour mettre à jour le catalogue 
SAchez que la class  et la méthode exist déjà mais on ne sait pas si elle répond au spec.

***Contraintes*** : 
Usage de Teardown et setup pour charger et nettoyer la base de donnée de test.

***Tips*** : pouvez mettre en place un réassort automatique avec un design pattern de type Observeur et / ou Command


## Thème TDD - Refactoring - Techniques Avancés

> Objectif principal : Découvrir les techniques de refactoring simples et avancées
> Objectif secondaire : 

****Le refactoring.****

Le refactoring consiste à modifier la structure interne du code pour le rendre plus lisible, plus simple, plus maintenable,
sans changer ce qu’il fait.

🧱 Les grandes familles de techniques de refactoring
1. **Refactoring de nommage** : Clarifier l’intention (méthodes, variables, classes, fichiers).
2. **Refactoring de structure de code**	: Simplifier, réduire la duplication, isoler les responsabilités.
3. **Refactoring orienté objet** : Améliorer l’encapsulation, la hiérarchie, le polymorphisme.
4. **Refactoring de tests** : Simplifier, factoriser, rendre les tests plus expressifs et robustes.
5. **Refactoring architectural** : Réorganiser les dépendances, couches, modules ou composants.
6. **Refactoring de données** : Améliorer les structures, clarifier les modèles de domaine.
7. **Refactoring de performances** :	Optimiser sans casser la lisibilité (en dernier recours).

🧠 Les techniques fondamentales (tirées de Martin Fowler et de la pratique TDD)

🏷️ Refactoring de noms et intentions
* Rename Variable / Method / Class – nommer selon l’intention métier
* Introduce Explaining Variable – extraire une variable pour expliciter une condition complexe
* Rename Field / Parameter – clarifier le sens fonctionnel
* Replace Magic Number with Named Constant – rendre les valeurs explicites

🧩 Refactoring de structure
* Extract Method – isoler une partie de code dans une méthode nommée clairement
* Inline Method / Variable – faire l’inverse si la méthode ne fait qu’un appel trivial
* Extract Class / Module – isoler une responsabilité dans une nouvelle entité
* Inline Class – fusionner deux classes trop fragmentées
* Move Method / Field – déplacer là où la logique est vraiment pertinente
* Split Variable – éviter qu’une variable serve à plusieurs choses
* Remove Dead Code – supprimer le code inutilisé

🔁 Refactoring de logique
* Replace Conditional with Polymorphism – substituer un if/else complexe par des classes spécialisées
* Decompose Conditional – extraire des sous-fonctions de conditions pour clarifier les cas
* Consolidate Conditional Expression – regrouper plusieurs tests identiques
* Replace Nested Conditional with Guard Clauses – clarifier les branches d’erreur dès le début
* Replace Temp with Query – supprimer les variables temporaires inutiles
* Replace Loop with Pipeline – remplacer les boucles par des fonctions (map, filter, reduce)

🧱 Refactoring orienté objet
* Encapsulate Field – passer les attributs privés et exposer via getters/setters
* Encapsulate Collection – ne jamais exposer une collection directement
* Introduce Parameter Object – regrouper plusieurs paramètres qui vont ensemble
* Extract Interface / Abstract Class – isoler des comportements génériques
* Push Down / Pull Up Method / Field – déplacer dans la hiérarchie de classes
* Replace Inheritance with Delegation – quand la relation “est-un” ne tient pas
* Replace Delegation with Inheritance – si la délégation est trop verbeuse

🧪 Refactoring des tests
* Rename Test for Behavior – nommer le test selon la règle métier
* Extract Test Helper – factoriser les répétitions
* Remove Redundant Assertion – ne garder que les vérifications utiles
* Use Given-When-Then structure – rendre le test narratif
* Replace Hardcoded Data with Fixture / Factory
* Mock only what you own – ne pas moquer les détails d’implémentation
* Parameterize Tests – réduire la duplication de scénarios

🧭 Refactoring architectural
* Modularize – découper en modules indépendants
* Extract Component / Service / Domain – isoler une partie logique (DDD)
* Introduce Layer – ajouter une couche pour séparer responsabilités
* Move Responsibility to Appropriate Layer – respecter le principe Separation of Concerns
* Introduce Event / Message / Observer – découpler les dépendances fortes
* Replace Static with Dependency Injection – rendre le code testable et extensible

🗃️ Refactoring de données
* Change Value to Reference / Reference to Value – ajuster la nature des objets métier
* Encapsulate Record – cacher la structure interne d’un enregistrement
* Replace Data Value with Object – donner du comportement à une donnée brute
* Replace Type Code with Class / Subclass – transformer un champ “type” en polymorphisme
* Replace Array with Object – clarifier la structure
* Rename Field / Split Table / Merge Table – (refactoring de schéma côté persistance)

⚙️ Refactoring de performances (à faire après les autres)
* Cache Calculation – mémoriser des résultats coûteux
* Lazy Initialization – retarder les calculs inutiles
* Inline Hot Path – supprimer les appels de fonctions sur les chemins critiques
* Reduce Algorithmic Complexity – changer d’approche algorithmique
* Move Expensive Operation Out of Loop


🧭 En TDD : les 3 lois d’or du refactoring
	1.	Faites-le après un test vert ✅ → Toujours sur du code stable.
	2.	Petites étapes 👣 → Une micro-modif, un test, commit.
	3.	Toujours couvert par les tests 🛡️ → Sinon, vous changez le comportement sans le savoir.

🧰 Ressources de référence
* [Refactoring: Improving the Design of Existing Code (édition 2, 2018) - Martin Fowler](https://amzn.to/4n2oPZM)
* [Test-Driven Development: By Example - Kent Beck](https://amzn.to/4nHGiHQ)
* [Clean Code en Python: Principes, patterns et pratiques pour les développeurs professionnels - Martin Glovva](https://amzn.to/4ocCwpW)
* [Working Effectively with Legacy Code - Michael Feathers](https://amzn.to/48GMFqz)
* [Software craft: TDD, Clean Code et autres pratiques essentielle - Cyrille Martraire, Arnaud Thiéfaine, Dorra Bartaguiz, Fabien Hiegel, Houssam Fakih](https://amzn.to/48mMAbe)

### Exercice 8 : Refactoriser le code

1. Identifier 5 types de rafactoring, que vous pouvez mettre en oeuvre facilement
2. Metter en place au moins 5 refactoring différents

***Tips*** : toujours modifier un test ou le code mais jamais les deux en même temps, ne pas oublier de relancer les testes après chaque modification

## Thème TDD - BDD - Techniques Avancés

> Objectif principal : Découvrir le cycle de developpement Behavior Driven Development et ATDD
> Objectif secondaire : Usage du langage Gherkin et de la librairie "Behave" et des 3 amigo (dev, QA, Non tech et parties prenantes du projets)

référence : 
- Behave : https://behave.readthedocs.io/en/stable/
- Behave-Django : https://behave-django.readthedocs.io/en/latest/index.html 
- Selenium : https://www.selenium.dev/documentation/
- Django-Selenium : https://django-selenium.readthedocs.io/en/latest/ et https://docs.djangoproject.com/fr/5.2/topics/testing/tools/
- Robot Framework : https://docs.robotframework.org/

### Exercice 9 : Mise en place d'une nouvelle fonctionnalité (phase 1 - Backend / service)

Mise en place du nouveau type de produit dans le catalogue : 

Nous avons récemment signé un partenariat avec un fournisseur de produit invoqué ("Conjured").
Cela nécessite une mise à jour de notre système :

- les éléments "Conjured" voient leur qualité se dégrader de deux fois plus vite que les objets normaux.

Juste une précision, un produit ne peut jamais voir sa qualité augmenter au-dessus de 50, cependant "Sulfuras" est un objet légendaire et comme tel sa qualité est de 80 et elle ne change jamais.

Dans cette exercice, on s'occupe uniquement de la mise à jour du service 'updateQuality' pour introduire cette nouvelle fonctionnalité de notre shop en ligne.

***Contraintes*** : 
Usage de Behave 
Si pas installer : 
> pip install behave
> behave -version 
> pip install behave-django

Pour vous aider, un exemple d'usage a été mis en place dans le répertoire tests.
pour lancer le test : 

	python manage.py behave tests/features

### Exercice 10 : Mise en place d'une nouvelle fonctionnalité (phase 2 - test de l'interface)

tester la mise a jour sur l'action de mettre à jour de UpdateQuality dans l'interface de l'admin.

***Contraintes*** : 
Usage de Selenium (Extension Django) 

	pip install django-selenium

### Exercice 11 : 
Mettre en place une fonctionnalité de gestion pour supprimer les articles périmés.

Commencer par les tests.

Note : Une page robot exemple est à disposition : tests/robot/shop_admin_customers.robot

CMD : robot tests/robot/shop_admin_customers.robot


***Contraintes*** :
Usage de Robot Framework 

	pip install robotframework robotframework-seleniumlibrary 

Autres framework BDD : 
- https://lettuce.readthedocs.io/en/latest/tutorial/simple.html


### Exercice 12 : Integration continue (optionnel)

Objectif : Mettre en place un pipe de compilation à chaque modification

1. Configurer votre git (ou github) (tuto : https://editions-celine-et-nico.com/fork-et-rebase-dun-projet-git/)
2. configurer un pipe jenkins pour lancer tous les tests écrits jusqu'à maintenant.
3. Ajuster le pipe pour déployer dans les containers Docker
