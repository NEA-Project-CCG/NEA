from UI import draw_battle, Draw_abilities
from Battle_Classes import *
from Battle_Queue import *
import pygame
from Pygame_clicks_logic import LMB

class Battle_Loop:

    @staticmethod
    def the_loop(window, characters):
        Battle, Team1, Team2, list_of_chars = Battle_Loop.Create_battle_classes(characters)

        queue = Speed_Queue(list_of_chars)

        queue.speed_turn()

        char_turn = queue.Get_character_for_turn()
        Battle_Loop.__turn_loop(char_turn, window)


















        draw_battle(window, characters)

    @staticmethod
    def battle_characters(characters: dict, Battle) -> dict:
        dict_of_characters = {}
        for i in range(5):
            team = Battle.get_team_2()
            dict_of_characters[f"EChar_class{i+1}"] = (Character(characters[f"EChar{i+1}"], team))
            team.add_character(dict_of_characters[f"EChar_class{i+1}"])

        for i in range(5):
            team = Battle.get_team_1()
            dict_of_characters[f"PChar_class{i + 1}"] = (Character(characters[f"PChar{i + 1}"], team))
            team.add_character(dict_of_characters[f"PChar_class{i + 1}"])

        return dict_of_characters



    @staticmethod
    def battle_class():
        Battle = BattleField()

        return Battle


    @staticmethod
    def battle_teams(Battle: BattleField) -> list[Team]:
        for i in range(2):
            Battle.add_team(Team(Battle))


    @staticmethod
    def character_list(Character_dict: dict) -> list[Character]:
        list_of_characters = []
        for i in range(5):
            list_of_characters.append(Character_dict[f"PChar_class{i + 1}"])

        for i in range(5):
            list_of_characters.append(Character_dict[f"EChar_class{i + 1}"])

        return list_of_characters


    @staticmethod
    def Create_battle_classes(characters):
        Battle = Battle_Loop.battle_class()
        Battle_Loop.battle_teams(Battle)
        dict_of_chars = Battle_Loop.battle_characters(characters, Battle)
        list_of_chars = Battle_Loop.character_list(dict_of_chars)
        Team1 = list_of_chars[0].team_that_owns_me
        Team2 = list_of_chars[6].team_that_owns_me

        return Battle, Team1, Team2, list_of_chars


    @staticmethod
    def __turn_loop(character, window):
        basic = character.basic
        special = character.special
        ultimate = character.ultimate

        attacked = False

        while not attacked:
            window = Draw_abilities(window)

            lmb = 1

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.mouse.get_pressed()[0]:
                        pos_x = pygame.mouse.get_pos()[0]
                        pos_y = pygame.mouse.get_pos()[1]
                        ability = LMB.click_attack(pos_x, pos_y)


