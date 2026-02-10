
from random import randint

#all of the parameters for damage calculation
#specilised calculator that does not include damage variance
# def Damage_calculator_Unit_Test(damage: int, offense: int, ap: int, crit_chance: int, crit_damage: int, ability_modifier: int, buffs: list[int], debuffs:  list[int], accuracy: int, crit_avoidance: int, defense: int, evasion: int) -> int:
#
#     #applies buffs to stats
#     for buff in buffs:
#         #checks if buff is offense up
#         if buff == 1:
#             damage = round((damage * 150) / 100)
#
#         #checks if buff accuracy up
#         if buff == 2:
#             accuracy = round((accuracy * 150) / 100)
#
#         #checks if buff critical chance up
#         if buff == 3:
#             crit_chance = round((crit_chance * 150) / 100)
#
#         #checks if buff critical damage up
#         if buff == 4:
#             crit_damage = round((crit_damage * 150) / 100)
#
#         # checks if buff is critical avoidance up
#         if buff == 5:
#             crit_avoidance = round((crit_avoidance * 150) / 100)
#
#         #checks if buff is defense up
#         if buff == 6:
#             defense = round((defense * 150) / 100)
#
#         #checks if buff is evasion up
#         if buff == 7:
#             evasion = round((evasion * 150) / 100)
#
#
#     for debuff in debuffs:
#         # checks if debuff is offense down
#         if debuff == 1:
#             damage = round((damage / 150) * 100)
#
#         # checks if debuff is accuracy down
#         if debuff == 2:
#             accuracy = round((accuracy / 150) * 100)
#
#         # checks if debuff is critical chance down
#         if debuff == 3:
#             crit_chance = round((crit_chance / 150) * 100)
#
#         # checks if debuff is critical damage down
#         if debuff == 4:
#             crit_damage = round((crit_damage / 150) * 100)
#
#         # checks if debuff is critical avoidance down
#         if debuff == 5:
#             crit_avoidance = round((crit_avoidance / 150) *100)
#
#         # checks if debuff is defense down
#         if debuff == 6:
#             defense = round((defense / 150) * 100)
#
#         # checks if debuff is evasion down
#         if debuff == 7:
#             evasion = round((evasion / 150) * 100)
#
#     #calculates whether there is a hit
#     hit_chance: int = accuracy - evasion
#     if hit_chance < 0:
#         hit_chance = 0
#     hit_rand = randint(0, 100)
#     if hit_chance < hit_rand:
#         damage = 0
#         print("missed")
#         return damage
#
#     #offense is applied to the damage
#     damage = round((damage * offense) / 100)
#
#     #damage variance is calculated and applied
#     #dam_var = randint(95, 105)
#     damage = round((damage * 100) / 100)
#
#     #calculates critical chance
#     crit_chance = crit_chance - crit_avoidance
#     if crit_chance < 0:
#         crit_bool: bool = False
#
#     else:
#         crit_rand: int = randint(0, 100)
#         if crit_chance < crit_rand:
#             crit_bool = False
#         else:
#             crit_bool = True
#
#     if crit_bool:
#         damage = round((damage * crit_damage) / 100)
#
#     calc_defense = defense - ap
#     if calc_defense < 0:
#
#         damage = round(damage * (1000 + abs(calc_defense)) / 1000)
#
#     else:
#         damage = round(damage / (1000 + calc_defense) * 1000)
#
#
#
#     damage = round(round(damage * ability_modifier) / 100)
#
#     return damage

