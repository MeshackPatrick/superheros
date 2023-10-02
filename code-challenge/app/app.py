#!/usr/bin/env python3

from flask import Flask, make_response,request,jsonify
from flask_migrate import Migrate

from models import db, Hero,Power, HeroPower

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///heroes.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def home():
    return 'Welcome to super hero'

@app.route('/heroes', methods=['GET'])
def get_heroes():
    heroes = Hero.query.all()
    hero_data = [{"id":hero.id, "name":hero.name,"super_name":hero.super_name}for hero in heroes]
    return jsonify(hero_data)

@app.route('/powers/<int:id>', methods=['GET'])
def get_power_by_id(id):
    power = Power.query.get(id)
    if power:
        power_data = {
            "id": power.id,
            "name": power.name,
            "description": power.description
        }
        return jsonify(power_data)
    return jsonify({"error": "Power not found"}), 404

@app.route('/powers/<int:id>', methods=['PATCH'])
def update_power(id):
    power = Power.query.get(id)
    if power:
        data = request.get_json()
        description = data.get('description')
        if description:
            power.description = description
            try:
                db.session.commit()
                return jsonify({"id": power.id, "name": power.name, "description": power.description})
            except:
                return jsonify({"errors": ["Validation errors"]}), 400
        return jsonify({"errors": ["Description must be present and at least 20 characters long"]}), 400
    return jsonify({"error": "Power not found"}), 404

@app.route('/hero_powers', methods=['POST'])
def create_hero_power():
    data = request.get_json()
    strength = data.get('strength')
    power_id = data.get('power_id')
    hero_id = data.get('hero_id')

    if strength and power_id and hero_id:
        hero_power = HeroPower(strength=strength, power_id=power_id, hero_id=hero_id)
        db.session.add(hero_power)
        try:
            db.session.commit()
            return get_hero_by_id(hero_id)
        except:
            return jsonify({"errors": ["Validation errors"]}), 400
    return jsonify({"errors": ["Missing required data"]}), 400

if __name__ == '__main__':
    app.run(port=5555)