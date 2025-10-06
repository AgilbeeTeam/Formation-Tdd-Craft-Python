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

