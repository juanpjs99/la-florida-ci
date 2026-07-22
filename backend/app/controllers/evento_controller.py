from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    flash
)

import datetime

from app.models.evento_model import EventoModel


class EventoController:

    @staticmethod
    def listar():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        eventos = EventoModel.obtener_todos()

        return render_template(
            "dashboard/eventos/index.html",
            eventos=eventos
        )

    @staticmethod
    def mostrar_crear():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        return render_template(
            "dashboard/eventos/crear.html"
        )

    @staticmethod
    def guardar():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        titulo = request.form.get("titulo")
        descripcion = request.form.get("descripcion")
        lugar = request.form.get("lugar")
        fecha_evento = request.form.get("fecha_evento")
        hora_evento = request.form.get("hora_evento")
        estado = request.form.get("estado")

        imagen = request.files.get("imagen")

        nombre_imagen = None

        if imagen and imagen.filename != "":

            nombre_imagen = (
                f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{imagen.filename}"
            )

            ruta_imagen = (
                f"app/static/uploads/eventos/{nombre_imagen}"
            )

            imagen.save(ruta_imagen)

        usuario_id = session["usuario_id"]

        EventoModel.guardar(
            usuario_id,
            titulo,
            descripcion,
            nombre_imagen,
            lugar,
            fecha_evento,
            hora_evento,
            estado
        )

        flash(
            "Evento creado correctamente.",
            "success"
        )

        return redirect(
            url_for("evento.listar")
        )

    @staticmethod
    def editar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        evento = EventoModel.obtener_por_id(id)

        if not evento:
            flash("El evento no existe.", "warning")
            return redirect(url_for("evento.listar"))

        return render_template(
            "dashboard/eventos/editar.html",
            evento=evento
        )

    @staticmethod
    def actualizar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        titulo = request.form.get("titulo")
        descripcion = request.form.get("descripcion")
        lugar = request.form.get("lugar")
        fecha_evento = request.form.get("fecha_evento")
        hora_evento = request.form.get("hora_evento")
        estado = request.form.get("estado")

        imagen = request.files.get("imagen")

        nombre_imagen = request.form.get("imagen_actual")

        if imagen and imagen.filename != "":

            nombre_imagen = (
                f"{datetime.datetime.now().strftime('%Y%m%d%H%M%S')}_{imagen.filename}"
            )

            ruta_imagen = (
                f"app/static/uploads/eventos/{nombre_imagen}"
            )

            imagen.save(ruta_imagen)

        EventoModel.actualizar(
            id,
            titulo,
            descripcion,
            nombre_imagen,
            lugar,
            fecha_evento,
            hora_evento,
            estado
        )

        flash(
            "Evento actualizado correctamente.",
            "success"
        )

        return redirect(
            url_for("evento.listar")
        )

    @staticmethod
    def eliminar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        EventoModel.eliminar(id)

        flash(
            "Evento eliminado correctamente.",
            "success"
        )

        return redirect(
            url_for("evento.listar")
        )