from flask import Blueprint
from app.controllers.auth_controller import auth_bp

# Criando o blueprint que vai redirecionar as rotas
user_bp = Blueprint('user_routes', __name__)

# Registrando o blueprint de autenticação dentro das rotas de usuários
user_bp.register_blueprint(auth_bp, url_prefix='/auth')
