from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from flask_login import LoginManager, login_manager, UserMixin

app = Flask("__name__")
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///usuario.db"
app.config["SECRET_KEY"] = "secret"
db = SQLAlchemy(app)
login_manager = LoginManager(app)

if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)