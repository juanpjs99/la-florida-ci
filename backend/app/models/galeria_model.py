from app.database.db import mysql
import MySQLdb.cursors


class GaleriaModel:

    @staticmethod
    def obtener_todas():
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            SELECT
                g.id,
                g.titulo,
                g.descripcion,
                g.portada,
                g.estado,
                g.created_at,
                CONCAT(u.nombres, ' ', u.apellidos) AS usuario
            FROM galerias g
            INNER JOIN usuarios u
                ON g.usuario_id = u.id
            ORDER BY g.created_at DESC
        """

        cursor.execute(sql)
        galerias = cursor.fetchall()
        cursor.close()

        return galerias

    @staticmethod
    def contar():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM galerias")
        count = cursor.fetchone()[0]
        cursor.close()
        return count

    @staticmethod
    def obtener_por_id(id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            SELECT *
            FROM galerias
            WHERE id = %s
        """

        cursor.execute(sql, (id,))
        galeria = cursor.fetchone()
        cursor.close()

        return galeria

    @staticmethod
    def crear(data):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            INSERT INTO galerias
            (
                usuario_id,
                titulo,
                descripcion,
                portada,
                estado
            )
            VALUES
            (%s, %s, %s, %s, %s)
        """

        cursor.execute(sql, (
            data["usuario_id"],
            data["titulo"],
            data["descripcion"],
            data["portada"],
            data["estado"]
        ))

        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def actualizar(id, data):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            UPDATE galerias
            SET
                titulo = %s,
                descripcion = %s,
                portada = %s,
                estado = %s
            WHERE id = %s
        """

        cursor.execute(sql, (
            data["titulo"],
            data["descripcion"],
            data["portada"],
            data["estado"],
            id
        ))

        mysql.connection.commit()
        cursor.close()

    @staticmethod
    def eliminar(id):
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            DELETE FROM galerias
            WHERE id = %s
        """

        cursor.execute(sql, (id,))
        mysql.connection.commit()
        cursor.close()

    # ==========================================================
    # PORTAL WEB
    # ==========================================================

    @staticmethod
    def obtener_publicas(limit=6):
        """
        Obtiene las galerías activas para el portal web.
        """

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            SELECT
                id,
                titulo,
                descripcion,
                portada,
                created_at
            FROM galerias
            WHERE estado = 'ACTIVA'
            ORDER BY created_at DESC
            LIMIT %s
        """

        cursor.execute(sql, (limit,))

        galerias = cursor.fetchall()

        cursor.close()

        return galerias