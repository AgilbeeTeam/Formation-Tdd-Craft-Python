import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from pymongo_get_database import get_database

from gilded_rose import Item, GildedRose


app = FastAPI()


logger = logging.getLogger(__name__)

# Définir les origines autorisées (par exemple, localhost:3000 pour développement)
# @TODO : a externaliser pour que cela soit le Docker de prod qui prend en charge les autorisations.
origins = [
    "http://localhost",  # Frontend en développement
    "http://localhost:5173"  # Frontend en développement
    # Ajoutez d'autres origines si nécessaire
]

app.add_middleware(
    CORSMiddleware,
#    allow_origin_regex=r'http(?:s)?://(?:[^/]*.)?localhost(:\d+)?',
    allow_origins=origins,             # Ou ["*"] pour autoriser toutes les origines (moins sécurisé)
#    allow_origins=["*"],             # Ou ["*"] pour autoriser toutes les origines (moins sécurisé)
    allow_credentials=True,
    allow_methods=["*"],               # Autoriser toutes les méthodes HTTP -> GET uniquement ?
    allow_headers=["*"],               # Autoriser tous les en-têtes
)

@app.get("/")
def hello_world():
    return {"error": "Hello World"}

@app.get("/message")
def get_message():
    return {"message": "OK, le message provient de FastAPI -- reloaded ?!"}

@app.get("/items")
def lister_items():
    try :
        items = []
        for item in get_database().items.find({}) :
            logger.info("item : " + item)
            items.append(Item(name=item["name"], sell_in=item["sell_in"], quality=item["quality"]))

        return items

    except Exception as e:
        logger.error(e)
        raise e
