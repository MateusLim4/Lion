from flask import render_template, redirect, request, url_for
from requests import api
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app import login_manager, app
from app.model.tables import Usuarios
from api_login.api import validaUser

def validaDados(dado1, dado2):
    if dado1 == dado2:
        return True
    else:
        return False

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/auth/login", methods=["POST"])
def auth_login():
    user = request.form["username"]
    senha = request.form["password"]

    auth = validaUser(user, senha)
    
    if auth:
        return redirect(url_for("home"))
    else:
        return render_template("login.html", mensagem="Usuario e senha incorretos!")

# @app.route("/auth/singup", methods=["GET", "POST"])
# def auth_singup():
#     if request.method == "POST":   
#         if validaDados(request.form["email"], request.form["emailConfirm"]):
#             email = request.form["email"]
#         else:
#             return render_template("login.html", mensagem="Emails não batem!")

#         usuario = Usuarios(request.form["name"],
#                         request.form["lastname"],
#                         request.form["username"],
#                         request.form["phone"], 
#                         email,
#                         senha,
#                         created_at,
#                         updated_at)
#     else:
#         return render_template("login.html")    



@app.route("/home")
def home():
    return render_template("landing-page.html")


