
0. Les commandes docker à lancer pour initier son environnement de dev

La Stack VueJS, FastAPI, MongoDB 
   
    docker compose up -d --force-recreate db db-ui
    docker compose up --watch api ui

La Stack Django, Postgresql 
    
    docker compose up -d --force-recreate db db-ui
    docker compose up --watch 
    
    python manage.py migrate
    python manage.py createsuperuser --username=admin --email=admin@example.com

ATTENTION n'oubliez de définir un mot de passe (ex : admin)


Lien vers les repos qui ont servi à construire les exercices : 
1. GildedRose Refactoring Kata
https://github.com/emilybache/GildedRose-Refactoring-Kata/tree/main

2. Docker et Vue.js : https://github.com/kristiyan-velkov/docker-vuejs-sample
et https://docs.docker.com/guides/vuejs/

3. Docker et Django : https://www.docker.com/blog/how-to-dockerize-django-app/

