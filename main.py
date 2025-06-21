import pygame

print('Setup started')
pygame.init()
# Set up the display
window = pygame.display.set_mode(size=(600, 480))


print('Loop sstared')
while True: #deixa janela aberta enquanto true
    # Check for all events
    for event in pygame.event.get(): #pegar eventos e ficar checando
        if event.type == pygame.QUIT: #apenas o evento de fechar a janela
            pygame.quit() #close window
            exit() #end pygame
