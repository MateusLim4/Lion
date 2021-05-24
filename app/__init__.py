from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager, login_manager, UserMixin

app = Flask(__name__, template_folder="templates")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuario.db"
app.config["SECRET_KEY"] = "secret"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
login_manager = LoginManager(app)

from app.controller import default