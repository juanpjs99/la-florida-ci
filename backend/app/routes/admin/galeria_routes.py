from flask import Blueprint

from app.controllers.galeria_controller import GaleriaController


galeria = Blueprint(
    "galeria",
    __name__,
    url_prefix="/dashboard/galerias"
)


@galeria.route("/")
def listar():
    return GaleriaController.listar()


@galeria.route("/nueva")
def mostrar_crear():
    return GaleriaController.mostrar_crear()


@galeria.route("/guardar", methods=["POST"])
def guardar():
    return GaleriaController.guardar()


@galeria.route("/editar/<int:id>")
def editar(id):
    return GaleriaController.editar(id)


@galeria.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    return GaleriaController.actualizar(id)


@galeria.route("/eliminar/<int:id>")
def eliminar(id):
    return GaleriaController.eliminar(id)