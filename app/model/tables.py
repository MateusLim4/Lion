from app import db,UserMixin

class Usuarios(db.Model, UserMixin):
    __tablename__ = "tb_usuarios"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(150))
    sobrenome = db.Column(db.String(150))
    username = db.Column(db.String(16))
    telefone = db.Column(db.String(14))
    email = db.Column(db.String(255), unique=True)
    theme = db.Column(db.String(10))
    created_at = db.Column(db.String(120))
    updated_at = db.Column(db.String(120))

    def __init__(self, nome, sobrenome, username, telefone, email, theme, created_at, updated_at):
        self.nome = nome
        self.sobrenome = sobrenome
        self.username = username
        self.telefone = telefone
        self.email = email
        self.theme = theme
        self.created_at = created_at
        self.updated_at = updated_at

class Follow(db.Model, UserMixin):
    __tablename__ = "tb_follow"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user = db.Column(db.Integer, ForeingKey("tb_usuarios.id"))
    id_seguidores = db.Column(db.Integer)
    id_seguindo = db.Column(db.Integer)

    def __init__(self, user, id_seguidores, id_seguindo):
        self.user = user
        self.id_seguidores = id_seguidores
        self.id_seguindo = id_seguindo
