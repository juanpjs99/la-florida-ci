from flask import Blueprint, render_template, session, redirect, url_for

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
        "noticias": 0,
        "eventos": 0,
        "galerias": 0
    }

    return render_template(
        "dashboard/index.html",
        nombre=session["nombre"],
        rol=session["rol"],
        stats=stats
    )