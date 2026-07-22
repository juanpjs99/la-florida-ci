from flask import Flask, render_template, session, redirect, url_for

from config import Config
from app.database.db import mysql
from app.routes.auth_routes import auth
from app.routes.noticia_routes import noticia
from app.routes.evento_routes import evento_bp

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.config.from_object(Config)
mysql.init_app(app)

#registrar blueprint de rutas de autenticación
app.register_blueprint(auth)
#registrar blueprint de rutas de noticias
app.register_blueprint(noticia)
#registrar blueprint de rutas de eventos
app.register_blueprint(evento_bp)
    


@app.route("/")
def home():
    return "Backend La Florida CI"


#dashboar protegido 
@app.route("/dashboard")
def dashboard():

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