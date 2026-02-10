from Tkinter_Backend import Tkinter_Backend
from Ninjago_Characters import *
from Chima_Characters import *
from Marvel_characters import *
from Star_Wars_characters import *
from DC_Characters import *
from LotR_Characters import *
from Lego_Characters import *
from Character_leveling import Char_upgrading
from random import randint

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
    character_object_call[12] = Daredevil
    character_object_call[13] = Gambit
    character_object_call[14] = Spiderman
    character_object_call[15] = Storm
    character_object_call[16] = Sentry
    character_object_call[17] = Doom
    character_object_call[18] = Luke
    character_object_call[19] = Kenobi
    character_object_call[20] = Dooku
    character_object_call[21] = Ahsoka
    character_object_call[22] = Din
    character_object_call[23] = Maul
    character_object_call[24] = Kai
    character_object_call[25] = Batman
    character_object_call[26] = Lantern
    character_object_call[27] = Beetle
    character_object_call[28] = Constantine
    character_object_call[29] = Superman
    character_object_call[30] = Aragorn
    character_object_call[31] = Tom
    character_object_call[32] = Samwise
    character_object_call[33] = Sauron
    character_object_call[34] = Gollum
    character_object_call[35] = Gandalf
    character_object_call[36] = Gold
    character_object_call[37] = JarJar
    character_object_call[38] = Lincoln
    character_object_call[39] = Business
    character_object_call[40] = Chase
    character_object_call[41] = Clutch


    @staticmethod
    def Check_stage(campaign, chapter, stage, player_id):
        comp, battle_id = Database.Find_Player_Battle(campaign, chapter, stage, player_id)

        return comp, battle_id

    @staticmethod
    def start_battle(battle_id, player_id):

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

        CharDict = {}
        for i in range(5):
            CharDict["EChar"+str(i+1)] = Campaign_Logic.init_Echar(Campaign_chars[i], multiplier, battle_id)

        chars = Campaign_Logic.__Player_choose_chars(player_id)
        for i in range(5):
            CharDict["PChar"+str(i+1)] = Campaign_Logic.init_Pchar(chars[i], player_id)


        return CharDict

        # TempDict["EChar1"]
        # ECharacters[0]





    @staticmethod
    def init_Echar(character_id, multiplier, battle_id):

        character = Campaign_Logic.character_object_call[character_id](stat_multiplier=multiplier, Battle_id=battle_id)


        return character

    @staticmethod
    def init_Pchar(char, player_id):

        character = Campaign_Logic.character_object_call[char](player_id=player_id)

        return character

    @staticmethod
    def __Player_choose_chars(player_id):
        names = Database.Get_player_char_names(player_id)
        for i in range(len(names)):
            names[i] = names[i][0]

        chars = []

        for i in range(5):
            char, name_to_remove = Tkinter_Backend.Player_chars(names)
            names.remove(name_to_remove)
            chars.append(char)

        return chars

    @staticmethod
    def end_battle(player_id, Characters, Battle_id):

        Chapter, Stage = Database.Stage_and_Chapter_from_id(Battle_id)
        exp = Multiplier.EXP_Calculator(Chapter, Stage)
        for i in range(5):
            char = Characters["PChar"+str(i+1)]
            name = char.name
            char_id = Database.Char_id_from_name(name)
            Database.add_exp(player_id, char_id, exp)
            Char_upgrading.exp_to_level(player_id, char_id)
        Database.Unlock_next(player_id, Battle_id)
        char_unlock = Database.node_reward(Battle_id)
        chance = randint(0, 1)
        if chance == 1:
            Char_upgrading.Unlock_char(player_id, char_unlock)










