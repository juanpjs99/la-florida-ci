from flask import render_template

from app.models.noticia_model import NoticiaModel
from app.models.evento_model import EventoModel
from app.models.galeria_model import GaleriaModel


class WebController:

    @staticmethod
    def inicio():
        """
        Página principal del portal web.
        """

        noticias = NoticiaModel.obtener_recientes(5)

        eventos = EventoModel.obtener_proximos(5)

        galerias = GaleriaModel.obtener_publicas(6)

        return render_template(
            "web/index.html",
            noticias=noticias,
            eventos=eventos,
            galerias=galerias
        )