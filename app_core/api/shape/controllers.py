from flask import Blueprint, jsonify, request, current_app
from datetime import datetime
from ...lib.shapes.geometric_shape import GeometricShape
import math

#from app_core.data.models import db, User
shape = Blueprint('shape', __name__)

@shape.route('/', methods=['GET'])
def get_shapes():

    return jsonify({ "module": "shapes" })

#@shape.route('/square/<float:side_lenght>', methods=['GET'])
@shape.route('/square/calculator', methods=['POST'])
def square():
    if request.is_json:
       square = GeometricShape("SQUARE",request.json).geometricShape
       return jsonify({ "shape": "square",
     "side_lenght":square.lenght,
     "area":str(square.area),
     "perimeter":str(square.perimeter),
     "status":200,
     "from_ip":request.remote_addr,
     "timestamp":datetime.now().strftime("%d/%m/%Y %H:%M:%S")})

    """square = Square(side_lenght)
    return jsonify({ "shape": "square",
     "side_lenght":side_lenght,
     "area":str(square.area),
     "perimeter":str(square.perimeter),
     "status":200,
     "from_ip":request.remote_addr,
     "timestamp":datetime.now().strftime("%d/%m/%Y %H:%M:%S")})
    """

#@shape.route('/circle/<float:radius>', methods=['GET'])
@shape.route('/circle/calculator', methods=['POST'])
def circle():
    print("Circle>>>>")
    if request.is_json:
       print("Circle>>>>"+str(request.json)) 
       circle = GeometricShape("CIRCLE",request.json).geometricShape
       return jsonify({ "shape": "circle",
     "radius":circle.radius,
     "area":str(circle.area),
     "perimeter":str(circle.perimeter),
     "status":200,
     "from_ip":request.remote_addr,
     "timestamp":datetime.now().strftime("%d/%m/%Y %H:%M:%S")})

@shape.route('/login/<int:id>', methods=['POST'])
def login(id):

    return jsonify({ "id": id })

@shape.route('/register/<int:id>', methods=['POST'])
def register(id):

    return jsonify({ "id": id })

@shape.route('/update/<int:id>', methods=['PUT'])
def update(id):

    return jsonify({ "id": id })

@shape.route('/remove/<int:id>', methods=['DELETE'])
def delete(id):

    return jsonify({ "id": id })