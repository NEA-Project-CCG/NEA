import pygame
from UI import initial_UI, draw_window, draw_win, draw_loss
from Campaign_logic import Campaign_Logic
from Pygame_clicks_logic import LMB
from Battle_Loop import Battle_Loop
from Journey_logic import Journeys


class Gameloop:
    @staticmethod
    def gameloop(Player_id):

        campaign_re = "campaign_"

        state = "hub"

        battling = False
        Journey = False

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
                        state = LMB.clicked_state(state, campaign_re, pos_x, pos_y, Player_id)
                        if len(state) == 14:
                            comp, Battle_id = Campaign_Logic.Check_stage(state[Campaign_index], state[Chapter_index], state[Stage_index], Player_id)
                            if comp:
                                Characters = Campaign_Logic.start_battle(Battle_id, Player_id)
                                battling = True

                        elif state[len(state)-3] == "J":
                            if state[0] == "L":
                                journey_id = 2
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state)-1], Player_id)
                            elif state[0] == "W":
                                journey_id = 3
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            elif state[0] == "D":
                                journey_id = 4
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            elif state[0] == "M":
                                journey_id = 5
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            elif state[0] == "S":
                                journey_id = 6
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            elif state[0] == "G":
                                journey_id = 7
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            elif state[0] == "C":
                                journey_id = 8
                                Journeys.check_eligibility(Player_id, journey_id)
                                comp, Battle_id = Campaign_Logic.Check_stage(journey_id, 1, state[len(state) - 1],
                                                                             Player_id)
                            if comp:
                                Characters = Journeys.start_battle(Battle_id, Player_id, journey_id)
                                Journey = True
                                battling = True

                            else:
                                state = state[:len(state)-2]


                if event.type == pygame.QUIT:
                    pygame.quit()
                    running = False
                    quit()



                if battling:

                    Battle, Team1, Team2, list_of_chars= Battle_Loop.Startup(window, Characters)
                    while battling:
                        battling, victory, list_of_chars = Battle_Loop.the_loop(window, Battle, Team1, Team2, list_of_chars)

                        if not battling:
                            if victory:
                                if Journey:
                                    Journey = False
                                    Journeys.end_battle(Battle_id, Player_id, journey_id)
                                    state = state[:len(state) - 2]

                                else:

                                    Campaign_Logic.end_battle(Player_id, Characters, Battle_id)
                                draw_win(window)
                            else:
                                if Journey:
                                    state = state[:len(state) - 2]
                                Journey = False
                                draw_loss(window)

                else:
                    draw_window(window, state, font, campaign_re, Player_id)

        
        
        
if __name__ == '__main__':
    Gameloop.gameloop(0)


