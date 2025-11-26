import sqlite3
from Multiplier_Calculator import Multiplier
from UI_States import ui_states
from Ninjago_Characters import *
from Chima_Characters import *

class Campaign_Logic:
    @staticmethod
    def Check_stage(campaign, chapter, stage, player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT Battle_id FROM Campaigns;
                       WHERE Campaign = ?;
                       AND Chapter = ?;
                       AND Stage = ?;""",
                       (campaign, chapter, stage))

        battle_id = cursor.fetchone()

        cursor.execute("""SELECT Prev_completed FROM Campaigns_Player;
                       WHERE Battle_id = ?;
                       AND Player_id = ?;""",
                       (battle_id, player_id))

        comp = cursor.fetchone()

        conn.close()

        if comp:
            Campaign_Logic.start_battle(battle_id)

    @staticmethod
    def start_battle(battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Charatcer_1,
                                 Charatcer_2,
                                 Character_3,
                                 Charatcer_4,
                                 Character_5,
                                 Level,
                                 Gear,
                                 Star
                          FROM Campaigns;
        WHERE Battle_id = ?;""",
                       (battle_id))

        Enemy_battle = cursor.fetchall()[0]


        multiplier = Multiplier.calculate_stats_enemy(Enemy_battle[5], Enemy_battle[6], Enemy_battle[7])

        Echaracter1 = Campaign_Logic.__init_char(Enemy_battle[0], multiplier)
        Echaracter2 = Campaign_Logic.__init_char(Enemy_battle[1], multiplier)
        Echaracter3 = Campaign_Logic.__init_char(Enemy_battle[2], multiplier)
        Echaracter4 = Campaign_Logic.__init_char(Enemy_battle[3], multiplier)
        Echaracter5 = Campaign_Logic.__init_char(Enemy_battle[4], multiplier)





    @staticmethod
    def __init_char(character_id, multiplier):
        if character_id == 0:
            character = Cragger(stat_multiplier=multiplier)

        if character_id == 1:
            character = Gorzan(stat_multiplier=multiplier)

        if character_id == 2:
            character = Eris(stat_multiplier=multiplier)

        if character_id == 3:
            character = Razar(stat_multiplier=multiplier)

        if character_id == 4:
            character = Rinona(stat_multiplier=multiplier)

        if character_id == 5:
            character = Laval(stat_multiplier=multiplier)

        if character_id == 6:
            character = Kai(stat_multiplier=multiplier)

        if character_id == 7:
            character = Zane(stat_multiplier=multiplier)

        if character_id == 8:
            character = Cole(stat_multiplier=multiplier)

        if character_id == 9:
            character = Jay(stat_multiplier=multiplier)

        if character_id == 10:
            character = Lloyd(stat_multiplier=multiplier)

        if character_id == 11:
            character = Wu(stat_multiplier=multiplier)

        return character

    @staticmethod
    def __Player_choose_chars(Player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT Name FROM General_Character, Player_Table;
                       WHERE Player_Table.Player_id = ?;
                       AND General_Character.Character_id = Player_Table.Character_id;
                       AND Player_Table.Collected = True;
                       ORDER BY Level DESC;""",
                       (Player_id,))

        names = cursor.fetchall()

        ui_states.Character_selection_screen(names)




