#!/usr/bin/python3
''' Module for FileStorage '''
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class FileStorage:
    '''
    Define FileStorage class

    Attributes:
        __file_path (str): The path to the JSON file
        __objects (dict): Dictionary containing objects

    Methods:
        __init__: Initializes the FileStorage instance
        all: Returns the dictionary of objects
        new: Adds a new object to the dictionary of objects
        save: Serializes the dictionary of objects into a JSON file
        reload: Deserializes the JSON file into the dictionary of objects
    '''
    def __init__(self, file_path='file.json', objects={}):
        ''' FileStorage constructor '''
        self.__file_path = file_path
        self.__objects = objects

    def all(self):
        ''' returns the dictionary __objects '''
        return self.__objects

    def new(self, obj):
        ''' sets in __objects the obj with key <obj class name>.id '''
        key = obj.__class__.__name__ + '.' + obj.id
        self.__objects[key] = obj

    def save(self):
        ''' serializes __objects to the JSON file (path: __file_path) '''
        json_obj = {}

        for k in self.__objects:
            json_obj[k] = self.__objects[k].to_dict()

        with open(self.__file_path, 'w') as file:
            json.dump(json_obj, file)

    def reload(self):
        '''
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists; otherwise, do nothing.
        '''
        try:
            with open(self.__file_path, 'r') as file:
                for k, v in json.load(file).items():
                    val = eval(v["__class__"])(**v)
                    self.__objects[k] = val
        except FileNotFoundError:
            pass
