import os

class Config:
    SECRET_KEY = os.getenv("SECRET_KEY", "minha_secreta")
    MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/auth_db")
