from flask import Flask
from models.contact import User
from routes.routes import user_bp

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'your_secret_key'

    # Crear tablas a través de los modelos
    User.create_table()

    # Registrar rutas
    app.register_blueprint(user_bp, url_prefix="/api/users")
    
    return app
