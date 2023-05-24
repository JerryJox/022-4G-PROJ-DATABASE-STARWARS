import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()


class Films(Base):
    __tablename__ = 'films'
    id_films = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    characters = Column(Integer, ForeignKey('character.id_character'))
    starships = Column(Integer, ForeignKey('starship.id_starship'))
    planets = Column(Integer, ForeignKey('planet.id_planet'))

class Character(Base):
    __tablename__ = 'character'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id_character = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    bith_year = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    hair_color = Column(String(250), nullable=False)
    homeworld_id = Column(Integer, ForeignKey('planet.id_planet'))
    mass = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    species = Column(String(250), nullable=False)
    starship = Column(Integer, ForeignKey('starship.id_starship'))
    films = Column(Integer, ForeignKey('film.id_film'))

class Starship(Base):
    __tablename__ = 'starship'
    id_starship = Column(Integer, primary_key=True)
    cargo_capacity = Column(String(250), nullable=False)
    consumable = Column(String(250), nullable=False)
    cost_in_credits = Column(String(250), nullable=False)
    crew = Column(String(250), nullable=False)
    hyperdrive_rating = Column(String(250), nullable=False)
    MGLT = Column(String(250), nullable=False)
    length = Column(String(250), nullable=False)
    manufacturer = Column(String(250), nullable=False)
    max_atmosfering_speed = Column(String(250), nullable=False)
    model = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    passengers = Column(String(250), nullable=False)
    films = Column(Integer, ForeignKey('film.id_film'))
    pilots = relationship(Character)
    starship_class = Column(String(250), nullable=False)



class Planets(Base):
    __tablename__ = 'planets'
    id_planet = Column(Integer, primary_key=True)
    climate = Column(String(250), nullable=False)
    films = Column(Integer, ForeignKey('film.id_film'))
    gravity = Column(String(250), nullable=False)
    name = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    residents = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    surface_water = Column(String(250), nullable=False)
    terrain = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    id_user = Column(Integer, primary_key=True)  
    id_character = Column(Integer, ForeignKey('character.id_character'))
    id_starship = Column(Integer, ForeignKey('starship.id_starship'))
    id_planet = Column(Integer, ForeignKey('planet.id_planet'))
    id_films = Column(Integer, ForeignKey('film.id_film'))

class User(Base):
    __tablename__ = 'user'
    id_user = Column(Integer, primary_key=True)  
    email = Column(Integer, primary_key=True)
    password = Column(Integer, primary_key=True)
    

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



# import os
# import sys
# from sqlalchemy import Column, ForeignKey, Integer, String
# from sqlalchemy.orm import relationship, declarative_base
# from sqlalchemy import create_engine
# from eralchemy2 import render_er

# Base = declarative_base()


# class Films(Base):
#     __tablename__ = 'films'
#     id_films = Column(Integer, ForeignKey('film.id_film'))
#     name = Column(String(250), nullable=False)
#     characters = Column(String(250), nullable=False)
#     starships = Column(String(250), nullable=False)
#     planets = Column(String(250), nullable=False)

# class Character(Base):
#     __tablename__ = 'character'
#     # Here we define columns for the table person
#     # Notice that each column is also a normal Python instance attribute.
#     id_character = Column(Integer, ForeignKey('character.id_character'))
#     name = Column(String(250), nullable=False)
#     bith_year = Column(String(250), nullable=False)
#     eye_color = Column(String(250), nullable=False)
#     gender = Column(String(250), nullable=False)
#     hair_color = Column(String(250), nullable=False)
#     homeworld_id = Column(String(250), nullable=False)
#     mass = Column(String(250), nullable=False)
#     skin_color = Column(String(250), nullable=False)
#     species = Column(String(250), nullable=False)
#     starship = Column(String(250), nullable=False)
#     films = Column(String(250), nullable=False)

# class Starship(Base):
#     __tablename__ = 'starship'
#     id_starship = Column(Integer, ForeignKey('starship.id_starship'))
#     cargo_capacity = Column(String(250), nullable=False)
#     consumable = Column(String(250), nullable=False)
#     cost_in_credits = Column(String(250), nullable=False)
#     crew = Column(String(250), nullable=False)
#     hyperdrive_rating = Column(String(250), nullable=False)
#     MGLT = Column(String(250), nullable=False)
#     length = Column(String(250), nullable=False)
#     manufacturer = Column(String(250), nullable=False)
#     max_atmosfering_speed = Column(String(250), nullable=False)
#     model = Column(String(250), nullable=False)
#     name = Column(String(250), nullable=False)
#     passengers = Column(String(250), nullable=False)
#     films = Column(String(250), nullable=False)
#     pilots = Column(String(250), nullable=False)
#     starship_class = Column(String(250), nullable=False)

# class Planets(Base):
#     __tablename__ = 'planets'
#     id_planet = Column(Integer, ForeignKey('planet.id_planet'))
#     climate = Column(String(250), nullable=False)
#     films = Column(String(250), nullable=False)
#     gravity = Column(String(250), nullable=False)
#     name = Column(String(250), nullable=False)
#     orbital_period = Column(String(250), nullable=False)
#     population = Column(String(250), nullable=False)
#     residents = Column(String(250), nullable=False)
#     rotation_period = Column(String(250), nullable=False)
#     surface_water = Column(String(250), nullable=False)
#     terrain = Column(String(250), nullable=False)

# class Participation(Base):
#     __tablename__ = 'participation'
#     id_participation = Column(Integer, primary_Key=True)
#     id_films = relationship(Films)
#     id_character = relationship(Character)
#     id_planet = relationship(Planets)
#     id_starship = relationship(Starship)

# class Favorites(Base):
#     __tablename__ = 'favorites'
#     id_user = Column(Integer, primary_key=True)  
#     id_character = relationship(Character)
#     id_starship = relationship(Starship)
#     id_planet = relationship(Planets)
#     id_films = relationship(Films)

# class User(Base):
#     __tablename__ = 'user'
#     id_user = Column(Integer, primary_key=True)  
#     email = Column(Integer, primary_key=True)
#     password = Column(Integer, primary_key=True)


    

# # class Address(Base):
# #     __tablename__ = 'address'
# #     id = Column(Integer, primary_key=True)
# #     street_name = Column(String(250))
# #     street_number = Column(String(250))
# #     post_code = Column(String(250), nullable=False)
# #     person_id = Column(Integer, ForeignKey('person.id'))
# #     person = relationship(Character)

#     def to_dict(self):
#         return {}

# ## Draw from SQLAlchemy base
# render_er(Base, 'diagram.png')
