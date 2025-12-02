from UI_States import ui_states
from Ninjago_Characters import *
from Chima_Characters import *

class Campaign_Logic:

    character_object_call = {}

    character_object_call[0] = Cragger
    character_object_call[1] = Gorzan
    character_object_call[2] = Eris
    character_object_call[3] = Razar
    character_object_call[4] = Rinona
    character_object_call[5] = Laval
    character_object_call[6] = Kai
    character_object_call[7] = Zane
    character_object_call[8] = Cole
    character_object_call[9] = Jay
    character_object_call[10] = Lloyd
    character_object_call[11] = Wu


    @staticmethod
    def Check_stage(campaign, chapter, stage, player_id):
        comp, battle_id = Database.Find_Player_Battle(campaign, chapter, stage, player_id)

        if comp:
            Campaign_Logic.start_battle(battle_id)

    @staticmethod
    def start_battle(battle_id):

        Campaign_chars = Database.Get_Campaign_Chars(battle_id)

        Enemy_level, Enemy_gear, Enemy_star = Database.Get_Multiplier_levels(battle_id)


        multiplier = Multiplier.calculate_stats_enemy(Enemy_level, Enemy_gear, Enemy_star)
        """
        ECharacters: list[Character] = []
        # duck-typing
        for i in range(5):
            ECharacters.append(Campaign_Logic.__init_char(Enemy_battle[i], multiplier))
            
        """

        # Echaracter1 = Campaign_Logic.__init_char(Enemy_battle[0], multiplier)
        # Echaracter2 = Campaign_Logic.__init_char(Enemy_battle[1], multiplier)
        # Echaracter3 = Campaign_Logic.__init_char(Enemy_battle[2], multiplier)
        # Echaracter4 = Campaign_Logic.__init_char(Enemy_battle[3], multiplier)
        # Echaracter5 = Campaign_Logic.__init_char(Enemy_battle[4], multiplier)

        TempDict = {}
        for i in range(5):
            TempDict["EChar"+str(i+1)] = Campaign_Logic.__init_char(Campaign_chars[i], multiplier)

        # TempDict["EChar1"]
        # ECharacters[0]





    @staticmethod
    def __init_char(character_id, multiplier):

        character = Campaign_Logic.character_object_call[character_id](stat_multiplier=multiplier)


        return character

    @staticmethod
    def __Player_choose_chars(player_id):
        names = Database.Get_player_char_names(player_id)

        ui_states.Character_selection_screen_setup(names)




