from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ARRAY
from sqlalchemy.orm import composite

db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    role = db.Column(db.Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'role': self.role
        }


class Ingredient(db.Model):
    __tablename__ = 'ingredient'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
        }


class Recipes(db.Model):
    __tablename__ = 'recipes'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    listIngredients = db.Column(ARRAY(object))

    @ property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'listIngredients': self.listIngredients
        }
