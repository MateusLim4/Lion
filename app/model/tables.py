from app import db,UserMixin

class Usuarios(db.Model, UserMixin):
    __tablename__ = "tb_usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    sobrenome = db.Column(db.String(150))
    user_name = db.Column(db.String(16), unique=True)
    telefone = db.Column(db.String(14))
    email = db.Column(db.String(255), unique=True)
    senha = db.Column(db.String(150))
    created_at = db.Column(db.String(120))
    updated_at = db.Column(db.String(120))

    def __init__(self, nome, sobrenome, user_name, telefone, email, senha, created_at, updated_at):
        self.nome = nome
        self.sobrenome = sobrenome
        self.user_name = user_name
        self.telefone = telefone
        self.email = email
        self.senha = senha
        self.created_at = created_at
        self.updated_at = updated_at