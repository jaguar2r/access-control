from pymongo import MongoClient
from app.config.config import Config

# Função para conectar ao banco de dados MongoDB
def get_db():
    client = MongoClient(Config.MONGO_URI)
    db = client.auth_db
    return db

db = get_db()
