#!/usr/bin/python3
"""
cities
"""
from modles.base_model import BaseModel


class City(BaseModel):

    """
    info airbnb city 
    public state id string empty it is state id name empty
    """
    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def to_dict(self):
        return super (City, self).to_dict()
