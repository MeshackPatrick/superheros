from random import randint, choice
from models import Hero, Power, HeroPower

print("🦸‍♀️ Seeding powers...")
powers_data = [
    { "name": "super strength", "description": "gives the wielder super-human strengths" },
    { "name": "flight", "description": "gives the wielder the ability to fly through the skies at supersonic speed" },
    { "name": "super human senses", "description": "allows the wielder to use her senses at a super-human level" },
    { "name": "elasticity", "description": "can stretch the human body to extreme lengths" }
]

for data in powers_data:
    # Create powers using the data
    power = Power.create(name=data["name"], description=data["description"])

print("🦸‍♀️ Seeding heroes...")
heroes_data = [
    { "name": "Kamala Khan", "super_name": "Ms. Marvel" },
    { "name": "Doreen Green", "super_name": "Squirrel Girl" },
    { "name": "Gwen Stacy", "super_name": "Spider-Gwen" },
    { "name": "Janet Van Dyne", "super_name": "The Wasp" },
    { "name": "Wanda Maximoff", "super_name": "Scarlet Witch" },
    { "name": "Carol Danvers", "super_name": "Captain Marvel" },
    { "name": "Jean Grey", "super_name": "Dark Phoenix" },
    { "name": "Ororo Munroe", "super_name": "Storm" },
    { "name": "Kitty Pryde", "super_name": "Shadowcat" },
    { "name": "Elektra Natchios", "super_name": "Elektra" }
]

for data in heroes_data:
    # Create heroes using the data
    hero = Hero.create(name=data["name"], super_name=data["super_name"])

print("🦸‍♀️ Adding powers to heroes...")
strengths = ["Strong", "Weak", "Average"]

for hero in Hero.query.all():
    for _ in range(randint(1, 3)):
        # Get a random power
        power = Power.query.get(randint(1, len(powers_data)))

        # Create HeroPower relationships
        HeroPower.create(hero_id=hero.id, power_id=power.id, strength=choice(strengths))

print("🦸‍♀️ Done seeding!")
