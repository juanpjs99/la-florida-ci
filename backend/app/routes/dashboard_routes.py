from flask import Blueprint, render_template, session, redirect, url_for
from app.models.noticia_model import NoticiaModel
from app.models.evento_model import EventoModel
from app.models.galeria_model import GaleriaModel

dashboard = Blueprint(
    "dashboard",
    __name__,
    url_prefix="/dashboard"
)


@dashboard.route("/")
def index():

    if "usuario_id" not in session:
        return redirect(url_for("auth.mostrar_login"))

    stats = {
        "noticias": NoticiaModel.contar(),
        "eventos": EventoModel.contar(),
        "galeria": GaleriaModel.contar()
    }

    return render_template(
        "dashboard/index.html",
        nombre=session["nombre"],
        rol=session["rol"],
        stats=stats
    )