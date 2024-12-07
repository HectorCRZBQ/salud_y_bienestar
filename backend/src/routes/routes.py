from flask import Blueprint, request, jsonify
from src.models.contact import User

user_bp = Blueprint('user', __name__)

@user_bp.route("/api/users/contact", methods=["GET","POST"])
def create_user():
    data = request.get_json()
    nombre = data.get("name")  # Changed from "nombre" to match frontend
    email = data.get("email")
    mensaje = data.get("message")  # Changed from "mensaje" to match frontend
    
    if not all([nombre, email, mensaje]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400
    
    response = User.create_user(nombre, email, mensaje)
    return jsonify(response)
