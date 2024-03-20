#!/usr/bin/python3
''' State module '''

from models.base_model import BaseModel


class State(BaseModel):
    ''' State class '''
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = kwargs.get('name', '')