class Battle_Calculators:
    @staticmethod
    def Damage_calculator(damage: int, offense: int, ap: int, crit_chance: int, crit_damage: int, ability_modifier: int, buffs: list[str], debuffs:  list[str], accuracy: int, crit_avoidance: int, defense: int, evasion: int, testing: bool = False) -> int:

        #applies buffs to stats
        for buff in buffs:
            #checks if buff is offense up
            if buff == "offense up":
                damage = round((damage * 150) / 100)

            #checks if buff accuracy up
            if buff == "accuracy up":
                accuracy = round((accuracy * 150) / 100)

            #checks if buff critical chance up
            if buff == "crit chance up":
                crit_chance = round((crit_chance * 150) / 100)

            #checks if buff critical damage up
            if buff == "crit damage up":
                crit_damage = round((crit_damage * 150) / 100)

            # checks if buff is critical avoidance up
            if buff == "crit avoidance up":
                crit_avoidance = round((crit_avoidance * 150) / 100)

            #checks if buff is defense up
            if buff == "defense up":
                defense = round((defense * 150) / 100)

            #checks if buff is evasion up
            if buff == "evasion up":
                evasion = round((evasion * 150) / 100)


        for debuff in debuffs:
            # checks if debuff is offense down
            if debuff == "offense down":
                damage = round((damage / 150) * 100)

            # checks if debuff is accuracy down
            if debuff == "accuracy down":
                accuracy = round((accuracy / 150) * 100)

            # checks if debuff is critical chance down
            if debuff == "crit chance down":
                crit_chance = round((crit_chance / 150) * 100)

            # checks if debuff is critical damage down
            if debuff == "crit damage down":
                crit_damage = round((crit_damage / 150) * 100)

            # checks if debuff is critical avoidance down
            if debuff == "crit avoidance down":
                crit_avoidance = round((crit_avoidance / 150) *100)

            # checks if debuff is defense down
            if debuff == "defense down":
                defense = round((defense / 150) * 100)

            # checks if debuff is evasion down
            if debuff == "evasion down":
                evasion = round((evasion / 150) * 100)

        #calculates whether there is a hit
        hit_chance: int = accuracy - evasion
        if hit_chance < 0:
            hit_chance = 0
        hit_rand = 100 if testing else randint(0, 100)
        if hit_chance < hit_rand:
            print("miss")
            damage = 0
            return damage

        #offense is applied to the damage
        damage = round((damage * offense) / 100)

        #damage variance is calculated and applied
        dam_var = 100 if testing else randint(95, 105)
        damage = round((damage * dam_var) / 100)

        #calculates critical chance
        crit_chance = crit_chance - crit_avoidance
        if crit_chance < 0:
            crit_bool: bool = False

        #calculates critical hit
        else:
            crit_rand: int = 100 if testing else randint(0, 100)
            if crit_chance < crit_rand:
                crit_bool = False
            else:
                crit_bool = True

        #calculates crit damage
        if crit_bool:
            damage = round((damage * crit_damage) / 100)

        #calculates armour penetration
        calc_defense = defense - ap
        if calc_defense < 0:

            damage = round(damage * (1000 + abs(calc_defense)) / 1000)

        else:
            damage = round(damage / (1000 + calc_defense) * 1000)



        damage = round(round(damage * ability_modifier) / 100)

        return damage


    @staticmethod
    def Debuff_Calculator(potency: int, tenacity: int, buffs: list[str], debuffs: list[str], evasion: int, accuracy: int, debuffs_to_be_applied: list[str], rdebuffs: list[str]) -> list[str]:
        #applies buffs
        for buff in buffs:
            #checks if buff is accuracy up
            if buff == "accuracy up":
                accuracy = round((accuracy * 150) / 100)

            # checks if buff is evasion up
            if buff == "evasion up":
                evasion = round((evasion * 150) / 100)

            #checks if buff is potency up
            if buff == "potency up":
                potency = round((potency * 150) / 100)

            #checks if buff is tenacity up
            if buff == "tenacity up":
                tenacity = round((tenacity * 150) / 100)


        #applies debuffs
        for debuff in debuffs:
            #checks if debuff is accuracy down
            if debuff == "accuracy down":
                accuracy = round((accuracy * 50) / 100)

            #checks if debuff is evasion down
            if debuff == "evasion down":
                evasion = round((evasion * 50) / 100)

            #checks if debuff is potency down
            if debuff == "potency down":
                potency = round((potency * 50) / 100)

            #checks if debuff is tenacity down
            if debuff == "tenacity down":
                tenacity = round((tenacity * 50) / 100)


        #creates accuracy for calculating
        calc_acc = accuracy - round(evasion / 2)
        #creates random number to compare against calculated accuracy
        rand_acc = randint(0, 100)
        #checks whether it is a hit
        if calc_acc < rand_acc:
            print("miss")
            return rdebuffs


        #calculates potency
        calc_pot = potency - tenacity
        if calc_pot < 0:
            return rdebuffs

        #calculates whether the potency works
        rand_pot =  randint(0, 100)
        if calc_pot < rand_pot:
            return rdebuffs
        #applies debuffs
        for application in debuffs_to_be_applied:
            rdebuffs.append(application)

        rdebuffs_set = set(rdebuffs)
        rdebuffs = []
        for debuff in rdebuffs_set:
            rdebuffs.append(debuff)
        rdebuffs.sort()

        return rdebuffs

    @staticmethod
    def Buff_calculator(buffs: list[str], buffs_to_be_applied: list[str]) -> list[str]:
        for application in buffs_to_be_applied:
            buffs.append(application)

        #applies buffs
        buffs_set = set(buffs)
        buffs = []
        for buff in buffs_set:
            buffs.append(buff)
        buffs.sort()

        return buffs

    @staticmethod
    def resolve_damage_buffs(buffs: list[str], debuffs: list[str], other_buffs: list[str], other_debuffs: list[str]) -> list[list[str], list[str]]:
        #formats buffs and debuffs in a way for the damage calculator

        enemy_calc_buffs = []
        for buff in buffs:
            if buff not in ["offense up", "accuracy up", "crit chance up", "crit damage up", "potency up"]:
                enemy_calc_buffs.append(buff)

        player_calc_buffs = []
        for buff in other_buffs:
            if buff in ["offense up", "accuracy up", "crit chance up", "crit damage up", "potency up"]:
                player_calc_buffs.append(buff)

        calc_buffs = player_calc_buffs + enemy_calc_buffs

        enemy_calc_debuffs = []
        for debuff in debuffs:
            if debuff not in ["offense up", "accuracy up", "crit chance up", "crit damage up", "potency up"]:
                enemy_calc_debuffs.append(debuff)

        player_calc_debuffs = []
        for debuff in other_debuffs:
            if debuff in ["offense up", "accuracy up", "crit chance up", "crit damage up", "potency up"]:
                player_calc_debuffs.append(debuff)

        calc_debuffs = player_calc_debuffs + enemy_calc_debuffs

        for i in range(1, 8):
            if i in calc_debuffs and i in calc_buffs:
                calc_buffs.remove(i)
                calc_buffs.remove(i)

        return [calc_buffs, calc_debuffs]
