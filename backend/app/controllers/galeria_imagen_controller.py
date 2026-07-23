import os
import uuid

from flask import (
    render_template,
    request,
    redirect,
    url_for,
    flash,
    current_app
)

from werkzeug.utils import secure_filename

from app.models.galeria_model import GaleriaModel
from app.models.galeria_imagen_model import GaleriaImagenModel


class GaleriaImagenController:

    @staticmethod
    def listar(galeria_id):

        galeria = GaleriaModel.obtener_por_id(galeria_id)

        if not galeria:

            flash("La galería no existe.", "danger")
            return redirect(url_for("galeria.listar"))

        imagenes = GaleriaImagenModel.obtener_por_galeria(galeria_id)

        return render_template(

            "dashboard/galerias/imagenes/listar.html",

            galeria=galeria,

            imagenes=imagenes

        )

    @staticmethod
    def subir(galeria_id):

        archivos = request.files.getlist("imagenes")

        carpeta = os.path.join(
            current_app.static_folder,
            "uploads",
            "galeria_imagenes"
        )

        os.makedirs(carpeta, exist_ok=True)

        for archivo in archivos:

            if archivo and archivo.filename != "":

                extension = os.path.splitext(
                    secure_filename(archivo.filename)
                )[1]

                nombre = f"{uuid.uuid4().hex}{extension}"

                archivo.save(os.path.join(carpeta, nombre))

                GaleriaImagenModel.crear({

                    "galeria_id": galeria_id,
                    "ruta_imagen": nombre,
                    "descripcion": None,
                    "orden": 1

                })

        flash("Imágenes cargadas correctamente.", "success")

        return redirect(
            url_for(
                "galeria_imagen.listar",
                galeria_id=galeria_id
            )
        )

    @staticmethod
    def eliminar(id):

        imagen = GaleriaImagenModel.obtener_por_id(id)

        if not imagen:

            flash("La imagen no existe.", "danger")
            return redirect(url_for("galeria.listar"))

        ruta = os.path.join(

            current_app.static_folder,

            "uploads",

            "galeria_imagenes",

            imagen["ruta_imagen"]

        )

        if os.path.exists(ruta):

            os.remove(ruta)

        galeria_id = imagen["galeria_id"]

        GaleriaImagenModel.eliminar(id)

        flash("Imagen eliminada correctamente.", "success")

        return redirect(

            url_for(

                "galeria_imagen.listar",

                galeria_id=galeria_id

            )

        )