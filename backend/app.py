from flask import Flask, request, redirect
from prometheus_flask_exporter import PrometheusMetrics
import mysql.connector

app = Flask(__name__)

# Integración con Prometheus
metrics = PrometheusMetrics(app)
metrics.info('app_info', 'Formulario Flask con monitorización', version='1.0.0')

# Configuración de la base de datos
db_config = {
    'host': 'db',
    'user': 'empresa_user',
    'password': 'userpassword',
    'database': 'empresa_db'
}

def init_db():
    """Inicializar la base de datos y crear la tabla si no existe."""
    try:
        connection = mysql.connector.connect(**db_config)
        cursor = connection.cursor()

        # Crear tabla usuarios si no existe
        cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuarios (
            id INT AUTO_INCREMENT PRIMARY KEY,
            nombre VARCHAR(100),
            apellidos VARCHAR(100),
            email VARCHAR(100)
        )
        """)

        connection.commit()
        cursor.close()
        connection.close()
        print("Base de datos inicializada correctamente")
    except mysql.connector.Error as err:
        print(f"Error al inicializar la base de datos: {err}")

@app.route("/", methods=["GET", "POST"])
def form():
    """Formulario de ingreso y procesamiento de datos."""
    if request.method == "POST":
        # Obtener los datos del formulario
        nombre = request.form["nombre"]
        apellidos = request.form["apellidos"]
        email = request.form["email"]

        # Imprimir los datos en los logs para asegurarnos de que se están recibiendo correctamente
        print(f"Datos recibidos: nombre={nombre}, apellidos={apellidos}, email={email}")

        # Guardar en la base de datos
        try:
            connection = mysql.connector.connect(**db_config)
            cursor = connection.cursor()
            cursor.execute("INSERT INTO usuarios (nombre, apellidos, email) VALUES (%s, %s, %s)",
                           (nombre, apellidos, email))
            connection.commit()
            cursor.close()
            connection.close()
            print("Datos insertados correctamente en la base de datos")
        except mysql.connector.Error as err:
            print(f"Error al insertar datos: {err}")
            return "Error al guardar los datos en la base de datos", 500

        # Redirigir al usuario de vuelta al formulario para un nuevo ingreso
        return redirect("/")
    


if __name__ == "__main__":
    init_db()  # Inicializa la base de datos al arrancar
    app.run(host="0.0.0.0", port=5000)
