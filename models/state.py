#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
storage_comm = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel):
    """ State class """
    __tablename__ = 'states'
    if storage_comm == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        @property
        def cities(self):
            city_inst = []
            all_cities = models.storage.all(City)
            for city in city_inst.values():
                if city.state_id == self.id:
                    city_inst.append(city)
            return city_inst
