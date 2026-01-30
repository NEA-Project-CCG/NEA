import pygame
import re
from Campaign_logic import Campaign_Logic
from Database_Querying import Database
from Character_leveling import Char_upgrading


class LMB:

    @staticmethod
    def clicked_state(state, campaign_re, pos_x, pos_y, player_id):
        if state == "hub":
            state = LMB.in_hub(pos_x, pos_y, state)
        elif state in ["journey guide", "campaigns", "characters"]:
            state = LMB.in_hub_level_1(pos_x, pos_y, state, player_id)
        elif re.match(campaign_re, state):
            state = LMB.inside_a_campaign(pos_x, pos_y, state)
        else:
            state = LMB.in_char(pos_x, pos_y, state, player_id)
        return state

    @staticmethod
    def click_attack(pos_x, pos_y):
        start_x = 50
        end_x = 250
        y_top = 560
        y_bottom = 580

        if pos_y > y_top and pos_y < y_bottom:
            for i in range(3):
                if pos_x > start_x + i*250 and pos_x < end_x + i*250:
                    pass




    @staticmethod
    def in_hub(pos_x, pos_y, state):
        if pos_x >= 0 and pos_x < 350 and pos_y >= 0 and pos_y < 400:
            state = "characters"


        elif pos_x >= 0 and pos_x < 350 and pos_y >= 425 and pos_y <= 600:
            state = "journey guide"

        elif pos_x >= 375 and pos_x < 800 and pos_y >= 0 and pos_y <= 600:
            state = "campaigns"


        return state

    @staticmethod
    def in_hub_level_1(pos_x, pos_y, state, player_id):
        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
            state = "hub"

        elif state == "campaigns":
            state = LMB.in_campaigns(pos_x, pos_y, state)

        elif state == "characters":
            state = LMB.choosing_char(pos_x,pos_y, state, player_id)

        return state


    @staticmethod
    def choosing_char(pos_x, pos_y, state, player_id):
        names = Database.names_in_collected(player_id)
        j = 6
        for i in range(len(names)):
            if pos_y > 50 + 80*(i//j) and pos_y < 110 + 80*(i//j):
                if pos_x > 20 + (130*(i%j)) and pos_x < 120 + (130*(i%j)):
                    state = names[i][0]
                    print(state)

        return state

    @staticmethod
    def in_campaigns(pos_x, pos_y, state):
        if pos_x >= 40 and pos_y >= 60 and pos_x <= 290 and pos_y <= 540:
            state = "campaign_1_1"

        return state


    @staticmethod
    def inside_a_campaign(pos_x, pos_y, state):
        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
            state = "campaigns"

        if pos_y >= 50 and pos_y <= 100:
            state = LMB.change_chapter(pos_x, state)

        if (pos_y >= 225 and pos_y <= 265) or (pos_y >= 450 and pos_y <= 490):
            state = LMB.campaign_node(pos_x, state)



        return state

    @staticmethod
    def change_chapter(pos_x, state):
        if pos_x <= 260 and pos_x >= 0:
            state = state[:11] + f"1"
        elif pos_x >= 270 and pos_x <= 530:
            state = state[:11] + f"2"
        elif pos_x >= 540 and pos_x <= 800:
            state = state[:11] + f"3"

        return state

    @staticmethod
    def campaign_node(pos_x, state):
        for i in range(10):
            if pos_x >= (70 * (i) + 55) and pos_x <= (70 * (i) + 95):
                if len(state) < len("campaign_x_x_"):
                    state += f"_{i}"
                elif state[len(state) - 1] != f"{i}":
                    state = state[:(len(state) - 1)] + f"{i}"

        return state

    @staticmethod
    def in_char(pos_x, pos_y, state, player_id):
        if pos_x >= 10 and pos_y >= 10 and pos_x <= 40 and pos_y <= 40:
            state = "characters"

        elif pos_x >= 670 and pos_x <= 750 and pos_y >= 80 and pos_y <= 110:
            char_id = Database.Char_id_from_name(state)
            Char_upgrading.Upgrade_star(char_id, player_id)

        elif pos_x >= 580 and pos_x <= 660 and pos_y >= 80 and pos_y <= 110:
            char_id = Database.Char_id_from_name(state)
            Char_upgrading.Upgrade_gear(char_id, player_id)

        return state
