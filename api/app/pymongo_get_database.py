from pymongo import MongoClient

# Fournissez l'url mongodb atlas pour connecter python à mongodb à l'aide de pymongo
# cas d'atlas et cluster : CHAINE_DE_CONNEXION = "mongodb+srv://init-mongo.js:pass@cluster.mongodb.net/myFirstDatabase"
#URL_MONGO_DB = "mongodb://dev:passdev@localhost:27017/?tls=false"
import os


URL_MONGO_DB = os.getenv("MONGO_URL", "mongodb://dev:passdev@localhost:27017")


def get_database() :

    # Créez une connexion à l'aide de MongoClient. Vous pouvez importer MongoClient ou utiliser pymongo.MongoClient
    try :
        return MongoClient(URL_MONGO_DB).get_database(name="gilderose")
    except (RuntimeError, ConnectionError):
        print("Error connecting to database")
        raise