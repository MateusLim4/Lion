from flask import render_template, redirect, request, url_for
from requests import api
from datetime import date, datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, UserMixin, current_user
from app import login_manager, app, db
from app.model.tables import Usuarios
from api_login.api import validaUser, loginUser, criaUser, Login

light = ['bg-light','bg-body','text-dark','border-body','border-body','black']

dark = ['bg-dark','bg-black','text-light','border-dark','border-body','white']

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


@app.route("/home")
def home():
    if current_user.is_authenticated:
        if current_user.theme == "light":
            theme = light
            return render_template("landing-page.html",theme=theme)
        elif current_user.theme == "dark":
            theme = dark
            return render_template("landing-page.html",theme=theme)
    else:
        return render_template("login.html")


@app.route("/perfil")
def perfil():
    if current_user.is_authenticated:
        if current_user.theme == "light":
            theme = light
            return render_template("perfil.html",theme=theme)
        elif current_user.theme == "dark":
            theme = dark
            return render_template("perfil.html",theme=theme)


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

        usuario = Usuarios(request.form["name"],request.form["lastname"],username, request.form["phone"], email, "light", date, date)

        criaUser(username, password)

        db.session.add(usuario)
        db.session.commit()

        return render_template("login.html", mensagem="Usuário criado com sucesso!")  
    else:
        return render_template("login.html")    

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("home"))


@app.route('/home/darkTheme/<int:user_id>', methods=['POST'])
def darkTheme(user_id):
    query = Usuarios.query.filter_by(id=user_id).first()

    query.theme = "dark"

    db.session.commit()
    db.session.close()
    
    return redirect(url_for("home"))


@app.route('/home/lightTheme/<int:user_id>', methods=['POST'])
def lightTheme(user_id):
    query = Usuarios.query.filter_by(id=user_id).first()

    query.theme = "light"

    db.session.commit()
    db.session.close()
    
    return redirect(url_for("home"))


@app.route('/perfil/darkTheme/<int:user_id>', methods=['POST'])
def darkPerfil(user_id):
    query = Usuarios.query.filter_by(id=user_id).first()

    query.theme = "dark"

    db.session.commit()
    db.session.close()
    
    return redirect(url_for("perfil"))


@app.route('/perfil/lightTheme/<int:user_id>', methods=['POST'])
def lightPerfil(user_id):
    query = Usuarios.query.filter_by(id=user_id).first()

    query.theme = "light"

    db.session.commit()
    db.session.close()
    
    return redirect(url_for("perfil"))



