from Database_Querying import Database
from Campaign_logic import Campaign_Logic
from Multiplier_Calculator import Multiplier


class Journeys:
    @staticmethod
    def check_eligibility(Player_id, Journey_id):
        reqs = Database.return_Journey_reqs(Journey_id)
        Valid = 0
        for i in range(5):
            gear = Database.return_gear(Player_id, reqs[i])
            star = Database.return_star(Player_id, reqs[i])
            if gear >= reqs[5] and star >= reqs[6]:
                Valid +=1
            else:
                Valid = -20

        if Valid < 0:
            return False
        Database.reqs_completed(Journey_id, Player_id)

    @staticmethod
    def start_battle(battle_id, player_id, Journey_id):
        Campaign_chars = Database.Get_Campaign_Chars(battle_id)

        Enemy_level, Enemy_gear, Enemy_star = Database.Get_Multiplier_levels(battle_id)

        multiplier = Multiplier.calculate_stats_enemy(Enemy_level, Enemy_gear, Enemy_star)

        CharDict: dict[Character] = {}
        for i in range(5):
            CharDict["EChar" + str(i + 1)] = Campaign_Logic.init_Echar(Campaign_chars[i], multiplier)

        chars = Journeys.PChars(player_id, Journey_id)
        for i in range(5):
            CharDict["PChar" + str(i + 1)] = Campaign_Logic.init_Pchar(chars[i], player_id)

        return CharDict

    @staticmethod
    def PChars(player_id, Journey_id):
        reqs = Database.return_Journey_reqs(Journey_id)
        chars = []
        for i in range(5):
            chars.append(reqs[i])

        return chars

    @staticmethod
    def Journey_rewards(Player_id, Journey_id):
        char_id = Database.Journey_reward(Journey_id)
        has_char = Database.has_char(char_id)
        if not has_char:
            Database.collect_character(Player_id, char_id)


    @staticmethod
    def end_battle(battle_id, player_id, journey_id):
        stage = Database.Stage_from_id(battle_id)
        Database.Unlock_next_journey(player_id, battle_id)
        if stage == 5:
            Journeys.Journey_rewards(player_id, journey_id)


