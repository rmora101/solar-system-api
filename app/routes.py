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

def validate_item(model, item_id):
    try:
        valid_id = int(item_id)
    except ValueError:
        return abort(make_response({"Message" : f"Invalid id: {item_id}"}, 400))
    
    return model.query.get_or_404(valid_id)

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def add_planet():
    request_body = request.get_json()
    new_planet = Planet.from_dict(request_body)

    db.session.add(new_planet)
    db.session.commit()

    return {"id": new_planet.id}, 201

@planets_bp.route("", methods= ["GET"])
def get_planets():
    response = []

    name_query = request.args.get("name")
    moons_query = request.args.get("number_of_moons")
    if moons_query:
        planets = Planet.query.filter_by(number_of_moons=moons_query)
    elif name_query:
        planets = Planet.query.filter_by(name=name_query)
    else:
        planets = Planet.query.all()

    for planet in planets:
        planet_dict = {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "number_of_moons": planet.number_of_moons

        }

        response.append(planet_dict)

    return jsonify(response), 200

@planets_bp.route("/<id>", methods = ["GET"])
def get_one_planet(id): 

    planet = validate_item(Planet, id)
    
    return planet.to_dict(), 200

@planets_bp.route("/<id>", methods = ["PUT"])
def update_planet(id):

    planet = validate_item(Planet, id)

    request_data = request.get_json()

    planet.name = request_data["name"]
    planet.description = request_data["description"]
    planet.number_of_moons = request_data["number_of_moons"]

    db.session.commit()

    return {"msg": f"planet {id} successfully updated"}, 200

@planets_bp.route("/<id>", methods = ["DELETE"])
def delete_planet(id):
    planet = validate_item(Planet, id)

    db.session.delete(planet)
    db.session.commit()

    return {"msg": f" planet {id} deleted"}, 200