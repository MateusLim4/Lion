from flask import render_template, redirect, request, url_for
from requests import api
from datatime import date, datatime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user
from app import login_manager, app
from app.model.tables import Usuarios
from api_login import criaUser

@app.route("/")
def entrar():
    pass

