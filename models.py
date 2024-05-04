"""Adoption Agency Models"""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app
    db.init_app(app)
    
class Pet(db.Model):
    """Pet Model for Pet Adoption database"""
    
    __tablename__ = "pets"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)  
    species = db.Column(db.Text, nullable=False)
    photo_url = db.Column(db.Text, nullable=False, default="https://t4.ftcdn.net/jpg/04/70/29/97/360_F_470299797_UD0eoVMMSUbHCcNJCdv2t8B2g1GVqYgs.jpg")
    age = db.Column(db.Integer) 
    notes = db.Column(db.Text)
    available = db.Column(db.Boolean, nullable=False, default=True)
    
    def __repr__(self):
        pet = self
        return f"<Pet id={pet.id} name={pet.name} species={pet.species} photo_url={pet.photo_url} age={pet.age} notes={pet.notes} available={pet.available}>"