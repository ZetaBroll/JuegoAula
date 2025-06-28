#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod

from code.Const import ENTITY_HEALTH


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('asset/' + name + '.png').convert_alpha()  # Load the image from the assets folder
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0  # Get the rectangle
        self.health = ENTITY_HEALTH[self.name]  # Health of the entity, default is 100

@abstractmethod  # é um decorator que indica que este método deve ser implementado por subclasses
def move(self):
    pass
