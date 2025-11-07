import pygame
from UI_States import ui_states

def initial_UI():
    pygame.init()
    
    font = pygame.font.Font(pygame.font.get_default_font(), 40)

    WIDTH = 800
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    window.fill((0,0,0))

    pygame.display.set_caption('Multiversal Warfare')

    pygame.display.flip()

    return window, font

def draw_window(window, state, font):
    
    
    ui_states.select_state(window, state, font)
    
        
        
        
    pygame.display.flip()








    return window
