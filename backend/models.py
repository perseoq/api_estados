from backend.instances import db

# Modelos
class States(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    estado = db.Column(db.String(100), nullable=False, unique=True)
    capital = db.Column(db.String(100), nullable=False)
    población = db.Column(db.String(100), nullable=False)