import pygame
from UI_States import ui_states
from time import sleep

def initial_UI():
    pygame.init()
    
    font = pygame.font.Font(pygame.font.get_default_font(), 35)

    WIDTH = 800
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    window.fill((0,0,0))

    pygame.display.set_caption('Multiversal Warfare')

    pygame.display.flip()

    return window, font

def draw_window(window, state, font, campaign_re, Player_id):
    
    
    ui_states.select_state(window, state, font, campaign_re, Player_id)
    
        
        
        
    pygame.display.flip()

def init_draw_battle(window, characters):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    ui_states.Battle_Background(window)
    ui_states.init_Charatcer_names_and_health(window, characters, font)



    pygame.display.flip()

def draw_battle(window, characters):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    ui_states.Battle_Background(window)
    ui_states.Charatcer_names_and_health(window, characters, font)











def Draw_abilities(window, abilities, character):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)



    for i in range(3):
        if i == 1 and character.character._special_cooldown > 0:
            pass
        elif i == 2 and character.character._ultimate_cooldown > 0:
            pass
        else:

            text = abilities[i]
            text = font.render(text, True, (255,255,255))
            pygame.draw.rect(window, (50,50,50), pygame.Rect(i*250 + 50, 560, 200, 20))
            window.blit(text, (i*250 + 100, 560))

    pygame.display.flip()

    return window

def draw_win(window):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render('Victory', True, (255,255,255))
    window.blit(text, (330, 300))
    pygame.display.flip()
    sleep(5)

def draw_loss(window):
    font = pygame.font.Font(pygame.font.get_default_font(), 20)
    text = font.render('Defeat', True, (255,255,255))
    window.blit(text, (330, 300))
    pygame.display.flip()
    sleep(5)

def draw_target(window, target):
    pygame.draw.rect(window, (0,0,255), pygame.Rect(15 + (150 * target), 85, 130, 80), 10)
