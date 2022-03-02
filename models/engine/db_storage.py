#!/usr/bin/python3
"""
New storage engine
"""


import models
from models.amenity import Amenity
from models.base_model import BaseModel, Base
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session
from os import getenv

class_dict = {
    "Amenity": Amenity,
    "City": City,
    "Place": Place,
    "State": State,
    "User": User,
    "Review": Review
}

class DBStorage():
    """
    New storage engine
    Private attrs: __engine = None, __session = None
    Public instabce methods: __init__(self):, all(self,cls=None):
        new(self, obj):, save(self):, delete(self, obj=None):
        reload(self):,
    """

    __engine = None
    __session = None

    def __init__(self):
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(HBNB_ENV, HBNB_MYSQL_USER, HBNB_MYSQL_PWD, HBNB_MYSQL_HOST, HBNB_MYSQL_DB), pool_pre_ping=True)
        if HBNB_ENV == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        all_dict = {}
        for exmpl in class_dict:
            if cls is None or cls == exmpl:
                our_objs = self.__session.query(class_dict[exmpl]).all()
                for obj in our_objs:
                    key = obj.__class__.__name__ + "." + obj.id
                    all_dict[key] = obj
        return (all_dict)

    def new(self, obj):
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def save(self):
        self.__session.commit()

    def delete(self, obj=None):
        if obj is not None:
            del obj
            self.save()

    def reload(self):
        Base.metadata.create_all(self.__engine)
        Session = scoped_session(sessionmaker(bind=self.__engine, expire_on_commit=False))

    def close(self):
        self.__session.close()
