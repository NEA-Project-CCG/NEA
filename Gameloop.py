import pygame
from UI import initial_UI, draw_window



def gameloop():

    state = 0



    window = initial_UI()

    running = True
    while running:





















        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]
                
     

                Mtype = pygame.mouse.get_pressed()[0]
                
                if state == 0:
                    if Mtype == 1:
                        if pos_x >= 0 and pos_x < 350 and pos_y >= 0 and pos_y < 400:
                            state = 1
               
                            
                        elif pos_x >= 0 and pos_x < 350 and pos_y >= 425 and pos_y <= 600:
                            state = 2
                            
                        elif pos_x >= 375 and pos_x < 800 and pos_y >= 0 and pos_y <= 600:
                            state = 3
                        
                elif state != 0:
                    if Mtype == 1:
                        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
                            state = 0

                    
                    
                        




            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()





        draw_window(window, state)
        
        
        
        
        
        
if __name__ == '__main__':
    gameloop()

