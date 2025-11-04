import pygame

def initial_UI():
    pygame.init()

    WIDTH = 800
    HEIGHT = 600
    window = pygame.display.set_mode((WIDTH, HEIGHT))

    window.fill((0,0,0))

    pygame.display.set_caption('Multiversal Warfare')

    pygame.display.flip()

    return window

def draw_window(window, state):

    if state == 0:
        window.fill((0,0,0))
        pygame.draw.rect(window, (255,255,255), pygame.Rect(0,0,350, 400))
        pygame.draw.rect(window, (255,0,0), pygame.Rect(0,425,350, 175))
        pygame.draw.rect(window, (0,255,0), pygame.Rect(375,0,425, 600))
        
    if state == 1:
        window.fill((255, 255, 255))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))
        
    if state == 2:
        window.fill((255, 0, 0))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))
        
    if state == 3:
        window.fill((0, 255, 0))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))
        
        
        
    pygame.display.flip()








    return window
