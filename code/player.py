#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame

from code.Const import ENTITY_SHOT_DELAY, ENTITY_SPEED, PLAYER_KEY_DOWN, PLAYER_KEY_LEFT, PLAYER_KEY_RIGHT, PLAYER_KEY_SHOOT, PLAYER_KEY_UP, WIN_HEIGHT, WIN_WIDTH
from code.PlayerShot import PlayerShot
from .entity import Entity
from code.entity import Entity


class Player(Entity):
    def __init__(self, name:str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = int(ENTITY_SHOT_DELAY[self.name])

        

    def move(self, ):
        # Implement player movement logic here
        pressed_key = pygame.key.get_pressed()
        if pressed_key[PLAYER_KEY_LEFT[self.name]] and self.rect.left > 0:
            self.rect.centerx -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_RIGHT[self.name]] and self.rect.right < WIN_WIDTH:
            self.rect.centerx += ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_UP[self.name]] and self.rect.top > 0:
            self.rect.centery -= ENTITY_SPEED[self.name]
        if pressed_key[PLAYER_KEY_DOWN[self.name]] and self.rect.bottom < WIN_HEIGHT:
            self.rect.centery += ENTITY_SPEED[self.name]
        pass


    def shoot(self):        # Implement player shooting logic here
        self.shot_delay -=1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            pressed_key = pygame.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:  # Assuming spacebar is used for shooting
                return PlayerShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))