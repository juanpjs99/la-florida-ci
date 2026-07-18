from flask import Blueprint

from app.controllers.auth_controller import AuthController

auth = Blueprint("auth", __name__)


@auth.get("/login")
def mostrar_login():
    return AuthController.mostrar_login()


@auth.post("/login")
def login():
    return AuthController.login()


@auth.get("/logout")
def logout():
    return AuthController.logout()