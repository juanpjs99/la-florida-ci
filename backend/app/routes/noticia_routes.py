from flask import Blueprint
from app.controllers.noticia_controller import NoticiaController

noticia = Blueprint("noticia", __name__)

noticia.route("/noticias")(NoticiaController.listar)

noticia.route(
    "/noticias/nueva",
    methods=["GET"]
)(NoticiaController.mostrar_crear)

noticia.route(
    "/noticias/guardar",
    methods=["POST"]
)(NoticiaController.guardar)

noticia.route(
    "/noticias/editar/<int:id>",
    methods=["GET"]
)(NoticiaController.editar)
# Actualizar noticia
noticia.route(
    "/noticias/actualizar/<int:id>",
    methods=["POST"]
)(NoticiaController.actualizar)
# Eliminar noticia
noticia.route(
    "/noticias/eliminar/<int:id>"
)(NoticiaController.eliminar)