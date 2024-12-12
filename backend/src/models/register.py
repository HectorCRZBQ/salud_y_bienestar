from src.database.database import get_connection

class Register:
    @staticmethod
    def create_table():
        """Crea la tabla usuarios_registro si no existe."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios_registro (
                id INT AUTO_INCREMENT PRIMARY KEY,
                usuario VARCHAR(100) NOT NULL,
                contrasena VARCHAR(255) NOT NULL
            )
            """)
            connection.commit()
            cursor.close()
            connection.close()
            print("Tabla 'registro' creada o ya existe.")
        except Exception as e:
            print(f"Error al crear la tabla 'usuarios_registro': {e}")

    @staticmethod
    def create_user(usuario, contrasena):
        """Inserta un nuevo usuario en la tabla usuarios_registro."""
        try:
            connection = get_connection()
            cursor = connection.cursor()
            query = """
            INSERT INTO usuarios_registro (usuario, contrasena)
            VALUES (%s, %s)
            """
            cursor.execute(query, (usuario, contrasena))
            connection.commit()
            cursor.close()
            connection.close()
            return {"message": "Usuario creado exitosamente"}
        except Exception as e:
            # Devuelve el error para fines de depuración
            return {"error": f"Error al insertar usuario: {e}"}
