from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import datetime

from app.models.noticia_model import NoticiaModel


class NoticiaController:

    @staticmethod
    def listar():

        noticias = NoticiaModel.obtener_todas()

        return render_template(
            "dashboard/noticias/index.html",
            noticias=noticias
        )

    @staticmethod
    def mostrar_crear():

        return render_template(
            "dashboard/noticias/crear.html"
        )

    @staticmethod
    def guardar():

        titulo = request.form.get("titulo")
        resumen = request.form.get("resumen")
        contenido = request.form.get("contenido")
        estado = request.form.get("estado")

        imagen = request.files.get("imagen")

        nombre_imagen = None

        # Guardar imagen
        if imagen and imagen.filename != "":

            nombre_imagen = (
                f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{imagen.filename}"
            )

            ruta_imagen = (
                f"app/static/uploads/noticias/{nombre_imagen}"
            )

            imagen.save(ruta_imagen)

        usuario_id = session["usuario_id"]

        NoticiaModel.guardar(
            usuario_id,
            titulo,
            resumen,
            contenido,
            estado,
            nombre_imagen
        )

        flash(
            "Noticia creada correctamente.",
            "success"
        )

        return redirect(url_for("noticia.listar"))

    @staticmethod
    def editar(id):
        """
        Muestra el formulario para editar una noticia.
        """

        noticia = NoticiaModel.obtener_por_id(id)

        if not noticia:
            return redirect(url_for("noticia.listar"))

        return render_template(
            "dashboard/noticias/editar.html",
            noticia=noticia
        )

    @staticmethod
    def actualizar(id):
        """
        Actualiza una noticia.
        """

        titulo = request.form.get("titulo")
        resumen = request.form.get("resumen")
        contenido = request.form.get("contenido")
        estado = request.form.get("estado")

        NoticiaModel.actualizar(
            id,
            titulo,
            resumen,
            contenido,
            estado
        )

        flash(
            "Noticia actualizada correctamente.",
            "success"
        )

        return redirect(url_for("noticia.listar"))

    @staticmethod
    def eliminar(id):
        """
        Elimina una noticia.
        """

        NoticiaModel.eliminar(id)

        flash(
            "Noticia eliminada correctamente.",
            "success"
        )

        return redirect(
            url_for("noticia.listar")
        )