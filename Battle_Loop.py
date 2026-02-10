from UI import init_draw_battle, Draw_abilities, draw_battle, draw_target
from Battle_Classes import *
from Battle_Queue import *
import pygame
from Pygame_clicks_logic import LMB
from random import randint

class Battle_Loop:

    @staticmethod
    def Startup(window, characters):
        init_draw_battle(window, characters)
        Battle, Team1, Team2, list_of_chars = Battle_Loop.Create_battle_classes(characters)

        queue = Speed_Queue(list_of_chars)

        Battle.add_queue(queue)

        return Battle, Team1, Team2, list_of_chars

    @staticmethod
    def the_loop(window, Battle, Team1, Team2, list_of_chars):


        Battle.queue.speed_turn()

        char_turn = Battle.queue.Get_character_for_turn()
        Battle_Loop.__turn_loop(char_turn, window, Battle, list_of_chars)



        list_of_chars = Battle_Loop.__update_list(Team1, Team2)

        battling = not Battle_Loop.__check_win_or_defeat(Battle)

        opposing_team, ai = Battle.opposing_team()

        char_turn.passive(opposing_team)


        draw_battle(window, list_of_chars)

        char_turn.character._special_cooldown -= 1
        char_turn.character._ultimate_cooldown -=1
        return battling, Battle.check_victory(), list_of_chars

    @staticmethod
    def battle_characters(characters: dict, Battle) -> dict:
        dict_of_characters = {}
        for i in range(5):
            team = Battle.battlefield[1]
            dict_of_characters[f"EChar_class{i+1}"] = (Character(characters[f"EChar{i+1}"], team))
            team.add_character(dict_of_characters[f"EChar_class{i+1}"])

        for i in range(5):
            team = Battle.battlefield[0]
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
    def __turn_loop(char_turn, window, Battle, characters):
        abs = [char_turn.basic, char_turn.special, char_turn.ultimate]
        opposing_team, ai = Battle.opposing_team()



        if ai == 1:
            if len(opposing_team.team) == 0:
                print("Here")
                pass
            else:
                char_turn._target = randint(0, len(opposing_team.team) - 1)
                cds = 1
                scds = 0
                ucds = 0
                if char_turn.character._special_cooldown == 0:
                    scds = 1
                    cds += 1
                if char_turn.character._ultimate_cooldown == 0:
                    ucds =1
                    cds +=1

                if cds == 1:
                    ability = 0
                elif cds == 3:
                    ability = randint(0, cds-1)
                elif cds == 2 and scds == 1:
                    ability = randint(0, 1)
                elif cds == 2 and ucds == 1:
                    ability = randint(0, 1)
                    if ability == 1:
                        ability = 2

                abs[ability](opposing_team)


        else:
            attacked = False
            char_turn._target = 0
            draw_target(window, char_turn._target)
            while not attacked:






                abilities = ["Basic", "Special", "Ultimate"]
                window = Draw_abilities(window, abilities, char_turn)

                lmb = 1

                for event in pygame.event.get():
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if pygame.mouse.get_pressed()[0]:
                            pos_x = pygame.mouse.get_pos()[0]
                            pos_y = pygame.mouse.get_pos()[1]
                            ability = LMB.click_attack(pos_x, pos_y, char_turn)
                            if ability == -1:
                                pass
                            else:
                                attacked = True
                            target = LMB.click_target(pos_x, pos_y, len(opposing_team.team))
                            if target == -1:
                                pass
                            else:
                                draw_battle(window, characters)
                                Draw_abilities(window, abilities, char_turn)
                                char_turn._target = target
                                draw_target(window, char_turn._target)

                    if event.type == pygame.QUIT:
                        pygame.quit()
                        quit()

            abs[ability](opposing_team)







    @staticmethod
    def __update_list(Team1, Team2):
        team1 = Team1.team
        team2 = Team2.team
        chars = []
        for i in range(len(team1)):
            chars.append(team1[i])
        for i in range(len(team2)):
            chars.append(team2[i])

        return chars

    @staticmethod
    def __check_win_or_defeat(Battle):
        win = Battle.check_victory()
        if win:
            return win
        lose = Battle.check_defeat()
        if lose:
            print("lose")
            return lose

        return False





