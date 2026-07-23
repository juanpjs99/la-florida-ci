from app.database.db import mysql
from MySQLdb.cursors import DictCursor


class EventoModel:

    @staticmethod
    def obtener_todos():
        """
        Obtiene todos los eventos.
        """

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT
                e.id,
                e.titulo,
                e.descripcion,
                e.imagen,
                e.lugar,
                e.fecha_evento,
                e.hora_evento,
                e.estado,
                e.created_at,
                CONCAT(u.nombres, ' ', u.apellidos) AS autor
            FROM eventos e
            INNER JOIN usuarios u
                ON e.usuario_id = u.id
            ORDER BY e.created_at DESC
        """

        cursor.execute(query)

        eventos = cursor.fetchall()

        cursor.close()

        return eventos

    @staticmethod
    def contar():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM eventos")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    @staticmethod
    def guardar(
        usuario_id,
        titulo,
        descripcion,
        imagen,
        lugar,
        fecha_evento,
        hora_evento,
        estado
    ):
        """
        Guarda un nuevo evento.
        """

        cursor = mysql.connection.cursor()

        query = """
            INSERT INTO eventos
            (
                usuario_id,
                titulo,
                descripcion,
                imagen,
                lugar,
                fecha_evento,
                hora_evento,
                estado
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                %s
            )
        """

        cursor.execute(
            query,
            (
                usuario_id,
                titulo,
                descripcion,
                imagen,
                lugar,
                fecha_evento,
                hora_evento,
                estado
            )
        )

        mysql.connection.commit()

        cursor.close()

    @staticmethod
    def obtener_por_id(id):
        """
        Obtiene un evento por su ID.
        """

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT *
            FROM eventos
            WHERE id = %s
        """

        cursor.execute(query, (id,))

        evento = cursor.fetchone()

        cursor.close()

        return evento

    @staticmethod
    def actualizar(
        id,
        titulo,
        descripcion,
        imagen,
        lugar,
        fecha_evento,
        hora_evento,
        estado
    ):
        """
        Actualiza un evento.
        """

        cursor = mysql.connection.cursor()

        query = """
            UPDATE eventos
            SET
                titulo=%s,
                descripcion=%s,
                imagen=%s,
                lugar=%s,
                fecha_evento=%s,
                hora_evento=%s,
                estado=%s
            WHERE id=%s
        """

        cursor.execute(
            query,
            (
                titulo,
                descripcion,
                imagen,
                lugar,
                fecha_evento,
                hora_evento,
                estado,
                id
            )
        )

        mysql.connection.commit()

        cursor.close()

    @staticmethod
    def eliminar(id):
        """
        Elimina un evento.
        """

        cursor = mysql.connection.cursor()

        query = """
            DELETE FROM eventos
            WHERE id = %s
        """

        cursor.execute(query, (id,))

        mysql.connection.commit()

        cursor.close()