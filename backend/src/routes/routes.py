from flask import Blueprint, request, jsonify
from src.models.contact import User

user_bp = Blueprint('user', __name__)

@user_bp.route("/", methods=["GET","POST"])
def create_user():
    data = request.get_json()
    nombre = data.get("nombre")
    email = data.get("email")
    categoria = data.get("categoria")
    prioridad = data.get("prioridad")
    mensaje = data.get("mensaje")
    
    if not all([nombre, email, categoria, prioridad, mensaje]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    response = User.create_user(nombre, email, categoria, prioridad, mensaje)
    return jsonify(response)
