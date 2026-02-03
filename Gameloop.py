import pygame
from UI import initial_UI, draw_window
from Campaign_logic import Campaign_Logic
from Pygame_clicks_logic import LMB
from Battle_Loop import Battle_Loop


class Gameloop:
    @staticmethod
    def gameloop(Player_id):

        campaign_re = "campaign_"

        state = "hub"

        battling = False

        lmb = 1

        Campaign_index = 9
        Chapter_index = 11
        Stage_index = 13

        window, font = initial_UI()

        running = True
        while running:

            for event in pygame.event.get():

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos_x = pygame.mouse.get_pos()[0]
                        pos_y = pygame.mouse.get_pos()[1]
                        state = LMB.clicked_state(state, campaign_re, pos_x, pos_y)
                        if len(state) == 14:
                            comp, Battle_id = Campaign_Logic.Check_stage(state[Campaign_index], state[Chapter_index], state[Stage_index], Player_id)
                            if comp:
                                Characters = Campaign_Logic.start_battle(Battle_id, Player_id)
                                battling = True

                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    quit()



                if battling:

                    Battle, Team1, Team2, list_of_chars, queue = Battle_Loop.Startup(window, Characters)
                    while battling:
                        battling = Battle_Loop.the_loop(window, Battle, Team1, Team2, list_of_chars, queue, Characters)
                else:
                    draw_window(window, state, font, campaign_re)

        
        
        
if __name__ == '__main__':
    Gameloop.gameloop(0)

