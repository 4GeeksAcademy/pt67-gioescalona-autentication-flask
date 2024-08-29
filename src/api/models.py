from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    
    name  = db.Column(db.String(120), unique=True, nullable=False)
  
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'
    
    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            "name": self.name,
            # do not serialize the password, its a security breach
        }
    
class Characters(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Birth_year = db.Column(db.String(120), unique=True, nullable=False)
    Eye_color = db.Column(db.String(120), unique=True, nullable=False)
    Films = db.Column(db.String(120), unique=True, nullable=False)
    Gender = db.Column(db.String(120), unique=True, nullable=False)
    Hair_color = db.Column(db.String(120), unique=True, nullable=False)
    Heigh = db.Column(db.String(120), unique=True, nullable=False)
    Homeworld = db.Column(db.String(120), unique=True, nullable=False)
    Mass = db.Column(db.String(120), unique=True, nullable=False)
    Name = db.Column(db.String(120), unique=True, nullable=False)
    Skin_color = db.Column(db.String(120), unique=True, nullable=False)
    Created = db.Column(db.String(120), unique=True, nullable=False)
    Edited = db.Column(db.String(120), unique=True, nullable=False)
    Species = db.Column(db.String(120), unique=True, nullable=False)
    Starships = db.Column(db.String(120), unique=True, nullable=False)
    Url = db.Column(db.String(120), unique=True, nullable=False)
    Vehicles = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "Birth_year": self.birth_year,
            "Eye_colo": self.eye_colo,
            "Films": self.films,
            "Gender": self.gender,
            "Hair_color": self.hair_color,
            "Heigh": self.heigh,
            "Homeworld": self.homeworld,
            "Mass": self.mass,
            "Name": self.name,
            "Skin_color": self.skin_color,
            "Created": self.created,
            "Edited": self.edited,
            "Species": self.species,
            "Starships": self.starships,
            "Url": self.url,
            "Vehicles": self.vehicles,
            
        }
    
class Vehicles(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Cargo_capacity = db.Column(db.String(120), unique=True, nullable=False)
    consumables = db.Column(db.String(120), unique=True, nullable=False)
    cost_in_credits = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(120), unique=True, nullable=False)
    crew = db.Column(db.String(120), unique=True, nullable=False)
    edited = db.Column(db.String(120), unique=True, nullable=False)
    length = db.Column(db.String(120), unique=True, nullable=False)
    manufacturer = db.Column(db.String(120), unique=True, nullable=False)
    max_atmosphering_speed = db.Column(db.String(120), unique=True, nullable=False)
    model = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    passengers = db.Column(db.String(120), unique=True, nullable=False)
    pilots = db.Column(db.String(120), unique=True, nullable=False)
    films = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    vehicle_class = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "Cargo_capacity": self.cargo_capacity,
            "consumables": self.consumables,
            "cost_in_credits": self.cost_in_credits,
            "created": self.created,
            "crew": self.crew,
            "edited": self.edited,
            "length": self.length,
            "manufacturer": self.manufacturer,
            "max_atmosphering_speed": self.max_atmosphering_speed,
            "model": self.model,
            "name": self.name,
            "passengers": self.edited,
            "pilots": self.pilots,
            "films": self.films,
            "url": self.url,
            "vehicle_class": self.vehicle_class,
            
        }

class Planets(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    climate = db.Column(db.String(120), unique=True, nullable=False)
    created = db.Column(db.String(120), unique=True, nullable=False)
    diameter = db.Column(db.String(120), unique=True, nullable=False)
    edited = db.Column(db.String(120), unique=True, nullable=False)
    films = db.Column(db.String(120), unique=True, nullable=False)
    gravity = db.Column(db.String(120), unique=True, nullable=False)
    name = db.Column(db.String(120), unique=True, nullable=False)
    orbital_period = db.Column(db.String(120), unique=True, nullable=False)
    population = db.Column(db.String(120), unique=True, nullable=False)
    residents = db.Column(db.String(120), unique=True, nullable=False)
    surface_water = db.Column(db.String(120), unique=True, nullable=False)
    terrain = db.Column(db.String(120), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)

    def serialize(self):
        return {
            "id": self.id,
            "climate": self.climate,
            "created": self.created,
            "diameter": self.diameter,
            "edited": self.edited,
            "films": self.films,
            "gravity": self.gravity,
            "name": self.name,
            "orbital_period": self.orbital_period,
            "population": self.population,
            "residents": self.residents,
            "rotation_period": self.rotation_period,
            "surface_water": self.surface_water,
            "terrain": self.terrain,
            "url": self.url,
            
        }
