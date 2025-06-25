#!/usr/bin/python
# -*- coding: utf-8 -*-

import pygame
from code.entity import Entity
from code.entityFactory import EntityFactory  # Importing the Entity class from entity module


class Level:
    def __init__(self, window, name, game_mode):
        self.window = window
        self.name = name
        self.gamemode = game_mode #modo de jogo, 1 ou 2 jogadores
        self.entity_list : list[Entity] = [] #lista de entidades do jogo, como inimigos, jogadores, etc.
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Adiciona o background do level 1 à lista de entidades

    def run(self, ):
        while True:
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            pygame.display.flip()# Update the display
        pass
