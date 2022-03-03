#!/usr/bin/python3
""" Place Module for HBNB project """
import models
from models.review import Review
from models.amenity import Amenity
from models.base_model import BaseModel
from models.base_model import Base
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv
storage_comm = getenv("HBNB_TYPE_STORAGE")

Table('place_amenity', Base.metadata,
      Column('place_id', ForeignKey('places.id'), nullable=False,
             primary_key=True),
      Column('amenity_id', ForeignKey('amenities.id'), nullable=False,
             primary_key=True))


class Place(BaseModel, Base):
    """ A place to stay """
    __tablename__ = 'places'
    city_id = Column(String(60), ForeignKey('cities.id'), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    name = Column(String(128),  nullable=False)
    description = Column(String(1024),  nullable=True)
    number_rooms = Column(Integer, default=0, nullable=False)
    number_bathrooms = Column(Integer, default=0, nullable=False)
    max_guest = Column(Integer, default=0, nullable=False)
    price_by_night = Column(Integer, default=0, nullable=False)
    latitude = Column(Float, nullable=True)
    longitude = Column(Float, nullable=True)
    amenity_ids = []

    if storage_comm == "db":
        reviews = relationship("Review", cascade="all, delete",
                               backref="place")
        amenities = relationship("Amenity", secondary='place_amenity',
                                 viewonly=False, backref="place_amenities")
    else:
        @property
        def reviews(self):
            """Getter for reviews in a Place"""
            review_inst = []
            all_reviews = models.storage.all(Review)
            for review in all_reviews.values():
                if review.place_id == self.id:
                    review_inst.append(review)
            return review_inst

        @property
        def amenities(self):
            """Getter for Amenities in a Place"""
            amenities_inst = []
            all_amenities = models.storage.all(Amenity)
            for amenity in all_amenities.values():
                if self.id == amenity.place_id:
                    amenities_inst.append(amenity)
            return amenities_inst

        @amenities.setter
        def amenities(self, obj):
            """setter for amenities in a Place"""
            if isinstance(obj, Amenity):
                self.append(obj)
