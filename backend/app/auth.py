from flask import Blueprint, request, jsonify
from flask_login import login_user, logout_user, login_required
from . import db, bcrypt
from .models import User

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    email = data.get('email')
    password = data.get('password')
    remember = True if data.get('rember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not bcrypt.check_password_hash(user.password, password):
        return jsonify({'error': 'Invalid data'}), 401
    
    login_user(user, remember=remember)

    return jsonify({
        'success': True,
        'user' : {
            'id': user.id,
            'email': user.email,
            'name': user.name
        }
    }), 200
