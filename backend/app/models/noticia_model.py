from app.database.db import mysql
from MySQLdb.cursors import DictCursor


class NoticiaModel:

    @staticmethod
    def obtener_todas():
        """
        Obtiene todas las noticias.
        """

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT
                n.id,
                n.titulo,
                n.resumen,
                n.imagen,
                n.estado,
                n.fecha_publicacion,
                n.created_at,
                CONCAT(u.nombres, ' ', u.apellidos) AS autor
            FROM noticias n
            INNER JOIN usuarios u
                ON n.usuario_id = u.id
            ORDER BY n.created_at DESC
        """

        cursor.execute(query)

        noticias = cursor.fetchall()

        cursor.close()

        return noticias

    @staticmethod
    def contar():
        cursor = mysql.connection.cursor()
        cursor.execute("SELECT COUNT(*) FROM noticias")
        count = cursor.fetchone()[0]
        cursor.close()
        return count


    @staticmethod
    def guardar(
        usuario_id,
        titulo,
        resumen,
        contenido,
        estado,
        imagen
    ):
        """
        Guarda una nueva noticia.
        """

        cursor = mysql.connection.cursor()

        query = """
            INSERT INTO noticias
            (
                usuario_id,
                titulo,
                resumen,
                contenido,
                imagen,
                estado,
                fecha_publicacion
            )
            VALUES
            (
                %s,
                %s,
                %s,
                %s,
                %s,
                %s,
                NOW()
            )
        """

        cursor.execute(
            query,
            (
                usuario_id,
                titulo,
                resumen,
                contenido,
                imagen,
                estado
            )
        )

        mysql.connection.commit()
        cursor.close()
    

    @staticmethod
    def obtener_por_id(noticia_id):
        """
        Obtiene una noticia por su ID.
        """

        cursor = mysql.connection.cursor(DictCursor)

        query = """
            SELECT
                n.id,
                n.titulo,
                n.resumen,
                n.contenido,
                n.estado,
                n.fecha_publicacion,
                n.created_at,
                CONCAT(u.nombres, ' ', u.apellidos) AS autor
            FROM noticias n
            INNER JOIN usuarios u
                ON n.usuario_id = u.id
            WHERE n.id = %s
            LIMIT 1
        """

        cursor.execute(query, (noticia_id,))

        noticia = cursor.fetchone()

        cursor.close()

        return noticia
    
    ##################33

    @staticmethod
    def actualizar(
        noticia_id,
        titulo,
        resumen,
        contenido,
        estado
    ):
        """
        Actualiza una noticia.
        """

        cursor = mysql.connection.cursor()

        query = """
            UPDATE noticias
            SET
                titulo = %s,
                resumen = %s,
                contenido = %s,
                estado = %s,
                updated_at = NOW()
            WHERE id = %s
        """

        cursor.execute(
            query,
            (
                titulo,
                resumen,
                contenido,
                estado,
                noticia_id
            )
        )

        mysql.connection.commit()

        cursor.close()

    ## modelo de eliminar noticia
    @staticmethod
    def eliminar(noticia_id):
        """
        Elimina una noticia.
        """

        cursor = mysql.connection.cursor()

        query = """
            DELETE FROM noticias
            WHERE id = %s
        """

        cursor.execute(query, (noticia_id,))

        mysql.connection.commit()

        cursor.close()  