from flask import Blueprint

from app.controllers.evento_controller import EventoController

evento_bp = Blueprint(
    "evento",
    __name__,
    url_prefix="/dashboard/eventos"
)


@evento_bp.route("/")
def listar():
    return EventoController.listar()


@evento_bp.route("/crear")
def mostrar_crear():
    return EventoController.mostrar_crear()


@evento_bp.route("/guardar", methods=["POST"])
def guardar():
    return EventoController.guardar()


@evento_bp.route("/editar/<int:id>")
def editar(id):
    return EventoController.editar(id)


@evento_bp.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    return EventoController.actualizar(id)


@evento_bp.route("/eliminar/<int:id>")
def eliminar(id):
    return EventoController.eliminar(id)