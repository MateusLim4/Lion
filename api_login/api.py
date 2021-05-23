from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import login_user, logout_user

# Criação da engine
engine = create_engine("sqlite:///login.db")

conn = engine.connect()

Base = declarative_base()

class Login(Base):
    __tablename__ = "tb_logins"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(28), unique=True)
    password = Column(String(100))

    def __init__(self, login, password):
        self.login = login
        self.password = generate_password_hash(password)
    
    def verify_passoword(self, pwd):
        return check_password_hash(self.password, pwd)


# Cria o banco
Base.metadata.create_all(engine)

# Criação configuração da sessão
Session = sessionmaker(bind=engine)

# Criação da sessão
session = Session()


# Programa principal

def criaUser(user, pwd):
    create = Login(user, pwd)

    session.add(create)

    session.commit()
    session.close()

def loginUser(user, pwd):
    search = session.query(Login).filter_by(login=user).first()

    if not search or not search.verify_passoword(pwd):
        session.close()
        return False
    else:
        session.close()
        return [True, search.login]

def validaUser(user):
    search = session.query(Login).filter_by(login=user).first()
    
    if search == None:
        return True
    else:
        return False

def deletaUser(user):
    session.delete(session.query(Login).filter_by(login=user).first())

    session.commit()
    session.close()






    


