from random import randint

#all of the parameters for damage calculation
#specilised calculator that does not include damage variance
def Damage_calculator_Unit_Test(damage: int, offense: int, ap: int, crit_chance: int, crit_damage: int, ability_modifier: int, buffs: list[int], debuffs:  list[int], accuracy: int, crit_avoidance: int, defense: int, evasion: int) -> int:

    #applies buffs to stats
    for buff in buffs:
        #checks if buff is offense up
        if buff == 1:
            damage = round((damage * 150) / 100)

        #checks if buff accuracy up
        if buff == 2:
            accuracy = round((accuracy * 150) / 100)

        #checks if buff critical chance up
        if buff == 3:
            crit_chance = round((crit_chance * 150) / 100)

        #checks if buff critical damage up
        if buff == 4:
            crit_damage = round((crit_damage * 150) / 100)

        # checks if buff is critical avoidance up
        if buff == 5:
            crit_avoidance = round((crit_avoidance * 150) / 100)

        #checks if buff is defense up
        if buff == 6:
            defense = round((defense * 150) / 100)

        #checks if buff is evasion up
        if buff == 7:
            evasion = round((evasion * 150) / 100)


    for debuff in debuffs:
        # checks if debuff is offense down
        if debuff == 1:
            damage = round((damage / 150) * 100)

        # checks if debuff is accuracy down
        if debuff == 2:
            accuracy = round((accuracy / 150) * 100)

        # checks if debuff is critical chance down
        if debuff == 3:
            crit_chance = round((crit_chance / 150) * 100)

        # checks if debuff is critical damage down
        if debuff == 4:
            crit_damage = round((crit_damage / 150) * 100)

        # checks if debuff is critical avoidance down
        if debuff == 5:
            crit_avoidance = round((crit_avoidance / 150) *100)

        # checks if debuff is defense down
        if debuff == 6:
            defense = round((defense / 150) * 100)

        # checks if debuff is evasion down
        if debuff == 7:
            evasion = round((evasion / 150) * 100)

    #calculates whether there is a hit
    hit_chance: int = accuracy - evasion
    if hit_chance < 0:
        hit_chance = 0
    hit_rand = randint(0, 100)
    if hit_chance < hit_rand:
        damage = 0
        print("missed")
        return damage

    #offense is applied to the damage
    damage = round((damage * offense) / 100)

    #damage variance is calculated and applied
    #dam_var = randint(95, 105)
    damage = round((damage * 100) / 100)

    #calculates critical chance
    crit_chance = crit_chance - crit_avoidance
    if crit_chance < 0:
        crit_bool: bool = False

    else:
        crit_rand: int = randint(0, 100)
        if crit_chance < crit_rand:
            crit_bool = False
        else:
            crit_bool = True

    if crit_bool:
        damage = round((damage * crit_damage) / 100)

    calc_defense = defense - ap
    if calc_defense < 0:

        damage = round(damage * (1000 + abs(calc_defense)) / 1000)

    else:
        damage = round(damage / (1000 + calc_defense) * 1000)



    damage = round(round(damage * ability_modifier) / 100)

    return damage


