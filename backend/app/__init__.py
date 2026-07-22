from flask import Flask

from config import Config
from app.database.db import mysql

from app.routes.auth_routes import auth
from app.routes.dashboard_routes import dashboard
from app.routes.admin.noticia_routes import noticia
from app.routes.admin.evento_routes import evento
from app.routes.admin.galeria_routes import galeria


def create_app():

    app = Flask(
        __name__,
        template_folder="templates",
        static_folder="static"
    )

    app.config.from_object(Config)

    mysql.init_app(app)

    app.register_blueprint(auth)
    app.register_blueprint(dashboard)
    app.register_blueprint(noticia)
    app.register_blueprint(evento)
    app.register_blueprint(galeria)

    @app.route("/")
    def home():
        return "La Florida CI Backend"

    @app.route("/test-db")
    def test_db():

        cursor = mysql.connection.cursor()

        cursor.execute("SELECT DATABASE();")

        resultado = cursor.fetchone()

        cursor.close()

        return f"Conectado a: {resultado[0]}"

    return app