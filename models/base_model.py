#!/usr/bin/python3
''' Module for BaseModel '''
import uuid
from datetime import datetime


class BaseModel:
    ''' Define BaseModel class '''
    def __init__(self, *args, **kwargs):
        ''' BaseModel constructor '''
        if kwargs:
            for key, value in kwargs.items():
                if (key != "__class__"):
                    if (key == "created_at" or key == "updated_at"):
                        value = datetime.fromisoformat(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self. created_at = self.updated_at = datetime.now()

    def __str__(self):
        ''' Returns the string representation of BaseModel '''
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' Updates updated_at with the current datetime '''
        self.updated_at = datetime.now()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__ '''
        res = self.__dict__.copy()
        res['__class__'] = type(self).__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res
