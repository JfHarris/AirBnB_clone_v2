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

our_insts = (City, State, User, Place, Amenity, Review)


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
        """Initializes the MySQL database"""
        HBNB_ENV = getenv('HBNB_ENV')
        HBNB_MYSQL_USER = getenv('HBNB_MYSQL_USER')
        HBNB_MYSQL_PWD = getenv('HBNB_MYSQL_PWD')
        HBNB_MYSQL_HOST = getenv('HBNB_MYSQL_HOST')
        HBNB_MYSQL_DB = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            HBNB_MYSQL_USER, HBNB_MYSQL_PWD,
            HBNB_MYSQL_HOST, HBNB_MYSQL_DB, HBNB_ENV), pool_pre_ping=True)

        if HBNB_ENV == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Retrieves all objects requested V2"""
        all_dict = {}
        if cls is None:
            for inst in our_insts:
                for obj in self.__session.query(inst):
                    all_dict["{}.{}".format(inst.__name__,obj.id)] = obj
        elif cls in our_insts:
            for obj in self.__session.query(cls):
                all_dict["{}.{}".format(cls.__name__, obj.id)] = obj
        return all_dict

    def new(self, obj):
        """adds an object"""
        if obj is not None:
            self.__session.add(obj)
            self.save()

    def save(self):
        """saves an object to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """removes an object"""
        if obj is not None:
            del obj
            self.save()

    def reload(self):
        """Retrieves all objects on start-up"""
        Base.metadata.create_all(self.__engine)
        session_rel = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(session_rel)
        self.__session = Session

    def close(self):
        """Closes session"""
        self.__session.close()
