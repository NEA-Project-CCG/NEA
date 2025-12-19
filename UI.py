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

def draw_window(window, state, font, campaign_re):
    
    
    ui_states.select_state(window, state, font, campaign_re)
    
        
        
        
    pygame.display.flip()

def draw_battle(window, characters):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    ui_states.Battle_Background(window)
    ui_states.Charatcer_names_and_health(window, characters, font)



    pygame.display.flip()









    return window

def Draw_abilities(window):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    abilites = ["Basic", "Special", "Ultimate"]
    for i in range(3):
        text = abilites[i]
        text = font.render(text, True, (255,255,255))
        pygame.draw.rect(window, (50,50,50), pygame.Rect(i*250 + 50, 560, 200, 20))
        window.blit(text, (i*250 + 100, 560))

    return window
