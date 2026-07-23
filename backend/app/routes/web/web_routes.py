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