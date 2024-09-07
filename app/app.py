from flask import Flask
from app.config.config import Config
from pymongo import MongoClient
from app.controllers.auth_controller import auth_bp

app = Flask(__name__)
app.config.from_object(Config)

# Conexão com MongoDB
client = MongoClient(app.config["MONGO_URI"])
db = client.auth_db

# Registrando o Blueprint
app.register_blueprint(auth_bp, url_prefix='/auth')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
