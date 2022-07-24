#!/usr/bin/python3
from models.rectangle import Rectangle
class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(id,x,y,width,height)
        self.width = size
        self.height = size
        self.id = id
        self.x = x
        self.y = y
    def __str__(self):
        return ("[Square] ({}) {}/{} - {}".format(id,x,y,width))
