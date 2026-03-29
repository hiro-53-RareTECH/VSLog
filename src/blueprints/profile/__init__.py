from flask import Blueprint

profile_bp = Blueprint('profile', __name__)

from .routes import password_update, profile_edit
