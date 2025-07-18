#!/usr/bin/python
# -*- coding: utf-8 -*-

from code.EnemyShot import EnemyShot
from .entity import Entity
from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, WIN_WIDTH


class Enemy(Entity):

    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = int(ENTITY_SHOT_DELAY[self.name])

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]  # Move the background to the left by 1 pixel, for example
        pass
    
    def shoot(self):
        self.shot_delay -=1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

