from flask import Blueprint

from app.controllers.galeria_imagen_controller import GaleriaImagenController


galeria_imagen_bp = Blueprint(

    "galeria_imagen",
    __name__

)


@galeria_imagen_bp.route(
    "/dashboard/galerias/<int:galeria_id>/imagenes"
)
def listar(galeria_id):

    return GaleriaImagenController.listar(galeria_id)


@galeria_imagen_bp.route(
    "/dashboard/galerias/<int:galeria_id>/imagenes/subir",
    methods=["POST"]
)
def subir(galeria_id):

    return GaleriaImagenController.subir(galeria_id)


@galeria_imagen_bp.route(
    "/dashboard/galerias/imagenes/eliminar/<int:id>"
)
def eliminar(id):

    return GaleriaImagenController.eliminar(id)