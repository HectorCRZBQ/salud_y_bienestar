from flask import Blueprint, request, jsonify
from src.models.contact import User
from src.models.register import Register


user_bp = Blueprint('user', __name__)

@user_bp.route("/api/users/contact", methods=["GET", "POST"])
def create_user():
    if request.method == "POST":
        data = request.get_json()
        nombre = data.get("name")  # Cambiado para coincidir con el frontend
        email = data.get("email")
        mensaje = data.get("message")  # Cambiado para coincidir con el frontend

        # Validación de campos
        if not all([nombre, email, mensaje]):
            return jsonify({"error": "Todos los campos son obligatorios"}), 400

        # Llamada al modelo para insertar el usuario
        response = User.create_user(nombre, email, mensaje)
        return jsonify(response)

    # Para método GET (opcional, si quisieras devolver algo)
    return jsonify({"message": "Método no soportado"}), 405

@user_bp.route("/api/users/register", methods=["GET", "POST"])
def register_user():
    data = request.get_json()
    usuario = data.get("email")
    contrasena = data.get("password")

    # Validación de campos
    if not all([usuario, contrasena]):
        return jsonify({"error": "Todos los campos son obligatorios"}), 400

    # Llamada al modelo para registrar el usuario
    response = Register.create_user(usuario, contrasena)
    return jsonify(response)
