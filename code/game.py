#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT #importar as constantes de tamanho da janela
from code.level import Level
from code.menu import Menu
# from code.menu import Menu #importar a classe menu do arquivo menu.py

class Game:
    def __init__(self):
        pygame.init() # Set up the display
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #tamanho da janela
        pygame.display.set_caption('MONTANHAS ATIRADEIRO') #titulo da janela

    def run(self):    
        while True: #deixa janela aberta enquanto true
            menu = Menu(self.window)
            menu_return = menu.run() #chama a classe menu e executa o metodo run
            
            
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]: #se o usuario escolher a opcao de novo jogo 1 jogador
                level = Level(self.window, 'Level1', menu_return) #chama a classe level e passa a janela e o numero de jogadores
                level_return = level.run() #chama o metodo run da classe level
            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit() #fecha a janela e encerra o pygame
            else:
                
                pass
            
            
            
            

