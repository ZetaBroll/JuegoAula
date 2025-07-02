

from datetime import datetime
import sys
from tkinter.font import Font
from unicodedata import name
import pygame

from code.Const import C_WHITE, C_YELLOW, MENU_OPTION, SCORE_POS
from code.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window # Initialize menu items, background, etc.
        self.surf = pygame.image.load('asset/ScoreBg.png').convert_alpha()  # Load the background image for the menu
        self.rect = self.surf.get_rect(left=0, top=0) 
        pass
    
    
    
    def save(self, game_mode: str, player_score:list[int]):
        pygame.mixer_music.load('asset/Score.mp3') #carregar a musica de fundo
        pygame.mixer_music.play(-1) #tocar a musica de fundo em loop infinito
        db_proxy = DBProxy('DBScore')
        name =''  # Initialize an empty name string
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!!', C_YELLOW, SCORE_POS['Title']) # Draw the title
            if game_mode == MENU_OPTION[0]: #se o jogo for 1 jogador
                score = player_score[0] #pega a pontuacao do jogador 1 no indice zero da lista
                text = 'Enter Player 1 name (4 Characters):'
                
            if game_mode == MENU_OPTION[1]: #se o jogo for 1 jogador
                score = (player_score[0] + player_score[1]) /2#pega a pontuacao do jogador 1 no indice zero da lista
                text = 'Enter Team name (4 Characters):'
                
                
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]: #se o jogador 1 tiver mais pontos que o jogador 2
                    score = player_score[0]
                    text = 'Enter Player 1 name (4 Characters):'
                else: #se o jogador 2 tiver mais pontos que o jogador 1
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 Characters):'
            self.score_text(30, text, C_WHITE, SCORE_POS['EnterName']) # Draw the title
            
            
            for event in pygame.event.get(): ## Checar eventos
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN: ##if a key is pressed
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_fomatted_date() })
                        self.show()  # Show the score screen after saving
                        return
                    elif event.key == pygame.K_BACKSPACE:  # If the backspace key is pressed, remove the last character
                        name = name[:-1]  # Remove the last character from the name
                    else:
                        if len(name) < 4:
                            name += event.unicode  # Add the pressed key's character to the name
            self.score_text(20, name, C_WHITE, SCORE_POS['Name'])
                            
                        
            pygame.display.flip()  # Update the display
            
            pass
        pass
    
    def show(self): ## tela score se clicada do menu
        pygame.mixer_music.load('asset/Score.mp3') #carregar a musica de fundo
        pygame.mixer_music.play(-1) #tocar a musica de fundo em loop infinito
        self.window.blit(source=self.surf, dest=self.rect)
        self.score_text(48, 'TOP 10 SCORE', C_YELLOW, SCORE_POS['Title']) 
        self.score_text(20, 'NAME           SCORE                            DATE         ', C_YELLOW, SCORE_POS['Label'])
        
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()  # Retrieve the top 10 scores from the database
        db_proxy.close()  # Close the database connection after retrieving scores
        
        clock = pygame.time.Clock()
        
        for player_score in list_score:
            id_, name, score, date = player_score  # Unpack the player score tuple
            self.score_text(25, f'                            {   name}               {score :06d}                       {date}', C_YELLOW, SCORE_POS[list_score.index(player_score)])
            
        while True:
            for event in pygame.event.get(): ## Checar eventos
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                    
                if event.type == pygame.KEYDOWN: ##if a key is pressed
                    if event.key == pygame.K_ESCAPE:
                        return
            pygame.display.flip()  # Update the display
            
        
        
        
        
        
        ## FORMATAÇÃO DO TEXTO DO MENU ##
    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        Font = pygame.font.SysFont(name="Gabriola", size=text_size)
        Surface = Font.render(text, True, text_color).convert_alpha()
        Rect = Surface.get_rect(center=text_center_pos)
        self.window.blit(source=Surface, dest=Rect)
        
        
def get_fomatted_date():  ## horario e data formatados ##
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%Y")
    return f"{current_time} - {current_date}"