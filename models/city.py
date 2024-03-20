#!/usr/bin/python3
''' City module '''

from models.base_model import BaseModel


class City(BaseModel):
    ''' City class '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.state_id = kwargs.get('state_id', '')
        self.name = kwargs.get('name', '')
