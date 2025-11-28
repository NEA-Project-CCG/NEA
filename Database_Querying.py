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
    def __Get_Charatcer_Name(Charatcer_ID):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Name FROM General_character
                       WHERE Character_id = ?;''',
                       [Charatcer_ID])

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
        cursor.execute('''SELECT Character_1, Charatcer_2, Charatcer_3, Charatcer_4, Charatcer_5 FROM Campaigns
                       WHERE Battle_id = ?;''',
                       [Battle_id])

        Campaign_Chars = cursor.fetchall()
        conn.close()

        return Campaign_Chars

    @staticmethod
    def Get_Multiplier_levels(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT Level, Gear, Star FROM Campaigns
                       WHERE Battle_id = ?;''',
                       [Battle_id])

        Multiplier_Levels = cursor.fetchall()
        conn.close()
        return Multiplier_Levels

    @staticmethod
    def Get_Player_Char_multiplier_stats(player_id, character_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT Level, Gear, Star
                          FROM Player_Table
        WHERE Player_id = ?
        AND Character_id = ?;''', [player_id, character_id])

        level = cursor.fetchone()[0][0]
        gear = cursor.fetchone()[1][0]
        star = cursor.fetchone()[2][0]

        conn.close()

        return level, gear, star
