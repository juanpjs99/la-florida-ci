import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    session,
    current_app
)

from app.models.galeria_model import GaleriaModel


class GaleriaController:

    @staticmethod
    def listar():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        galerias = GaleriaModel.obtener_todas()

        return render_template(
            "dashboard/galerias/listar.html",
            galerias=galerias
        )

    @staticmethod
    def mostrar_crear():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        return render_template(
            "dashboard/galerias/crear.html"
        )

    @staticmethod
    def guardar():

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        portada = None

        archivo = request.files.get("portada")

        if archivo and archivo.filename != "":

            extension = archivo.filename.rsplit(".", 1)[1].lower()

            nombre_archivo = f"{uuid.uuid4().hex}.{extension}"

            ruta = os.path.join(
                current_app.static_folder,
                "uploads",
                "galerias"
            )

            os.makedirs(ruta, exist_ok=True)

            archivo.save(
                os.path.join(ruta, nombre_archivo)
            )

            portada = nombre_archivo

        data = {
            "usuario_id": session["usuario_id"],
            "titulo": request.form["titulo"],
            "descripcion": request.form["descripcion"],
            "portada": portada,
            "estado": request.form["estado"]
        }

        GaleriaModel.crear(data)

        return redirect(
            url_for("galeria.listar")
        )

    @staticmethod
    def editar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        galeria = GaleriaModel.obtener_por_id(id)

        return render_template(
            "dashboard/galerias/editar.html",
            galeria=galeria
        )

    @staticmethod
    def actualizar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        galeria = GaleriaModel.obtener_por_id(id)

        portada = galeria["portada"]

        archivo = request.files.get("portada")

        if archivo and archivo.filename != "":

            if portada:

                ruta_anterior = os.path.join(
                    current_app.static_folder,
                    "uploads",
                    "galerias",
                    portada
                )

                if os.path.exists(ruta_anterior):
                    os.remove(ruta_anterior)

            extension = archivo.filename.rsplit(".", 1)[1].lower()

            nombre_archivo = f"{uuid.uuid4().hex}.{extension}"

            ruta = os.path.join(
                current_app.static_folder,
                "uploads",
                "galerias"
            )

            os.makedirs(ruta, exist_ok=True)

            archivo.save(
                os.path.join(ruta, nombre_archivo)
            )

            portada = nombre_archivo

        data = {
            "titulo": request.form["titulo"],
            "descripcion": request.form["descripcion"],
            "portada": portada,
            "estado": request.form["estado"]
        }

        GaleriaModel.actualizar(id, data)

        return redirect(
            url_for("galeria.listar")
        )

    @staticmethod
    def eliminar(id):

        if "usuario_id" not in session:
            return redirect(url_for("auth.mostrar_login"))

        galeria = GaleriaModel.obtener_por_id(id)

        if galeria["portada"]:

            ruta = os.path.join(
                current_app.static_folder,
                "uploads",
                "galerias",
                galeria["portada"]
            )

            if os.path.exists(ruta):
                os.remove(ruta)

        GaleriaModel.eliminar(id)

        return redirect(
            url_for("galeria.listar")
        )