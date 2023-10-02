from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import validates

db = SQLAlchemy()

class Hero(db.Model):
    __tablename__ = 'hero'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    super_name = db.Column(db.String(100), nullable=False)
    powers = db.relationship('Power', secondary='hero_power')


class Power(db.Model):
    __tablename__ = 'powers'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    #heroes = db.relationship('Hero', secondary='hero_power')
    heroes = db.relationship('Hero', secondary='hero_power', overlaps="powers")
    @validates('description')
    def validate_description(self,key,value):
        if len(value) < 20:
            raise ValueError("Description must be at least 20 characters long")
        return value

class HeroPower(db.Model):
    __tablename__ = 'hero_power'

    id = db.Column(db.Integer, primary_key=True)
    strength = db.Column(db.String(10), nullable=False)
    hero_id = db.Column(db.Integer, db.ForeignKey('hero.id'), nullable=False)
    power_id = db.Column(db.Integer, db.ForeignKey('powers.id'), nullable=False)

    valid_strengths = {'Strong', 'Weak', 'Average'}

    @validates('strength')
    def valid_strengths(self, key, value):
        if value not in self.valid_strengths:
            raise ValueError("Strength must be one of: 'Strong', 'Weak', 'Average'")
        return value