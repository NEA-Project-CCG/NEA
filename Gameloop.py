import pygame
from UI import initial_UI, draw_window
import sqlite3
import re



def gameloop():

    state = "hub"

    campaign_re = "campaign_"

    conn = sqlite3.connect("NEA Database.db")

    cursor = conn.cursor()





    window, font = initial_UI()

    running = True
    while running:





















        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                pos_x = pos[0]
                pos_y = pos[1]

                LMB = 1
                
     

                Mtype = pygame.mouse.get_pressed()[0]

                if Mtype == LMB:
                
                    if state == "hub":
                        if pos_x >= 0 and pos_x < 350 and pos_y >= 0 and pos_y < 400:
                            state = "characters"


                        elif pos_x >= 0 and pos_x < 350 and pos_y >= 425 and pos_y <= 600:
                            state = "journey guide"

                        elif pos_x >= 375 and pos_x < 800 and pos_y >= 0 and pos_y <= 600:
                            state = "campaigns"

                    elif state in ["journey guide", "campaigns", "characters"]:

                        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
                            state = "hub"

                    if state == "campaigns":

                        if pos_x >= 40 and pos_y >= 60 and pos_x <= 290 and pos_y <= 540:
                            state = "campaign_1_1"

                    #matches whether the state is a campaign using regex
                    elif re.match(campaign_re, state):
                        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
                            state = "campaigns"

                        if (pos_y >= 225 and pos_y <= 265) or (pos_y >= 450 and pos_y <= 490):
                            for i in range(10):
                                if pos_x >= (70*(i) + 55) and pos_x <= (70*(i) + 95):
                                    if len(state) < len("campaign_x_x_"):
                                        state += f"_{i}"
                                    elif state[len(state)-1] != f"{i}":
                                        state = state[:(len(state)-1)] + f"{i}"

                        if pos_y >= 50 and pos_y <= 100:
                            if pos_x <= 260 and pos_x >= 0:
                                state = state[:11] + f"1"
                            elif pos_x >= 270 and pos_x <= 530:
                                state = state[:11] + f"2"
                            elif pos_x >= 540 and pos_x <= 800:
                                state = state[:11] + f"3"

                            print(f"DEBUG: {state}")








                    
                    
                        




            if event.type == pygame.QUIT:
                pygame.quit()
                running = False
                quit()





        draw_window(window, state, font, campaign_re)
        
        
    conn.close()
        
        
        
if __name__ == '__main__':
    gameloop()

