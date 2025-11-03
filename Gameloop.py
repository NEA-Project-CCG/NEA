import pygame

from UI import initial_UI



def gameloop():





    initial_UI()

    running = True
    while running:





















        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                print(pos)
                type = pygame.mouse.get_pressed()[0]
                print(type)




            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()





