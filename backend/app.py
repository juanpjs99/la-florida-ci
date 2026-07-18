from flask import Flask, render_template, session, redirect, url_for

from config import Config
from app.database.db import mysql
from app.routes.auth_routes import auth

app = Flask(
    __name__,
    template_folder="app/templates",
    static_folder="app/static"
)

app.config.from_object(Config)
mysql.init_app(app)

#registrar blueprint de rutas de autenticación
app.register_blueprint(auth)




@app.route("/")
def home():
    return "Backend La Florida CI"


#dashboar protegido 
@app.route("/dashboard")
def dashboard():

    if "usuario_id" not in session:
        return redirect(url_for("auth.mostrar_login"))

    return render_template("dashboard/index.html")

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