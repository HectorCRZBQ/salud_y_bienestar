import mysql.connector
from config import Config

db_config = {
    'host': Config.DB_HOST,
    'user': Config.DB_USER,
    'password': Config.DB_PASSWORD,
    'database': Config.DB_NAME,
    'port': Config.DB_PORT
}

def get_connection():
    """Devuelve una conexión a la base de datos."""
    return mysql.connector.connect(**db_config)
