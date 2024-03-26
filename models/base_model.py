#!/usr/bin/python3
''' Module for BaseModel '''
import uuid
from datetime import datetime
import models


class BaseModel:
    '''
    Define BaseModel class

    Attributes:
        id (str): The unique identifier for each BaseModel instance
        created_at (datetime): The datetime when the instance was created
        updated_at (datetime): The datetime when the instance was updated

    Methods:
        __init__: Initializes a new instance of the BaseModel class
        __str__: Returns the string representation of the BaseModel instance
        save: Updates the 'updated_at' attribute with the current datetime
        to_dict: Converts the BaseModel instance
                 into a dictionary representation
    '''
    def __init__(self, *args, **kwargs):
        ''' BaseModel constructor '''
        if kwargs:
            for key, value in kwargs.items():
                if (key != "__class__"):
                    if (key == "created_at" or key == "updated_at"):
                        value = datetime.fromisoformat(value)
                    elif value.isdigit():
                        value = int(value)
                    elif value.replace('.', '', 1).isdigit():
                        value = float(value)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self. created_at = self.updated_at = datetime.now()
            models.storage.new(self)

    def __str__(self):
        ''' Returns the string representation of BaseModel '''
        return "[{}] ({}) {}".format(type(self).__name__,
                                     self.id, self.__dict__)

    def save(self):
        ''' Updates updated_at with the current datetime '''
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        ''' Returns a dictionary containing all keys/values of __dict__ '''
        res = self.__dict__.copy()
        res['__class__'] = type(self).__name__
        res['created_at'] = self.created_at.isoformat()
        res['updated_at'] = self.updated_at.isoformat()
        return res
