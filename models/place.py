#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
storage_comm = getenv("HBNB_TYPE_STORAGE")


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('states.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(128),  nullable=False)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    #idk if any of this is right
    if storage_comm == "db":
        reviews = relationship("Review", cascade="all, delete", backref="user")
    else:
        @property
        def reviews(self):
            review_inst = []
            all_cities = models.storage.all(Review)
            for review in review_inst.values():
                if review.state_id == self.id:
                    review_inst.append(review)
            return review_inst
