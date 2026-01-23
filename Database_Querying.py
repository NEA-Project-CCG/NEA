import sqlite3


class Database:
    @staticmethod
    def __Get_Character_ids():
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Character_id FROM General_character;''')

        Character_ids = cursor.fetchall()

        conn.close()

        return Character_ids

    @staticmethod
    def __Get_Character_Name(Character_ID):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Name FROM General_character
                       WHERE Character_id = ?;''',
                       [Character_ID])

        Names = cursor.fetchall()

        conn.close()

        return Names

    @staticmethod
    def Get_stats(Character_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT * FROM General_character 
                          WHERE Character_ID = ?''',
                       [Character_id])

        stats = cursor.fetchall()[0]

        conn.close()

        return stats

    @staticmethod
    def Get_Campaign_Chars(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Character_1, Character_2, Character_3, Character_4, Character_5 FROM Battles
                       WHERE Battle_id = ?;''',
                       [Battle_id[0]])

        Campaign_Chars = cursor.fetchall()[0]
        conn.close()

        return Campaign_Chars

    @staticmethod
    def Get_Multiplier_levels(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT Level, Gear, Star FROM Battles
                       WHERE Battle_id = ?;''',
                       [Battle_id[0]])

        Multiplier_Levels = cursor.fetchall()[0]
        Level = Multiplier_Levels[0]
        Gear = Multiplier_Levels[1]
        Star = Multiplier_Levels[2]
        conn.close()
        return Level, Gear, Star

    @staticmethod
    def Get_Player_Char_multiplier_stats(player_id, character_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT Level, Gear, Star
                          FROM Player_Table
        WHERE Player_id = ?
        AND Character_id = ?;''', [player_id, character_id])

        stats = cursor.fetchall()[0]

        level = stats[0]
        gear = stats[1]
        star = stats[2]

        conn.close()

        return level, gear, star

    @staticmethod
    def Find_Player_Battle(campaign, chapter, stage, player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT Battle_id
                          FROM Campaigns
        WHERE Campaign_id = ?
        AND Chapter_id = ?
        AND Stage_id = ?;""",
                       (campaign, chapter, stage))

        battle_id = cursor.fetchone()

        conn.close()

        comp = Database.__check_applicable(player_id, battle_id[0])
        return comp, battle_id


    @staticmethod
    def __check_applicable(player_id, battle_id):

        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT Prev_completed
                          FROM Campaigns_Player
        WHERE Battle_id = ?
        AND Player_id = ?;""",
                       (battle_id, player_id))

        completed_battle_id = cursor.fetchone()

        conn.close()

        if completed_battle_id[0]:
            return True
        return False

    @staticmethod
    def Get_player_char_names(player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""SELECT Character_Name
                          FROM General_Character,
                               Player_Table
        WHERE Player_Table.Player_id = ?
        AND General_Character.Character_id = Player_Table.Character_id
        AND Player_Table.Collected = True
        ORDER BY Level DESC;""",
                       (player_id,))

        names = cursor.fetchall()

        conn.close()

        return names

    @staticmethod
    def Char_id_from_name(name):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Character_id FROM General_character 
                       WHERE Character_Name = ?;""",
                       [name])

        character_id = cursor.fetchone()[0]
        conn.close()
        return character_id

    @staticmethod
    def Create_new_player_Chars(Player_id):

        char_ids = Database.__Get_Character_ids()

        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        for i in range(len(char_ids)):
            cursor.execute("""INSERT INTO Player_Table VALUES (?, ?, False, 1, 1, 0, 0);""",
                           (Player_id, char_ids[i][0]))

        for i in range(5):
            cursor.execute("""UPDATE Player_Table 
                              SET Collected = True, Star = 1
                              WHERE Character_id = ? 
                                AND Player_id = ?;""",
                           (char_ids[i][0], Player_id))

        conn.commit()
        conn.close()

    @staticmethod
    def Create_new_player_Campigns(player_id):

        num_of_battles = Database.how_many_battles()

        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        for i in range(num_of_battles):
            cursor.execute("""INSERT INTO Campaigns_Player 
                              VALUES (?, ?, False, False);""",
                           (player_id, i))

        cursor.execute("""UPDATE Campaigns_Player 
                          SET Prev_completed = True 
                          WHERE Battle_id = 0""")

        conn.commit()
        conn.close()

    @staticmethod
    def how_many_battles() -> int:
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Battle_id FROM Campaigns""")
        battles = cursor.fetchall()
        battle_nums = len(battles)

        conn.close()

        return battle_nums


    @staticmethod
    def node_reward(battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Char_id_reward from Campaigns
                       WHERE battle_id = ?;""", [battle_id])
        char_id = cursor.fetchone()[0]
        conn.close()
        return char_id

    @staticmethod
    def has_char(char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Star FROM Player_Table WHERE Character_id = ?;""",[char_id])
        got_char = cursor.fetchone()[0]
        conn.close()
        if got_char > 0:
            return True
        return False

    @staticmethod
    def return_level_and_tokens(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level, Level_tokens FROM Player_Table WHERE Player_id = ? AND Character_id = ?;""",(player_id, char_id))
        db_get = cursor.fetchone()
        level = db_get[0]
        level_tokens = db_get[1]
        conn.close()
        return level, level_tokens

    @staticmethod
    def increase_star(Player_id, char_id, level_tokens, star):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE Player_Table SET Star = ? + 1, Level_tokens = ? - 7 WHERE Player_id = ? AND Character_id = ?;""",[star, level_tokens, Player_id, char_id])
        conn.commit()
        conn.close()

    @staticmethod
    def return_star(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Star FROM PLayer_TABLE WHERE Character_id = ? AND Player_id = ?;""",(char_id, player_id))
        db_get = cursor.fetchone()
        star = db_get[0]
        conn.close()
        return star

    @staticmethod
    def return_gear(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Gear FROM PLayer_TABLE WHERE Character_id = ? AND Player_id = ?;""",(char_id, player_id))
        db_get = cursor.fetchone()
        gear = db_get[0]
        conn.close()
        return gear

    @staticmethod
    def increase_gear(Player_id, char_id, gear, level_tokens):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE Player_Table
                          SET Gear         = ? + 1,
                              Level_tokens = ? - 4
                          WHERE Player_id = ?
                            AND Character_id = ?;""", [gear, level_tokens, Player_id, char_id])
        conn.commit()
        conn.close()

    @staticmethod
    def return_level(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level FROM Player_Table WHERE Player_id = ? AND Character_id = ?;""",(player_id, char_id))
        db_get = cursor.fetchone()
        level = db_get[0]
        conn.close()
        return level

    @staticmethod
    def Stage_and_Chapter_from_id(battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Chapter_id, Stage_id FROM Campaigns WHERE Battle_id = ?;""",(battle_id,))
        db_get = cursor.fetchone()
        chapter = db_get[0]
        stage = db_get[1]
        conn.close()
        return chapter, stage

    @staticmethod
    def add_exp(player_id, char_id, exp):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE Player_Table SET""")

if __name__ == '__main__':
    Database.Create_new_player_Campigns(0)

