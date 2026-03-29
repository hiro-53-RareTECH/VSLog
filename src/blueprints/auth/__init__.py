from flask import Blueprint

auth_bp = Blueprint('auth', __name__)

from .routes import index, login, logout, password_reset, signup
