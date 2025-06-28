#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame.image
from abc import ABC, abstractmethod

from code.Const import ENTITY_DAMAGE, ENTITY_HEALTH, ENTITY_SCORE


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('asset/' + name + '.png').convert_alpha()  # Load the image from the assets folder
        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0  # Get the rectangle
        self.health = ENTITY_HEALTH[self.name]  # Health of the entity, default is 100
        self.damage = ENTITY_DAMAGE[self.name]  # Damage of the entity, default is 10
        self.score = ENTITY_SCORE[self.name]
        self.last_dmg = 'none'  # Last entity that caused damage to this entity, default is 'none'

@abstractmethod  # é um decorator que indica que este método deve ser implementado por subclasses
def move(self):
    pass
