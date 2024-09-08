from flask import Blueprint, request, jsonify, current_app
from werkzeug.security import generate_password_hash, check_password_hash
from app.models.user import User
from app.views.auth_view import render_success, render_error
import jwt
import datetime
from app.config.database import db

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return render_error('Email e senha são obrigatórios', 400)

    if User.find_by_email(db, email):
        return render_error('Usuário já existe', 400)

    hashed_password = generate_password_hash(password)
    user = User(email=email, password=hashed_password)
    User.insert_user(db, user)

    return render_success('Usuário cadastrado com sucesso', 201)

@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    user = User.find_by_email(db, email)

    if not user or not check_password_hash(user['password'], password):
        return render_error('Email ou senha inválidos', 401)

    token = jwt.encode({
        'user_id': str(user['_id']),
        'exp': datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(minutes=15)
        }, current_app.config['SECRET_KEY'], algorithm='HS256')

    return render_success({'token': token}, 200)
