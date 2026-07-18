from app.database.db import mysql
from MySQLdb.cursors import DictCursor


class UsuarioModel:

    @staticmethod
    def obtener_por_correo(correo):
        """
        Busca un usuario por su correo electrónico.
        """

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT
                u.id,
                u.rol_id,
                r.nombre AS rol,
                u.nombres,
                u.apellidos,
                u.correo,
                u.password,
                u.telefono,
                u.estado
            FROM usuarios u
            INNER JOIN roles r
                ON u.rol_id = r.id
            WHERE u.correo = %s
            LIMIT 1
        """

        cursor.execute(query, (correo,))

        usuario = cursor.fetchone()

        cursor.close()

        return usuario

    @staticmethod
    def actualizar_ultimo_acceso(usuario_id):
        """
        Actualiza la fecha y hora del último acceso.
        """

        cursor = mysql.connection.cursor()

        query = """
            UPDATE usuarios
            SET ultimo_acceso = NOW()
            WHERE id = %s
        """

        cursor.execute(query, (usuario_id,))

        mysql.connection.commit()

        cursor.close()