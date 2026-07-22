from flask import render_template, request, redirect, url_for, session, flash
from werkzeug.security import check_password_hash

from app.models.usuario_model import UsuarioModel


class AuthController:

    @staticmethod
    def mostrar_login():
        """
        Muestra la vista del login.
        """
        return render_template("login.html")


    @staticmethod
    def login():
        """
        Procesa el inicio de sesión.
        """

        correo = request.form.get("correo")
        password = request.form.get("password")


        # Buscar usuario
        usuario = UsuarioModel.obtener_por_correo(correo)


        


        # Validar que exista
        if not usuario:
            flash("Correo o contraseña incorrectos.", "danger")
            return redirect(url_for("auth.mostrar_login"))


        # Validar estado
        if usuario["estado"] != "ACTIVO":
            flash("El usuario está inactivo.", "warning")
            return redirect(url_for("auth.mostrar_login"))



        # Validar contraseña

        resultado_password = check_password_hash(
            usuario["password"],
            password
        )


        


        if not resultado_password:
            flash("Correo o contraseña incorrectos.", "danger")
            return redirect(url_for("auth.mostrar_login"))



        # Crear sesión
        session["usuario_id"] = usuario["id"]
        session["nombre"] = usuario["nombres"]
        session["rol"] = usuario["rol"]


        # Actualizar último acceso
        UsuarioModel.actualizar_ultimo_acceso(usuario["id"])


        # Redireccionar
        return redirect(url_for("dashboard.index"))



    @staticmethod
    def logout():
        """
        Cierra sesión.
        """

        session.clear()

        return redirect(url_for("auth.mostrar_login"))