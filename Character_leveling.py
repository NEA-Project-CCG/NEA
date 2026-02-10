
from Database_Querying import Database

class Char_upgrading:
    levels_dict = {
        "0" : 300,
        "1" : 1100,
        "2" : 1200,
        "3" : 1300,
        "4" : 1500,
        "5" : 1600,
        "6" : 3200,
        "7" : 6400,
        "8" : 8000,
        "9" : 16000,
        "l" : 32000,

    }

    @staticmethod
    def Unlock_char(player_id, char_id):
        Database.collect_character(player_id, char_id)

    @staticmethod
    def Upgrade_char(char_id, player_id, exp):
        level, level_tokens = Database.return_level_and_tokens(player_id, char_id)
        Database.increase_level(player_id, char_id, level,  exp, level_tokens)

    @staticmethod
    def Upgrade_star(char_id, player_id):
        level_tokens = Database.return_level_tokens(player_id, char_id)
        if level_tokens >= 7:
            stars = Database.return_star(player_id, char_id)
            if stars < 7:
                Database.increase_star(player_id, char_id, level_tokens, stars)
                return True
            return False
        return False

    @staticmethod
    def Upgrade_gear(char_id, player_id):
        level_tokens = Database.return_level_tokens(player_id, char_id)
        if level_tokens >= 5:
            gear = Database.return_gear(player_id, char_id)
            if gear < 10:
                Database.increase_gear(player_id, char_id, gear, level_tokens)
                return True
            return False
        return False

    @staticmethod
    def exp_to_level(player_id, char_id):
        exp = Database.get_exp(player_id, char_id)
        lvl = Database.return_level(player_id, char_id)
        leg = Database.is_legendary(char_id)
        str_lvl = str(lvl)
        levelable = True
        if len(str_lvl) == 1:
            str_lvl = "0"
        elif len(str_lvl) == 3 and leg == 1 and lvl < 125:
            str_lvl = "l"
        elif len(str_lvl) == 2:
            pass
        else:
            levelable = False

        if levelable:
            exp_threshold = Char_upgrading.levels_dict[str_lvl[0]]
            if exp >= exp_threshold:
                Char_upgrading.Upgrade_char(char_id, player_id, exp_threshold)





if __name__ == '__main__':
    Char_upgrading.Upgrade_char(6,0)
