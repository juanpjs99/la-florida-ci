from flask import Blueprint

from app.controllers.evento_controller import EventoController

evento = Blueprint(
    "evento",
    __name__,
    url_prefix="/dashboard/eventos"
)


@evento.route("/")
def listar():
    return EventoController.listar()


@evento.route("/crear")
def mostrar_crear():
    return EventoController.mostrar_crear()


@evento.route("/guardar", methods=["POST"])
def guardar():
    return EventoController.guardar()


@evento.route("/editar/<int:id>")
def editar(id):
    return EventoController.editar(id)


@evento.route("/actualizar/<int:id>", methods=["POST"])
def actualizar(id):
    return EventoController.actualizar(id)


@evento.route("/eliminar/<int:id>")
def eliminar(id):
    return EventoController.eliminar(id)