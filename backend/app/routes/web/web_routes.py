from flask import Blueprint

from app.controllers.web.web_controller import WebController


web_bp = Blueprint(
    "web",
    __name__
)


# ==========================================================
# INICIO
# ==========================================================

@web_bp.route("/")
def inicio():

    return WebController.inicio()

@web_bp.route("/galeria/<int:galeria_id>/imagenes")
def obtener_imagenes(galeria_id):
    return WebController.obtener_imagenes(galeria_id)