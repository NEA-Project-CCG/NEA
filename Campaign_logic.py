import sqlite3
from Multiplier_Calculator import Multiplier
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

        Ofile = open("All_chars_list.txt", "r")
        all_chars = Ofile.readline().strip()
        all_chars = all_chars.split(",")

        Enemy_Character_1 = all_chars[Enemy_battle[0]]




if __name__ == '__main__':
    Campaign_Logic.start_battle(None)
