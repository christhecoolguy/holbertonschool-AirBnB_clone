#!/usr/bin/python3
""" Amenity model module """
from models.base_model import BaseModel


class Amenity(BaseModel):
    """ Amenities information """

    name = ""

    def __init__(self, *, **):
        super().__init__(*, **)

    def to_dict(self):
        return super(Amenity, self).to_dict()
