from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons

planet1 = Planet(1, "Mercury", "The atmosphere of Mercury is a surface bounded exosphere, essentially a vacuum.", 0)
planet2 = Planet(2, "Venus", "Venus is the hottest planet.", 0)
planet3 = Planet(3, "Earth", "Earth is our home.", 1)
planet4 = Planet(4, "Mars", "Mars is red", 2)
planet5 = Planet(5, "Jupiter", "Jupiter is the biggest", 92)
planet6 = Planet(6, "Saturn", "Saturn has a big ring", 83)
planet7 = Planet(7, "Uranus", "Uranus has a unique tilt", 27)
planet8 = Planet(8, "Neptune", "Neptune is the only planet not visible to the naked eye", 14)
planet9 = Planet(9, "Pluto", "Pluto is a PLANET", 5)

planet_list = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8, planet9]

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods= ["GET"])
def get_planets():
    response = []
    for planet in planet_list:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.num_of_moons

        }

        response.append(planet_dict)

    return jsonify(response), 200

@planets_bp.route("/<id>", methods = ["GET"])
def get_one_planet(id): 

    try:
        planet.id = int(id)
    except ValueError:
        return {"message" : "Invalid id"}, 400
    
    for planet in planet_list:
        if planet.id == int(id):
            return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.num_of_moons
            }, 200
    
    return {"message" : f"{id} not found"}, 404