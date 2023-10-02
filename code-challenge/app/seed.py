from random import randint, choice
from app import db, app
from models import Hero, Power, HeroPower

with app.app_context():
    print("🦸‍♀️ Seeding powers...")
    powers_data = [
        {"name": "super strength", "description": "gives the wielder super-human strengths"},
        {"name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed"},
        {"name": "super human senses", "description": "allows the wielder to use her senses at a super-human level"},
        {"name": "elasticity", "description": "can stretch the human body to extreme lengths"}
    ]

    for data in powers_data:
        # Create powers using the data
        power = Power(name=data["name"], description=data["description"])
        db.session.add(power)

    db.session.commit()

    print("🦸‍♀️ Seeding heroes...")
    heroes_data = [
        {"name": "Kamala Khan", "super_name": "Ms. Marvel"},
        {"name": "Doreen Green", "super_name": "Squirrel Girl"},
        # Add more hero data here
    ]

    for data in heroes_data:
        # Create heroes using the data
        hero = Hero(name=data["name"], super_name=data["super_name"])
        db.session.add(hero)

    db.session.commit()

    print("🦸‍♀️ Adding powers to heroes...")
    strengths = ["Strong", "Weak", "Average"]

    for hero in Hero.query.all():
        for _ in range(randint(1, 3)):
            # Get a random power
            power = Power.query.get(randint(1, len(powers_data)))

            # Create HeroPower relationships
            hero_power = HeroPower(hero=hero, power=power, strength=choice(strengths))
            db.session.add(hero_power)

    db.session.commit()

print("🦸‍♀️ Done seeding!")
