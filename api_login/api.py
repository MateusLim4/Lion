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

def criaUser(user, pwd):
    create = Login(user, pwd)

    session.add(create)

    session.commit()
    session.close()

def validaUser(user, pwd):
    search = session.query(Login).filter_by(login=user).first()

    if user == search.login:
        if pwd == search.password:
            return True
        else:
            return False
    else:
        return False





    


