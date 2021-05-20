from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from werkzeug.security import check_password_hash

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
        self.password = password
    
    def verify_passoword(self, pwd):
        return check_password_hash(self.senha, pwd)


# Cria o banco
Base.metadata.create_all(engine)

# Criação configuração da sessão
Session = sessionmaker(bind=engine)

# Criação da sessão
session = Session()


# Programa principal

alunos = {"1" : {"login": request.form["user_name"],"senha": request.form["user_name"]}, 
          "2" : {"login": "Rafex","senha": "teste"},
          "3" : {"login": "Mateus","senha": "teste"}}

def criaUser(user):
    user = Login(user["login"], user["senha"])

    session.add(user)

    session.commit()
    session.close()



criaUser(alunos["1"])
criaUser(alunos["2"])
criaUser(alunos["3"])







    


