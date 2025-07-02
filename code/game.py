#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import MENU_OPTION, WIN_WIDTH, WIN_HEIGHT #importar as constantes de tamanho da janela
from code.Score import Score
from code.level import Level
from code.menu import Menu
# from code.menu import Menu #importar a classe menu do arquivo menu.py

class Game:
    def __init__(self):
        pygame.init() # Set up the display
        self.window = pygame.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT)) #tamanho da janela
        pygame.display.set_caption('MONTANHAS ATIRADEIRO') #titulo da janela

    def run(self, ):    
        while True: #deixa janela aberta enquanto true
            
            
            
            
            score = Score(self.window) #chama a classe Score e passa a janela como parametro
            menu = Menu(self.window)
            menu_return = menu.run() #chama a classe menu e executa o metodo run
            
            
            if menu_return in [MENU_OPTION[0],MENU_OPTION[1],MENU_OPTION[2]]: #se o usuario escolher a opcao de novo jogo 1 jogador
                player_score = [0, 0] #inicializa a pontuacao dos jogadores (1 e 2)
                level = Level(self.window, 'Level1', menu_return, player_score) #chama a classe level e passa a janela e o numero de jogadores
                level_return = level.run(player_score) #chama o metodo run da classe level
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)  #chama a classe level e passa a janela e o numero de jogadores
                    level_return = level.run(player_score) #chama o metodo run da classe level
                    if level_return:
                        score.save(menu_return, player_score)
                    
            elif menu_return == MENU_OPTION[3]:
                score.show() #chama o metodo show da classe Score para mostrar a pontuacao

            elif menu_return == MENU_OPTION[4]:
                pygame.quit()
                quit() #fecha a janela e encerra o pygame
            else:
                
                pass
            
            
            
            

