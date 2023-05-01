from flask import abort, Blueprint, jsonify, make_response, request
from app import db
from app.models.planet import Planet

# class Planet:
#     def __init__(self, id, name, description, num_of_moons):
#         self.id = id
#         self.name = name
#         self.description = description
#         self.num_of_moons = num_of_moons

# planet1 = Planet(1, "Mercury", "The atmosphere of Mercury is a surface bounded exosphere, essentially a vacuum.", 0)
# planet2 = Planet(2, "Venus", "Venus is the hottest planet.", 0)
# planet3 = Planet(3, "Earth", "Earth is our home.", 1)
# planet4 = Planet(4, "Mars", "Mars is red", 2)
# planet5 = Planet(5, "Jupiter", "Jupiter is the biggest", 92)
# planet6 = Planet(6, "Saturn", "Saturn has a big ring", 83)
# planet7 = Planet(7, "Uranus", "Uranus has a unique tilt", 27)
# planet8 = Planet(8, "Neptune", "Neptune is the only planet not visible to the naked eye", 14)
# planet9 = Planet(9, "Pluto", "Pluto is a PLANET", 5)

# planet_list = [planet1, planet2, planet3, planet4, planet5, planet6, planet7, planet8, planet9]

def validate_planet(planet_id):
    try:
        valid_planet_id = int(planet_id)
    except ValueError:
        return abort(make_response({f"Message" : "Invalid id: {planet_id}"}, 400))
    
    return Planet.query.get_or_404(valid_planet_id)

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet(
        name = request_body["name"],
        description = request_body["description"],
        number_of_moons = request_body["number_of_moons"]
    )

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planets_bp.route("", methods= ["GET"])
def get_planets():
    response = []
    all_planets = Planet.query.all()
    for planet in all_planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number of moons": planet.number_of_moons

        }

        response.append(planet_dict)

    return jsonify(response), 200

@planets_bp.route("/<id>", methods = ["GET"])
def get_one_planet(id): 

    planet = validate_planet(id)
    
    return planet.to_dict(), 200
