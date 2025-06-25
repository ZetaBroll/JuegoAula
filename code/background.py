#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.Const import ENTITY_SPEED, WIN_WIDTH
from code.entity import Entity


class Background(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)  # Call the constructor of the parent class Entity
        

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move the background to the left by 1 pixel, for example
        if self.rect.right <= 0:  # If the background goes off the left side
            self.rect.left = WIN_WIDTH

