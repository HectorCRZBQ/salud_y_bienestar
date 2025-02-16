from src.database.database import get_connection

class User:
    @staticmethod
    def create_table():
        """Crea la tabla usuarios_atencion si no existe."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_atencion (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100),
                email VARCHAR(100),
                mensaje TEXT
            )
            """)
            connection.commit()
            cursor.close()
            connection.close()
            print("Tabla 'usuarios_atencion' creada o ya existe.")
        except Exception as e:
            print(f"Error al crear la tabla 'usuarios_atencion': {e}")

    @staticmethod
    def create_user(nombre, email, mensaje):
        """Inserta un nuevo usuario en la tabla."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = """
            INSERT INTO usuarios_atencion (nombre, email, mensaje)
            VALUES (%s, %s, %s)
            """
            cursor.execute(query, (nombre, email, mensaje))
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "Usuario creado exitosamente"}
        except Exception as e:
            # Devuelve el error para fines de depuración
            return {"error": f"Error al insertar usuario: {e}"}
