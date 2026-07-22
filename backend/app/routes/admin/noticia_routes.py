from flask import Blueprint
from app.controllers.noticia_controller import NoticiaController

noticia = Blueprint(
    "noticia",
    __name__,
    url_prefix="/dashboard/noticias"
)

@noticia.route("/")
def listar():
    return NoticiaController.listar()

@noticia.route("/nueva", methods=["GET"])
def mostrar_crear():
    return NoticiaController.mostrar_crear()

@noticia.route("/guardar", methods=["POST"])
def guardar():
    return NoticiaController.guardar()

@noticia.route("/editar/<int:id>", methods=["GET"])
def editar(id):
    return NoticiaController.editar(id)

@noticia.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    return NoticiaController.actualizar(id)

@noticia.route("/eliminar/<int:id>")
def eliminar(id):
    return NoticiaController.eliminar(id)