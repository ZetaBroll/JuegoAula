#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.Const import WIN_WIDTH, WIN_HEIGHT #importar as constantes de tamanho da janela
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
            menu.run() #chama a classe menu e executa o metodo run
            pass
        
            
            
            
            

