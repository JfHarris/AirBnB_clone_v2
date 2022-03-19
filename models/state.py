#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel
from models.base_model import Base
import models
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv
from models.city import City
storage_comm = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """ State class """
    if models.storage_comm == "db":
        __tablename__ = 'states'
        name = Column(String(128), nullable=False)
        cities = relationship("City", cascade="all, delete,\
            delete-orphan", backref="state")
    else:
        name = ""

    def __init__(self, *args, **kwargs):
        """
        init state
        """
        super().__init__(*args, **kwargs)

    if models.storage_comm != "db":
        @property
        def cities(self):
            """
            Getter for Cities in a State
            """
            city_inst = []
            all_cities = models.storage.all(City)
            for city in all_cities.values():
                if city.state_id == self.id:
                    city_inst.append(city)
            return city_inst
