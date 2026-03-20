from flask import Blueprint

error_bp = Blueprint('error', __name__)

from .routes import error_403, error_404, error_500