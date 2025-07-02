#!/usr/bin/python
# -*- coding: utf-8 -*-
from tkinter.font import Font
import pygame
import pygame.image

from code.Const import WIN_WIDTH , WIN_HEIGHT, C_ORANGE, C_WHITE, C_YELLOW, MENU_OPTION

class Menu:
    def __init__(self, window):
        self.window = window # Initialize menu items, background, etc.
        self.surf = pygame.image.load('asset/MenuBg.png').convert_alpha()  # Load the background image for the menu
        self.rect = self.surf.get_rect(left=0, top=0)   # Get the rectangle of the surface for positioning

    def run(self, ):
        menu_option = 0 # Initialize the selected menu option
        pygame.mixer_music.load('asset/Menu.mp3') #carregar a musica de fundo
        pygame.mixer_music.play(-1) #tocar a musica de fundo em loop infinito
        while True:
####################---DRAW IMAGES---###################################
            self.window.blit(source=self.surf, dest=self.rect)
            self.menu_text(text_size=50, text="Mountanhas", text_color=C_ORANGE, text_center_pos=((WIN_WIDTH / 2), 70)) # Draw the title
            self.menu_text(text_size=50, text="Atiradeiro", text_color=C_ORANGE , text_center_pos=((WIN_WIDTH / 2), 120)) # Draw the subtitle
            
            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(25, MENU_OPTION[i], C_YELLOW, ((WIN_WIDTH / 2), 200 + 25 * i)) # Draw menu options
                else:
                    self.menu_text(25, MENU_OPTION[i], C_WHITE, ((WIN_WIDTH / 2), 200 + 25 * i)) # Draw menu options
            
            pygame.display.flip()        # Handle menu events and logic here
        # For example, check for button clicks, navigate through options, etc.

####################---EVENTOS - teclas ---##############################
        
            ###Check for all events ---- tirar bug da window para poder fechar a janela
            for event in pygame.event.get(): #pegar eventos e ficar checando
                if event.type == pygame.QUIT: #apenas o evento de fechar a janela
                    pygame.quit() #close window
                    exit() #end pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN: # If the down arrow key is pressed, move to the next menu option
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0 # Wrap around to the first option
                
                
                    if event.key == pygame.K_UP: # If the up arrow key is pressed, move to the next menu option
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) # Wrap around to the last option
                            
                    if event.key == pygame.K_RETURN: # If the enter key is pressed, select the current menu option
                        return MENU_OPTION[menu_option] # Return the selected menu option
                    


    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Gabriola", size=text_size)
        text_surf: pygame.Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: pygame.Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)