from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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