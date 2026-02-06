import re
import pygame

from Multiplier_Calculator import Multiplier
from Database_Querying import Database
from Tkinter_Backend import Tkinter_Backend

class ui_states:
    @staticmethod
    def select_state(window, state, font, campaign_re, player_id):
        chapter_index = 11
        if state == "hub":
            ui_states.__state_hub(window, font)

        elif state == "characters":
            ui_states.__state_characters_back(window, player_id)

        elif state == "journey guide":
            ui_states.__state_journey_guide(window)

        elif state == "campaigns":
            ui_states.__state_campaigns(window, font)

        elif re.match(campaign_re, state):
            ui_states.__state_campaign_base(window, font)
            if state[chapter_index] == "1":
                ui_states.__state_campaign_chapter_1(window, font)
            elif state[chapter_index] == "2":
                ui_states.__state_campaign_chapter_2(window, font)
            elif state[chapter_index] == "3":
                ui_states.__state_campaign_chapter_3(window, font)

        else:
            ui_states.__Character_state(player_id, state, window)

    @staticmethod
    def __Character_state(player_id, state, window):




        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        window.fill((125, 125, 125))

        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))
        text = state
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (375, 550))

        char_id = Database.Char_id_from_name(state)
        level, tokens = Database.return_level_and_tokens(player_id, char_id)
        star = Database.return_star(player_id, char_id)
        gear = Database.return_gear(player_id, char_id)

        text = f"Level: {str(level)}"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (20, 50))

        text = f"Tokens: {str(tokens)}"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (140, 50))

        text = f"Gear: {str(gear)}"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (580, 50))

        text = f"Star: {str(star)}"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (670, 50))

        if tokens >=5:
            text = f"Upgrade"
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (580, 80))

        if tokens >=7:
            text = f"Upgrade"
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (670, 80))

        multiplier = Multiplier.calculate_stats_player(player_id, char_id)
        text = f"Multiplier: {str(multiplier)}"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (325, 300))


    @staticmethod
    def __state_hub(window, font):
        window.fill((0, 0, 0))
        pygame.draw.rect(window, (0, 0, 255), pygame.Rect(0, 0, 350, 400))
        text = "Characters"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (30, 350))

        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(0, 425, 350, 175))
        text = "Journey Guide"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (15, 550))

        pygame.draw.rect(window, (0, 255, 0), pygame.Rect(375, 0, 425, 600))
        text = "Campaigns"
        text = font.render(text, True, (255, 254, 255))
        window.blit(text, (415, 550))


    #Characters screen
    @staticmethod
    def __state_characters_back(window, player_id):
        window.fill((0, 0, 254))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))
        ui_states.__State_Characters(window, player_id)


    @staticmethod
    def __State_Characters(window, player_id):
        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        names = Database.names_in_collected(player_id)
        j = 6
        for i in range(len(names)):
            pygame.draw.rect(window, (255*(1-names[i][1]), 255*(names[i][1]), 0), pygame.Rect(20 + (130*(i%j)), 50 + 80*(i//j), 100, 60))
            text = names[i][0]
            text = font.render(text, True, (255, 255, 255))
            window.blit(text,(30 + (130*(i%j)), 60 + 80*(i//j) ))




    #Journey Guide screen
    @staticmethod
    def __state_journey_guide(window):
        window.fill((255, 0, 0))
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        return window

    #Campaigns screen
    @staticmethod
    def __state_campaigns(window, font):
        window.fill((0, 255, 0))
        #Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        #draws first campaign
        pygame.draw.rect(window, (255, 0, 0), pygame.Rect(40, 60, 250, 480))
        text = "Campaign 1"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (45, 430))

    @staticmethod
    def __state_campaign_base(window, font):
        window.fill((7, 34, 166))

        # Draws back button
        pygame.draw.rect(window, (41, 103, 204), pygame.Rect(10, 10, 30, 30))

        # Draws campaign background
        pygame.draw.rect(window, (255, 125, 125), pygame.Rect(0, 100, 800, 500))

        pos_x = 55
        pos_y = [450, 225]

        for i in range(10):
            # draws campaign nodes
            pygame.draw.rect(window, (41, 255, 20), pygame.Rect(pos_x, pos_y[i%2], 40, 40))
            text = str(i + 1)
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (pos_x, pos_y[i%2]))

            pos_x += 70

        for i in range(3):
            pygame.draw.rect(window, (255, 255, 125), pygame.Rect((270*i), 50, 260, 50))

            text = str(i + 1)
            text = font.render(text, True, (0, 0, 0))
            window.blit(text, (270*i+125, 50))

    @staticmethod
    def __state_campaign_chapter_1(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(0, 50, 260, 50))

        text = "1"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (125, 50))

    @staticmethod
    def __state_campaign_chapter_2(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(270, 50, 260, 50))

        text = "2"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (395, 50))

    @staticmethod
    def __state_campaign_chapter_3(window, font):
        pygame.draw.rect(window, (138, 154, 91), pygame.Rect(540, 50, 260, 50))

        text = "3"
        text = font.render(text, True, (255, 255, 255))
        window.blit(text, (665, 50))


    @staticmethod
    def Battle_Background(window):
        window.fill((50, 50, 50))

    @staticmethod
    def init_Charatcer_names_and_health(window, characters, font):
        for i in range(5):
            character = characters[f"EChar{i+1}"]
            text = character.name
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150*i), 100))

            text = str(character.GetHealth())
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150*i), 130))

        for i in range(5):
            character = characters[f"PChar{i+1}"]
            text = character.name
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150*i), 400))

            text = str(character.GetSpeed())
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150*i), 430))


    @staticmethod
    def Charatcer_names_and_health(window, characters, font):
        change = len(characters[0].team_that_owns_me.team)


        for i in range(change):
            character = characters[i].character
            text = character.name
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150 * i), 400))

            text = str(character._health)
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150 * i), 430))


        j = 0
        for i in range(change, len(characters)):
            character = characters[i].character
            text = character.name
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150 * j), 100))

            text = str(character._health)
            text = font.render(text, True, (255, 255, 255))
            window.blit(text, (30 + (150 * j), 130))

            j +=1





