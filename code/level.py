#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from random import random
import random
import sys
from tkinter.font import Font
import pygame
from code.Const import C_CYAN, C_GREEN, C_WHITE, ENTITY_HEALTH, EVENT_ENEMY, MENU_OPTION, SPAWN_TIME, WIN_HEIGHT
from code.enemy import Enemy
from code.entity import Entity
from code.entityFactory import EntityFactory
from code.entityMediator import EntityMediator
from code.player import Player  # Importing the Entity class from entity module


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000 # Tempo de duração da fase em milissegundos (20 segundos)
        self.window = window
        self.name = name
        self.game_mode = game_mode #modo de jogo, 1 ou 2 jogadores
        self.entity_list : list[Entity] = [] #lista de entidades do jogo, como inimigos, jogadores, etc.
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))  # Adiciona o background do level 1 à lista de entidades
        self.entity_list.append(EntityFactory.get_entity('Player1'))  # Adiciona o jogador à lista de entidades
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))  # Adiciona o segundo jogador se o modo de jogo for cooperativo
        pygame.time.set_timer(EVENT_ENEMY, SPAWN_TIME)  # Set a timer to spawn enemies every 3 seconds

    def run(self, ):
        pygame.mixer_music.load(f'asset/{self.name}.mp3')  # Load the background music for the level
        pygame.mixer_music.play(-1)  # Play the background music in an infinite loop
        clock = pygame.time.Clock()  # Create a clock to control the frame rate
        while True:
            clock.tick(60)  # Limit the frame rate to 60 FPS
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))  # Randomly choose an enemy type to spawn
                    self.entity_list.append(EntityFactory.get_entity(choice))  # Add the chosen enemy to the entity list
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:  # Check if the shoot method returned a shot entity
                        self.entity_list.append(shoot)  # If the entity is a player or enemy, call its shoot method to handle shooting logic





             #printed text --- HUD DO JOGO ---
             
            if ent.name == 'Player1':
                self.level_text(14, f'Player1 - Health: {ent.health} | Score: {ent.score} ' , C_GREEN, (10,25))  # Display Player1's health in green
            if ent.name == 'Player2':
                self.level_text(14, f'Player2 - Health: {ent.health} | Score: {ent.score} ' , C_CYAN, (10, 45))

            self.level_text(14, f'{self.name} - Timeout:{self.timeout / 1000 :.1f}s', C_WHITE, (10, 5)) #tempo de duração da fase
            self.level_text(14, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 35))  # Display the current FPS
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20)) #qntde de entidades criadas na tela
        
            pygame.display.flip()  # Update the display
            
            
            
            
            
            
            ## collisions ##
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Verify collisions between entities
            EntityMediator.verify_health(entity_list=self.entity_list)
        pass



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Gabriola", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(top=text_pos[1] , left=text_pos[0])  # Get the rectangle of the text surface for positioning
        self.window.blit(source=text_surf, dest=text_rect)