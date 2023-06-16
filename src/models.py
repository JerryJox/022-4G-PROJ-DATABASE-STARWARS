import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    # Here we define columns for the table user
    # Notice that each column is also a normal Python instance attribute.
    id_user = Column(Integer(), primary_key=True, unique=True)  
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)

class Character(Base):
    __tablename__ = 'characters'
    id = Column(Integer(), primary_key=True, unique=True)
    name = Column(String(250), nullable=False)
    bith_year = Column(String(250), nullable=False)
    eye_color = Column(String(250))
    gender = Column (String(250))
    hair_color = Column(String(250))
    # homeworld_id = Column(String(250), ForeignKey=("planets.id_planet"), nullable=False)
    # planets = relationship(Planet)
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starship = Column(String(250), nullable=False)
    films = Column(String(250), nullable=False)

class Starship(Base):
    __tablename__ = 'starships'
    id = Column(Integer(), primary_key=True)
    cargo_capacity = Column(Integer(), nullable=False)
    consumable = Column(String(250), nullable=False)
    cost_in_credits = Column(Integer(), nullable=False)
    crew = Column(String(250), nullable=False)
    hyperdrive_rating = Column(Integer(), nullable=False)
    MGLT = Column(String(250), nullable=False)
    length = Column(Integer(), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosfering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(Integer(), nullable=False)
    films = Column(String(250), nullable=False)
    pilots = Column(String(250), nullable=False)
    starship_class = Column(String(250), nullable=False)

class Planet(Base):
    __tablename__ = 'planets'
    id = Column(Integer(), primary_key=True)
    climate = Column(String(250), nullable=False)
    films = Column(Integer(), primary_key=True)
    gravity = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

class Cha_Favs(Base):
    __tablename__ = 'cha_favs'
    id = Column(Integer(), primary_key=True)
    cha_favs_id= Column(Integer(), ForeignKey("characters.id"), nullable=False)
    id_user = Column(Integer(), ForeignKey("users.id_user"), nullable=False)
    users = relationship(User)   

class Pla_Favs(Base):
    __tablename__ = 'pla_favs'
    id = Column(Integer(), primary_key=True)
    pla_favs_id= Column(Integer(), ForeignKey("planets.id"), nullable=False)
    id_user = Column(Integer(), ForeignKey("users.id_user"), nullable=False)
    users = relationship(User)

class Shi_Favs(Base):
    __tablename__ = 'shi_favs'
    id = Column(Integer(), primary_key=True)
    shi_favs_id= Column(Integer(), ForeignKey("starships.id"), nullable=False)
    user_id = Column(Integer(), ForeignKey("users.id"), nullable=False)
    users = relationship(User)    

class Film(Base):
    __tablename__ = 'films'
    id_films = Column(Integer(), primary_key=True)
    film_name = Column(String(250), nullable=False)
    characters = Column(String(250), ForeignKey("characters.id"), nullable=False)
    starships = Column(String (250), ForeignKey("starships.id"), nullable=False)
    planets = Column(String(250), ForeignKey("planets.id"), nullable=False)

class Collaboration(Base):
    __tablename__ = 'collaborations'
    id_collab = Column(Integer(), primary_key=True)
    id_films = Column(Integer(), ForeignKey("films.id"), nullable=False)
    id_characters = Column(Integer(), ForeignKey("characters.id_character"), nullable=False)
    id_starships = Column(String(250), ForeignKey("starships.id"), nullable=False)
    id_planets = Column(String(250), ForeignKey("planets.id"), nullable=False)
    

# class Address(Base):
#     __tablename__ = 'address'
#     id = Column(Integer, primary_key=True)
#     street_name = Column(String(250))
#     street_number = Column(String(250))
#     post_code = Column(String(250), nullable=False)
#     person_id = Column(Integer, ForeignKey('person.id'))
#     person = relationship(Character)

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')