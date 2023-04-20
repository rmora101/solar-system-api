from flask import Blueprint, jsonify

class Planet:
    def __init__(self, id, name, description, num_of_moons):
        self.id = id
        self.name = name
        self.description = description
        self.num_of_moons = num_of_moons

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods= ["GET"])

