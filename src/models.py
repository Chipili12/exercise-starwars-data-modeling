import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Usuario(Base):
    __tablename__ = 'Usuario'
    # Here we define columns for the table Usuario
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    first_name = Column(String(250), nullable=False)
    last_name = Column(String(250), nullable=False)
    password = Column(String(250), nullable=False)
    username = Column(String(250), nullable=False)

class Favorito(Base):
    __tablename__ = 'Favorito'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    personaje_id = Column(String(250))
    nave_id = Column(String(250))
    planeta_id = Column(String(250))
    Usuario_id = Column(Integer, ForeignKey('Usuario.id'))
    Usuario = relationship(Usuario)

class Personaje(Base):
    __tablename__ = 'Personaje'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    birth_year = Column(String(250))
    eye_color = Column(String(250))
    gender = Column(String(250))
    hair_color = Column(String(250))
    height = Column(String(250))
    mass = Column(String(250))
    name = Column(String(250))
    planet_id = Column(String(250))
    skin_color = Column(String(250))

    Usuario_id = Column(Integer, ForeignKey('Favorito.personaje_id'))
    Usuario = relationship(Favorito)
class Nave(Base):
    __tablename__ = 'Nave'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    cost_in_credits = Column(String(250))
    crew = Column(String(250))
    length = Column(String(250))
    manufacturer = Column(String(250))
    max_atmospheric_speed = Column(String(250))
    name = Column(String(250))
    passengers = Column(String(250))
    vehicle_class = Column(String(250))
    Usuario_id = Column(Integer, ForeignKey('Favorito.nave_id'))
    Usuario = relationship(Favorito)
class Planeta(Base):
    __tablename__ = 'Planeta'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    climate = Column(String(250))
    diameter = Column(String(250))
    gravity = Column(String(250))
    name = Column(String(250))
    orbital_period = Column(String(250))
    population = Column(String(250))
    rotation_speed = Column(String(250))
    surface_water = Column(String(250))
    terrain = Column(String(250))
    Usuario_id = Column(Integer, ForeignKey('Favorito.planeta_id'))
    Usuario = relationship(Favorito)


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
