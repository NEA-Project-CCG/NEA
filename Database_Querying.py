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
        cursor.execute('''SELECT Character_Name FROM General_character
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
                       [Battle_id])

        Campaign_Chars = cursor.fetchall()[0]
        conn.close()

        return Campaign_Chars

    @staticmethod
    def Get_Multiplier_levels(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute('''SELECT Level, Gear, Star FROM Battles
                       WHERE Battle_id = ?;''',
                       [Battle_id])

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

        battle_id = cursor.fetchone()[0]

        conn.close()

        comp = Database.__check_applicable(player_id, battle_id)
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


            cursor.execute("""INSERT OR IGNORE INTO Player_Table VALUES (?, ?, False, 1, 1, 0, 0, 0);""",
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
            cursor.execute("""INSERT OR IGNORE INTO Campaigns_Player VALUES (?, ?, False, False);""",
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
        cursor.execute("""SELECT Char_id_reward FROM Battles
                          WHERE battle_id = ?;""", [battle_id])
        char_id = cursor.fetchone()[0]
        conn.close()
        return char_id

    @staticmethod
    def has_char(char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Star
                          FROM Player_Table
                          WHERE Character_id = ?;""", [char_id])
        got_char = cursor.fetchone()[0]
        conn.close()
        if got_char > 0:
            return True
        return False

    @staticmethod
    def return_level_and_tokens(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level, Level_tokens
                          FROM Player_Table
                          WHERE Player_id = ?
                            AND Character_id = ?;""", (player_id, char_id))
        db_get = cursor.fetchone()
        level = db_get[0]
        level_tokens = db_get[1]
        conn.close()
        return level, level_tokens

    @staticmethod
    def return_level_tokens(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level_tokens FROM Player_Table
                       WHERE Player_id = ?
                       AND Character_id = ?;""", [player_id, char_id])
        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def increase_level(player_id, char_id, level, exp, level_tokens):
        curr_exp = Database.get_exp(player_id, char_id)
        new_exp = curr_exp - exp
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE Player_Table
                        SET Level = ?, exp = ?, Level_tokens = ?
                        WHERE Player_id = ?
                        AND Character_id = ?;""",
                       (level + 1, new_exp, level_tokens + 1, player_id, char_id))

        conn.commit()
        conn.close()


    @staticmethod
    def increase_star(Player_id, char_id, level_tokens, star):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""UPDATE Player_Table
                          SET Star         = ? + 1,
                              Level_tokens = ? - 7
                          WHERE Player_id = ?
                            AND Character_id = ?;""", [star, level_tokens, Player_id, char_id])
        conn.commit()
        conn.close()

    @staticmethod
    def return_star(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Star
                          FROM PLayer_TABLE
                          WHERE Character_id = ?
                            AND Player_id = ?;""", (char_id, player_id))
        db_get = cursor.fetchone()
        star = db_get[0]
        conn.close()
        return star

    @staticmethod
    def return_gear(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Gear
                          FROM PLayer_TABLE
                          WHERE Character_id = ?
                            AND Player_id = ?;""", (char_id, player_id))
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
                              Level_tokens = ? - 5
                          WHERE Player_id = ?
                            AND Character_id = ?;""", [gear, level_tokens, Player_id, char_id])
        conn.commit()
        conn.close()

    @staticmethod
    def return_level(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level
                          FROM Player_Table
                          WHERE Player_id = ?
                            AND Character_id = ?;""", (player_id, char_id))
        db_get = cursor.fetchone()
        level = db_get[0]
        conn.close()
        return level

    @staticmethod
    def Stage_and_Chapter_from_id(battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Chapter_id, Stage_id
                          FROM Campaigns
                          WHERE Battle_id = ?;""", (battle_id,))
        db_get = cursor.fetchone()
        chapter = db_get[0]
        stage = db_get[1]
        conn.close()
        return chapter, stage

    @staticmethod
    def get_exp(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT exp
                          FROM Player_Table
                          WHERE Player_id = ?
                            AND Character_id = ?;""", (player_id, char_id))
        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def add_exp(player_id, char_id, exp):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()



        cur_exp = Database.get_exp(player_id, char_id)

        cursor.execute("""UPDATE Player_Table 
                        SET exp = ?
                       WHERE Player_id = ?
                       AND Character_id = ?;""", (cur_exp + exp, player_id, char_id))

        conn.commit()
        conn.close()

    @staticmethod
    def return_Journey_reqs(Journey_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Char_1_id, Char_2_id, Char_3_id, Char_4_id, Char_5_id, Gear, Star
                          FROM Journey_reqs
                          WHERE Journey_id = ?;""", [Journey_id])
        db_get = cursor.fetchone()
        conn.close()
        return db_get

    @staticmethod
    def Journey_reward(Journey_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        Battle_id = Database.Journey_Battle_id(Journey_id)

        cursor.execute("""SELECT Char_id_reward
                          FROM Battles
                          WHERE Battle_id = ?;""", [Battle_id])
        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def reqs_completed(Journey_id, Player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Battle_id
                          FROM Campaigns
                          WHERE Campaigns.Campaign_id = ?
                            AND Campaigns.Chapter_id = 1
                            AND Campaigns.Stage_id = 0;""", [Journey_id])

        battle_id = cursor.fetchone()[0]
        cursor.execute("""  UPDATE Campaigns_Player
                            SET Prev_completed = 1
                            WHERE Player_id = ?
                              AND Battle_id = ?;
                       """, [Player_id, battle_id])

        conn.commit()
        conn.close()

    @staticmethod
    def names_in_collected(player_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Character_Name, Collected
                          FROM Player_Table,
                               General_character
                          WHERE Player_id = ?
                            AND Player_Table.Character_id = General_Character.Character_ID
                          ORDER BY Collected DESC, Level DESC;""", (player_id,))

        Names = cursor.fetchall()
        names = []
        for i in range(len(Names)):
            names.append(Names[i])

        conn.close()
        return names

    @staticmethod
    def is_legendary(char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Legendary FROM General_character
                       WHERE Character_ID = ?;""", (char_id,))

        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def collect_character(player_id, char_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()

        cursor.execute("""UPDATE Player_Table
                        SET Collected = 1, Star = 1
                       WHERE Player_id = ?
                       AND Character_id = ?;""", (player_id, char_id))

        conn.commit()
        conn.close()

    @staticmethod
    def get_campaign(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Campaign_id, Chapter_id, Stage_id FROM Campaigns
                       WHERE Battle_id = ?""" , [Battle_id])

        db_get = cursor.fetchone()
        conn.close()
        Campaign = db_get[0]
        Chapter = db_get[1]
        Stage = db_get[2]
        return Campaign, Chapter, Stage

    @staticmethod
    def Unlock_next(player_id, Battle_id):
        campaign, chapter, stage = Database.get_campaign(Battle_id)
        another = True
        if stage < 9:
            comp, Battle_next = Database.Find_Player_Battle(campaign, chapter, stage + 1, player_id)
        elif chapter < 3:
            comp, Battle_next = Database.Find_Player_Battle(campaign, chapter + 1, 0, player_id)
        else:
            another = False

        if another:

            conn = sqlite3.connect('NEA Database.db')
            cursor = conn.cursor()
            cursor.execute("""UPDATE Campaigns_Player
            SET Prev_completed = 1
            WHERE Player_id = ?
            AND Battle_id = ?""", [player_id, Battle_next])

            cursor.execute("""UPDATE Campaigns_Player
                              SET Completed = 1
                              WHERE Player_id = ?
                                AND Battle_id = ?""", [player_id, Battle_id])

        conn.commit()
        conn.close()

    @staticmethod
    def Journey_Battle_id(Journey_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Battle_id FROM Campaigns
                       WHERE Campaign_id = ?
                       AND Chapter_id = 1
                       AND Stage_id = 5;""", [Journey_id])

        battle_id = cursor.fetchone()[0]
        conn.close()
        return battle_id

    @staticmethod
    def Stage_from_id(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Stage_id FROM Campaigns
                       WHERE Battle_id = ?""",[Battle_id])
        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def Unlock_next_journey(PLayer_id, Battle_id):
        stage = Database.Stage_from_id(Battle_id)
        if stage < 5:
            conn = sqlite3.connect('NEA Database.db')
            cursor = conn.cursor()
            cursor.execute("""UPDATE Campaigns_Player
                        SET Prev_completed = 1
                        WHERE Player_id = ?
                        AND Battle_id = ?""", [PLayer_id, Battle_id + 1])

            cursor.execute("""UPDATE Campaigns_Player
                              SET Completed = 1
                              WHERE Player_id = ?
                                AND Battle_id = ?""", [PLayer_id, Battle_id])

            conn.commit()
            conn.close()

    @staticmethod
    def Battle_level(Battle_id):
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute("""SELECT Level FROM Battles
                       WHERE Battle_id = ?""", [Battle_id])

        db_get = cursor.fetchone()[0]
        conn.close()
        return db_get

    @staticmethod
    def New_user(username, password):
        conn = sqlite3.connect("NEA Database.db")

        cursor = conn.cursor()

        cursor.execute('''INSERT INTO User(Email, Password)
                          VALUES (?, ?)''', [username, password])

        conn.commit()

        conn.close()

        p_id = Database.get_player_id(username, password)
        Database.Create_new_player_Chars(p_id)
        Database.Create_new_player_Campigns(p_id)





    @staticmethod
    def get_player_id(email, password):
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT Player_id
                          FROM User
                          WHERE Email = ?
                            AND Password = ?''', [email, password])

        p_id = cursor.fetchone()[0]
        conn.close()
        return p_id

    @staticmethod
    def all_emails():
        conn = sqlite3.connect('NEA Database.db')
        cursor = conn.cursor()
        cursor.execute('''SELECT Email FROM User''')
        fetched = cursor.fetchall()
        list_of_emails = []
        for email in fetched:
            list_of_emails.append(email[0])
        conn.close()
        return list_of_emails

    @staticmethod
    def password(email):
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()

        cursor.execute('''SELECT Password
                          FROM User
                          WHERE Email = (?)''', [email])

        password = cursor.fetchone()[0]
        conn.close()
        return password


if __name__ == '__main__':
    Database.Create_new_player_Campigns(0)
