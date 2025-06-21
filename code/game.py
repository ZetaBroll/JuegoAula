#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from code.menu import Menu
# from code.menu import Menu #importar a classe menu do arquivo menu.py

class Game:
    def __init__(self):
        pygame.init() # Set up the display
        self.window = pygame.display.set_mode(size=(600, 480))

    def run(self):
        print('Setup started')
        while True: #deixa janela aberta enquanto true
            menu = Menu(self.window)
            menu.run() #chama a classe menu e executa o metodo run
            pass
        
            
            
            
            
            # Check for all events
            #for event in pygame.event.get(): #pegar eventos e ficar checando
            #    if event.type == pygame.QUIT: #apenas o evento de fechar a janela
            #        pygame.quit() #close window
            #        exit() #end pygame
