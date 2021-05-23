from app import db,UserMixin

class Usuarios(db.Model, UserMixin):
    __tablename__ = "tb_usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    sobrenome = db.Column(db.String(150))
    username = db.Column(db.String(16))
    telefone = db.Column(db.String(14))
    email = db.Column(db.String(255), unique=True)
    created_at = db.Column(db.String(120))
    updated_at = db.Column(db.String(120))

    def __init__(self, nome, sobrenome, username, telefone, email, created_at, updated_at):
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username
        self.telefone = telefone
        self.email = email
        self.created_at = created_at
        self.updated_at = updated_at