from Database_Querying import Database

class Char_upgrading:

    @staticmethod
    def Unlock_char(player_id, char_id):
        Database.collect_character(player_id, char_id)

    @staticmethod
    def Upgrade_char(char_id, player_id):
        level = Database.return_level(player_id, char_id)
        if level < 100 and (char_id + 1) % 6 != 0:
            Database.increase_level(player_id, char_id)
        elif level < 150 and (char_id + 1) % 6 == 1:
            Database.increase_level(player_id, char_id)

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
                Database.increase_gear(player_id, char_id, gear)
                return True
            return False
        return False




if __name__ == '__main__':
    Char_upgrading.Upgrade_star(6,0)
