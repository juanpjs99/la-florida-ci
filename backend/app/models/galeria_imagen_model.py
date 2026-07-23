import MySQLdb.cursors

from app.database.db import mysql
from app.database.db import mysql
from MySQLdb.cursors import DictCursor


class GaleriaImagenModel:

    @staticmethod
    def obtener_por_galeria(galeria_id):

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            SELECT
                id,
                galeria_id,
                ruta_imagen,
                descripcion,
                orden,
                created_at
            FROM galeria_imagenes
            WHERE galeria_id = %s
            ORDER BY orden ASC, id ASC
        """

        cursor.execute(sql, (galeria_id,))
        imagenes = cursor.fetchall()

        cursor.close()

        return imagenes

    @staticmethod
    def crear(data):

        cursor = mysql.connection.cursor()

        sql = """
            INSERT INTO galeria_imagenes
            (
                galeria_id,
                ruta_imagen,
                descripcion,
                orden
            )
            VALUES
            (%s, %s, %s, %s)
        """

        cursor.execute(sql, (

            data["galeria_id"],
            data["ruta_imagen"],
            data["descripcion"],
            data["orden"]

        ))

        mysql.connection.commit()

        cursor.close()

    @staticmethod
    def obtener_por_id(id):

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        sql = """
            SELECT *
            FROM galeria_imagenes
            WHERE id = %s
        """

        cursor.execute(sql, (id,))

        imagen = cursor.fetchone()

        cursor.close()

        return imagen

    @staticmethod
    def eliminar(id):

        cursor = mysql.connection.cursor()

        sql = """
            DELETE
            FROM galeria_imagenes
            WHERE id = %s
        """

        cursor.execute(sql, (id,))

        mysql.connection.commit()

        cursor.close()


    # ==========================================================
# PORTAL WEB
# ==========================================================

    @staticmethod
    def obtener_publicas_por_galeria(galeria_id):

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT
                id,
                ruta_imagen,
                descripcion,
                orden
            FROM galeria_imagenes
            WHERE galeria_id = %s
            ORDER BY orden ASC, created_at ASC
        """

        cursor.execute(query, (galeria_id,))

        imagenes = cursor.fetchall()

        cursor.close()

        return imagenes

    @staticmethod
    def obtener_por_galeria(galeria_id):

        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)

        cursor.execute("""
            SELECT
                id,
                ruta_imagen,
                descripcion,
                orden
            FROM galeria_imagenes
            WHERE galeria_id = %s
            ORDER BY orden ASC, id ASC
        """, (galeria_id,))

        imagenes = cursor.fetchall()

        cursor.close()

        return imagenes