from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

# Criação da engine
engine = create_engine("sqlite:///login.db")

conn = engine.connect()

Base = declarative_base()

class Usuario(Base):
    __tablename__ = "tb_usuarios"

    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(28), unique=True)
    password = Column(String(100))

    def __init__(self, login, password):
        self.login = login
        self.password = password

# Cria o banco
Base.metadata.create_all(engine)

# Criação configuração da sessão
Session = sessionmaker(bind=engine)

# Criação da sessão
session = Session()


# Programa principal

alunos = {"1" : {"login": "Lucas","senha": "teste"}, 
          "2" : {"login": "Rafex","senha": "teste"},
          "3" : {"login": "Mateus","senha": "teste"}}

def criaUser(user):
    user = Usuario(user["login"], user["senha"])

    session.add(user)

    session.commit()
    session.close()









    


