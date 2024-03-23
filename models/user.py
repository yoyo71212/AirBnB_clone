#!/usr/bin/python3
''' User class that inherits from BaseModel '''

from models.base_model import BaseModel


class User(BaseModel):
    '''
    User class

    Attributes:
        email (str): The email address of the user
        password (str): The password of the user
        first_name (str): The first name of the user
        last_name (str): The last name of the user

    Methods:
        __init__: Initializes a new User instance
    '''
    def __init__(self, *args, **kwargs):
        ''' User constructor '''
        super().__init__(*args, **kwargs)
        self.email = kwargs.get('email', '')
        self.password = kwargs.get('password', '')
        self.first_name = kwargs.get('first_name', '')
        self.last_name = kwargs.get('last_name', '')
