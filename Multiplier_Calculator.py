from Database_Querying import Database





class Multiplier:
    @staticmethod
    def __overall_multiplier(level, gear, star):
        multiplier_l = Multiplier.level_multiplier(level)
        multiplier_g = Multiplier.gear_multiplier(gear)
        multiplier_s = Multiplier.star_multiplier(star)

        total_m = ((2*multiplier_l) +(4*multiplier_g) + (4*multiplier_s))

        return total_m

    @staticmethod
    def calculate_stats_player(player_id, character_id):

        level, gear, star = Database.Get_Player_Char_multiplier_stats(player_id, character_id)

        stat_multiplier = Multiplier.__overall_multiplier(level, gear, star)


        return stat_multiplier

    @staticmethod
    def calculate_stats_enemy(level, gear, star):
        stat_multiplier = Multiplier.__overall_multiplier(level, gear, star)

        return stat_multiplier


        
    @staticmethod
    def level_multiplier(level):

        level_m = level


        return level_m

    @staticmethod
    def gear_multiplier(gear):
        gear_m = gear**2
        return gear_m

    @staticmethod
    def star_multiplier(star):
        star_m = star**3
        return star_m

    @staticmethod
    def EXP_Calculator(Chapter, Stage):
        exp1 = Stage * 100
        exp2 = (Chapter ** Chapter) * 100
        total_exp = exp1 + exp2
        return total_exp
