from Database_Querying import Database

class Char_upgrading:

    @staticmethod
    def upgrade_existing_char(char_id, player_id):
        Database.return_level_and_tokens(player_id, char_id)
