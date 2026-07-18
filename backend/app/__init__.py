from flask import Flask

from config import Config
from app.database.db import mysql


def create_app():

    app = Flask(__name__)

    app.config.from_object(Config)

    mysql.init_app(app)

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