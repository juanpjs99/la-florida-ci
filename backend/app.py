from flask import Flask

from config import Config
from app.database.db import mysql

# Blueprints
from app.routes.auth_routes import auth
from app.routes.dashboard_routes import dashboard
from app.routes.admin.noticia_routes import noticia
from app.routes.admin.evento_routes import evento
from app.routes.admin.galeria_routes import galeria
from app.routes.admin.galeria_imagen_routes import galeria_imagen_bp


app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.config.from_object(Config)

mysql.init_app(app)

# Registrar Blueprints
app.register_blueprint(auth)
app.register_blueprint(dashboard)
app.register_blueprint(noticia)
app.register_blueprint(evento)
app.register_blueprint(galeria)
app.register_blueprint(galeria_imagen_bp)


@app.route("/")
def home():
    return "Backend La Florida CI"


@app.route("/test-db")
def test_db():
    try:
        cursor = mysql.connection.cursor()

        cursor.execute("SELECT DATABASE();")

        resultado = cursor.fetchone()

        cursor.close()

        return {
            "status": "ok",
            "database": resultado[0]
        }

    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }


if __name__ == "__main__":
    app.run(debug=True)