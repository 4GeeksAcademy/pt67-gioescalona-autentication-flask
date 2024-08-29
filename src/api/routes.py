from flask import Flask, request, jsonify, Blueprint
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from api.models import db, User, Characters, Vehicles, Planets
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

app = Flask(__name__)

api = Blueprint('api', __name__)
CORS(api)

current_user = User.name

@api.route('/login', methods=['POST'])
def login():
   
    name = request.json.get('name', None)
    email = request.json.get('email', None)
    password = request.json.get('password', None)

  
    if not name or not email or not password:
        return jsonify({"msg": "Missing name, email, or password"}), 400

    user = User.query.filter_by(email=email).first()

 
    if not user or user.password != password:
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=email)
    return jsonify(access_token=access_token), 200


@api.route('/protected', methods=['GET'])
@jwt_required()
def protected():
    current_user = get_jwt_identity()
    user = User.query.filter_by(email=current_user)
    if user is None:
        raise APIException("USER NOT FOUND",status_code=404)
    return jsonify("user autenticated"), 200

@api.route('/hello', methods=['POST', 'GET'])
def handle_hello():
    response_body = {
        "message": "Hello! I'm a message that came from the backend, check the network tab on the google inspector and you will see the GET request"
    }
    return jsonify(response_body), 200

################# TODOS mis endpoints a partir de aquí
############ métodos GET ALL
@api.route('/users', methods=['GET'])
def handle_users():
    users = User.query.all()
    users_serialized = list(map(lambda item:item.serialize(), users))
    response_body = {
        "msg": "OK",
        "data": users_serialized
    }
    return jsonify(response_body), 200

@api.route('/characters', methods=['GET'])
def handle_characters():
    characters = Characters.query.all()
    characters_serialized = list(map(lambda item:item.serialize(), characters))
    response_body = {
        "msg": "OK",
        "data": characters_serialized
    }
    return jsonify(response_body), 200

@api.route('/vehicles', methods=['GET'])
def handle_vehicles():
    vehicles = Vehicles.query.all()
    vehicles_serialized = list(map(lambda item:item.serialize(), vehicles))
    response_body = {
        "msg": "OK",
        "data": vehicles_serialized
    }
    return jsonify(response_body), 200

@api.route('/planets', methods=['GET'])
def handle_planets():
    planets = Planets.query.all()
    planets_serialized = list(map(lambda item:item.serialize(), planets))
    response_body = {
        "msg": "OK",
        "data": planets_serialized
    }
    return jsonify(response_body), 200

#####post

@api.route('/users', methods=['POST'])
def create_user():
    body = request.json
    me = User(name=body["name"], email=body["email"], password=body["password"], is_active=body["is_active"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/characters', methods=['POST'])
@jwt_required()
def create_character():
    body = request.json
    me = Characters(name=body["name"], eye_color=body["eye_color"], hair_color=body["hair_color"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/vehicles', methods=['POST'])
@jwt_required()
def create_vehicle():
    body = request.json
    me = Vehicles(name=body["name"], model=body["model"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200

@api.route('/planets', methods=['POST'])
@jwt_required()
def create_planet():
    body = request.json
    me = Planets(name=body["name"], population=body["population"])
    db.session.add(me)
    db.session.commit()
    response_body = {
        "msg": "Ok",
        "id": me.id
    }
    return jsonify(response_body), 200


