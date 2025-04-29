"""
    Turn this routes folder to a Package
"""

from .user_routes import user_bp
from .home_routes import home_bp
from .recipe_routes import recipe_bp
from .error_routes import error_bp


bluprints = [user_bp, home_bp, recipe_bp, error_bp]