def Damage_calculator(damage: int, offense: int, ap: int, crit_chance: int, crit_damage: int, ability_modifier: int, buffs: list[int], debuffs:  list[int], accuracy: int, crit_avoidance: int, defense: int, evasion: int) -> int:

    #applies buffs to stats
    for buff in buffs:
        #checks if buff is offense up
        if buff == 1:
            damage = round((damage * 150) / 100)

        #checks if buff accuracy up
        if buff == 2:
            accuracy = round((accuracy * 150) / 100)

        #checks if buff critical chance up
        if buff == 3:
            crit_chance = round((crit_chance * 150) / 100)

        #checks if buff critical damage up
        if buff == 4:
            crit_damage = round((crit_damage * 150) / 100)

        # checks if buff is critical avoidance up
        if buff == 5:
            crit_avoidance = round((crit_avoidance * 150) / 100)

        #checks if buff is defense up
        if buff == 6:
            defense = round((defense * 150) / 100)

        #checks if buff is evasion up
        if buff == 7:
            evasion = round((evasion * 150) / 100)


    for debuff in debuffs:
        # checks if debuff is offense down
        if debuff == 1:
            damage = round((damage / 150) * 100)

        # checks if debuff is accuracy down
        if debuff == 2:
            accuracy = round((accuracy / 150) * 100)

        # checks if debuff is critical chance down
        if debuff == 3:
            crit_chance = round((crit_chance / 150) * 100)

        # checks if debuff is critical damage down
        if debuff == 4:
            crit_damage = round((crit_damage / 150) * 100)

        # checks if debuff is critical avoidance down
        if debuff == 5:
            crit_avoidance = round((crit_avoidance / 150) *100)

        # checks if debuff is defense down
        if debuff == 6:
            defense = round((defense / 150) * 100)

        # checks if debuff is evasion down
        if debuff == 7:
            evasion = round((evasion / 150) * 100)

    #calculates whether there is a hit
    hit_chance: int = accuracy - evasion
    if hit_chance < 0:
        hit_chance = 0
    hit_rand = randint(0, 100)
    if hit_chance < hit_rand:
        damage = 0
        return damage

    #offense is applied to the damage
    damage = round((damage * offense) / 100)

    #damage variance is calculated and applied
    dam_var = randint(95, 105)
    damage = round((damage * dam_var) / 100)

    #calculates critical chance
    crit_chance = crit_chance - crit_avoidance
    if crit_chance < 0:
        crit_bool: bool = False

    else:
        crit_rand: int = randint(0, 100)
        if crit_chance < crit_rand:
            crit_bool = False
        else:
            crit_bool = True

    if crit_bool:
        damage = round((damage * crit_damage) / 100)

    calc_defense = defense - ap
    if calc_defense < 0:

        damage = round(damage * (1000 + abs(calc_defense)) / 1000)

    else:
        damage = round(damage / (1000 + calc_defense) * 1000)



    damage = round(round(damage * ability_modifier) / 100)

    return damage

def Debuff_Calculator(potency: int, tenacity: int, buffs: list[int], debuffs: list[int], evasion: int, accuracy: int, debuffs_to_be_applied: list[int]) -> list[int]:
    #applies buffs
    for buff in buffs:
        #checks if buff is accuracy up
        if buff == 2:
            accuracy = round((accuracy * 150) / 100)

        # checks if buff is evasion up
        if buff == 7:
            evasion = round((evasion * 150) / 100)

        #checks if buff is potency up
        if buff == 8:
            potency = round((potency * 150) / 100)

        #checks if buff is tenacity up
        if buff == 9:
            tenacity = round((tenacity * 150) / 100)


    #applies debuffs
    for defbuff in debuffs:
        #checks if debuff is accuracy down
        if defbuff == 2:
            accuracy = round((accuracy * 50) / 100)

        #checks if debuff is evasion down
        if defbuff == 7:
            evasion = round((evasion * 50) / 100)

        #checks if debuff is potency down
        if defbuff == 8:
            potency = round((potency * 50) / 100)

        #checks if debuff is tenacity down
        if defbuff == 9:
            tenacity = round((tenacity * 50) / 100)


    #creates accuracy for calculating
    calc_acc = accuracy - round(evasion / 2)
    #creates random number to compare against calculated accuracy
    rand_acc = randint(0, 100)
    #checks whether it is a hit
    if calc_acc < rand_acc:
        print("missed")
        return debuffs



    calc_pot = potency - tenacity
    if calc_pot < 0:
        return debuffs
    rand_pot =  randint(0, 100)
    if calc_pot < rand_pot:
        print("resisted")
        return debuffs
    for application in debuffs_to_be_applied:
        debuffs.append(application)

    debuffs_set = set(debuffs)
    debuffs = []
    for debuff in debuffs_set:
        debuffs.append(debuff)
    debuffs.sort()

    return debuffs


def Buff_calculator(buffs: list[int], buffs_to_be_applied: list[int]) -> list[int]:
    for application in buffs_to_be_applied:
        buffs.append(application)

    buffs_set = set(buffs)
    buffs = []
    for buff in buffs_set:
        buffs.append(buff)
    buffs.sort()

    return buffs



if __name__ == "__main__":
    test_data_1 = [1500, 100, 500, 100, 150, 100, [], [], 100, 0, 0, 0]

    result = Damage_calculator(test_data_1[0], test_data_1[1], test_data_1[2], test_data_1[3], test_data_1[4], test_data_1[5], test_data_1[6], test_data_1[7], test_data_1[8], test_data_1[9], test_data_1[10], test_data_1[11])

    print(result)
