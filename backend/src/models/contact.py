from src.database.database import get_connection

class User:
    @staticmethod
    def create_table():
        """Crea la tabla usuarios si no existe."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100),
                categoria VARCHAR(50),
                prioridad VARCHAR(10),
                mensaje TEXT
            )
            """)
            connection.commit()
            cursor.close()
            connection.close()
            print("Tabla 'usuarios' creada o ya existe.")
        except Exception as e:
            print(f"Error al crear la tabla 'usuarios': {e}")

    @staticmethod
    def create_user(nombre, email, categoria, prioridad, mensaje):
        """Inserta un nuevo usuario en la tabla."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = """
            INSERT INTO usuarios (nombre, email, categoria, prioridad, mensaje)
            VALUES (%s, %s, %s, %s, %s)
            """
            cursor.execute(query, (nombre, email, categoria, prioridad, mensaje))
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "Usuario creado exitosamente"}
        except Exception as e:
            return {"error": str(e)}
