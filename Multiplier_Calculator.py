import sqlite3






class Multiplier:
    @staticmethod
    def overall_multiplier(level, gear, star):
        multiplier_l = Multiplier.level_multiplier(level)
        multiplier_g = Multiplier.gear_multiplier(gear)
        multiplier_s = Multiplier.star_multiplier(star)

        total_m = (multiplier_l * multiplier_g * multiplier_s)

        return total_m

    @staticmethod
    def calculate_stats(player_id, character_id):
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()

        vals = conn.execute('''SELECT Level, Gear, Star FROM Player_Table;
                     WHERE Player_id = ?;
                     AND Character_id = ?;''', (player_id, character_id))

        level = vals.fetchone()[0]
        gear = vals.fetchone()[1]
        star = vals.fetchone()[2]

        stat_multiplier = Multiplier.overall_multiplier(level, gear, star)

        conn.close()

        return stat_multiplier
        
    @staticmethod
    def level_multiplier(level):
        level_m = level


        return level_m

    @staticmethod
    def gear_multiplier(gear):
        gear_m = gear * 10
        return gear_m

    @staticmethod
    def star_multiplier(star):
        star_m = star * 14
        return star_m
