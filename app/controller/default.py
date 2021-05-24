from flask import render_template, redirect, request, url_for
from requests import api
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, UserMixin
from app import login_manager, app, db
from app.model.tables import Usuarios
from api_login.api import validaUser, loginUser, criaUser, Login

def getDate():
    today = date.today()
    now = datetime.now()

    data = today.strftime("%B %d, %Y")
    hora = now.strftime("%H:%M:%S")

    complete = data + " " + hora

    return complete

def validaDados(dado1, dado2):
    if dado1 == dado2:
        return True
    else:
        return False

@login_manager.user_loader
def get_user(user_id):
    return Usuarios.query.filter_by(id=user_id).first()


# @app.route("/")
# def login():
#     return render_template("login.html")


@app.route("/auth/login", methods=["POST"])
def auth_login():
    user = request.form["username"]
    senha = request.form["password"]

    auth = loginUser(user, senha)
    
    if auth[0]:
        login_user(Usuarios.query.filter_by(username=auth[1]).first())
        return redirect(url_for("home"))
    else:
        return render_template("login.html", mensagem="Usuario e senha incorretos!")


@app.route("/auth/singup", methods=["GET", "POST"])
def auth_singup():
    if request.method == "POST":   
        if validaDados(request.form["email"], request.form["emailConfirm"]) and (Usuarios.query.filter_by(email=request.form["email"]).first() == None):
            email = request.form["email"]
        else:
            return render_template("login.html", mensagem="Os Emails não batem!")

        if validaDados(request.form["password"], request.form["passwordConfirm"]):
            password = request.form["password"]
        else:
            return render_template("login.html", mensagem="As senhas não batem!")
        
        if validaUser(request.form["username"]):
            username = request.form["username"]
        else:
            return render_template("login.html", mensagem="Nome de usuário não disponível")

        date = getDate()

        usuario = Usuarios(request.form["name"],request.form["lastname"],username, request.form["phone"], email, date, date)

        criaUser(username, password)

        db.session.add(usuario)
        db.session.commit()

        return render_template("login.html", mensagem="Usuário criado com sucesso!")  
    else:
        return render_template("login.html")    



# ---------------------------------------------------------------------------------------------------------------------------- #


lightTheme = ['bg-light','bg-body','text-dark','border-body','border-body','black']
darkTheme = ['bg-dark','bg-black','text-light','border-dark','border-body','white']

theme = lightTheme #ideal colocar consultando o Banco de dados, para deixar como padão o que foi selecionado pelo usuário

@app.route("/")
def home():
    return render_template("landing-page.html",theme=theme)

@app.route("/perfil")
def perfil():
    return render_template('perfil.html',theme=theme)

@app.route('/darkTheme',methods=['POST'])
def dark():
    theme = darkTheme
    return render_template('landing-page.html',theme=theme)

@app.route('/lightTheme',methods=['POST'])
def light():
    theme = lightTheme
    return render_template('landing-page.html',theme=theme)

@app.route('/darkTheme1',methods=['POST'])
def dark1():
    theme = darkTheme
    return render_template('perfil.html',theme=theme)

@app.route('/lightTheme1',methods=['POST'])
def light1():
    theme = lightTheme
    return render_template('perfil.html',theme=theme)