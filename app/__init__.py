from flask import Flask
from .routes import routes

def create_app():
    app = Flask(__name__)
    
    # Registrar el Blueprint con las rutas
    app.register_blueprint(routes)
    
    return app
