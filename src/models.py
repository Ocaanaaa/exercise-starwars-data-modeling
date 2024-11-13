import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(200), unique=True, nullable=False)
    first_name = Column(String(200))
    last_name = Column(String(200))
    email = Column(String(200), unique=True)

    favorites = relationship("Favorite", back_populates="user")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    external_id = Column(Integer, unique=True)
    name = Column(String(200))
    diameter = Column(Integer)
    climate = Column(String(200))

    favorites = relationship("Favorite", back_populates="planet")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    external_id = Column(Integer, unique=True)
    name = Column(String(200))
    height = Column(Integer)
    weight = Column(Integer)
    skin_color = Column(String(200))

    favorites = relationship("Favorite", back_populates="character")

class Vehicle(Base):
    __tablename__ = 'vehicle'
    id = Column(Integer, primary_key=True)
    external_id = Column(Integer, unique=True)
    name = Column(String(200))
    speed = Column(Integer)
    model = Column(String(200))
    color = Column(String(200))

    favorites = relationship("Favorite", back_populates="vehicle")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("User", back_populates="favorites")

    character_id = Column(Integer, ForeignKey("character.external_id"))
    character = relationship("Character", back_populates="favorites")

    planet_id = Column(Integer, ForeignKey("planet.external_id"))
    planet = relationship("Planet", back_populates="favorites")

    vehicle_id = Column(Integer, ForeignKey("vehicle.external_id"))
    vehicle = relationship("Vehicle", back_populates="favorites")

    def to_dict(self):
        
        return {
            "id": self.id,
            "user_id": self.user_id,
            "character_id": self.character_id,
            "planet_id": self.planet_id,
            "vehicle_id": self.vehicle_id
        }


render_er(Base, 'diagram.png')
