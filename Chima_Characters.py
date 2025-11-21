from Battle_Classes import Character
import sqlite3
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier


class Cragger(Character):
    def __init__(self, player_id):
        cragger_id = 0
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM General_character;''')

        stats = cursor.fetchall()


        stat_multiplier = Multiplier.calculate_stats(player_id, cragger_id)

        stats = stats[cragger_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()



    def GetHealth(self):
        return self._health
    def GetDamage(self):
        return self._damage
    def GetEvasion(self):
        return self._evasion
    def GetAp(self):
        return self._ap
    def GetDefense(self):
        return self._defense
    def GetCrit_chance(self):
        return self._crit_chance
    def GetCrit_damage(self):
        return self._crit_damage
    def GetAccuracy(self):
        return self._accuracy
    def GetCrit_avoidance(self):
        return self._crit_avoidance
    def GetSpeed(self):
        return self._speed
    def GetPotency(self):
        return self._potency
    def GetTenacity(self):
        return self._tenacity
    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 130, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)
        new_buffs = []

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, 1000, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, 0, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        debuffs = []
        buffs = kbuffs

        self._crit_avoidance += round(self._crit_avoidance / 10)

        return [buffs, debuffs, offense]


class Gorzan(Character):
    def __init__(self, player_id):
        gorzan_id = 1
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM General_character''')

        stats = cursor.fetchall()

        stat_multiplier = Multiplier.calculate_stats(player_id, gorzan_id)

        stats = stats[gorzan_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()



    def GetHealth(self):
        return self._health
    def GetDamage(self):
        return self._damage
    def GetEvasion(self):
        return self._evasion
    def GetAp(self):
        return self._ap
    def GetDefense(self):
        return self._defense
    def GetCrit_chance(self):
        return self._crit_chance
    def GetCrit_damage(self):
        return self._crit_damage
    def GetAccuracy(self):
        return self._accuracy
    def GetCrit_avoidance(self):
        return self._crit_avoidance
    def GetSpeed(self):
        return self._speed
    def GetPotency(self):
        return self._potency
    def GetTenacity(self):
        return self._tenacity
    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):
        #grants defense up

        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["defense up"])

        new_buffs = ["defense up"]

        #applies defense down

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        debuffs = Battle_Calculators.Debuff_Calculator(self._potency, tenacity, calc_buffs_and_debuffs[0], calc_buffs_and_debuffs[1], evasion, self._accuracy, ["defense down"], debuffs)

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]


        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        self._health += round((10 * self.__max_health) / 100)
        return [buffs, debuffs, offense]


class Eris(Character):
    def __init__(self, player_id):
        eris_id = 2
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT *
                          FROM General_character''')

        stats = cursor.fetchall()

        stat_multiplier = Multiplier.calculate_stats(player_id, eris_id)

        stats = stats[eris_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()

    def GetHealth(self):
        return self._health

    def GetDamage(self):
        return self._damage

    def GetEvasion(self):
        return self._evasion

    def GetAp(self):
        return self._ap

    def GetDefense(self):
        return self._defense

    def GetCrit_chance(self):
        return self._crit_chance

    def GetCrit_damage(self):
        return self._crit_damage

    def GetAccuracy(self):
        return self._accuracy

    def GetCrit_avoidance(self):
        return self._crit_avoidance

    def GetSpeed(self):
        return self._speed

    def GetPotency(self):
        return self._potency

    def GetTenacity(self):
        return self._tenacity

    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 120, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):

        self._speed += round((2 * self._speed) / 100)

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 40, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        self._speed += round(self._speed / 100)
        return [buffs, debuffs, offense]


class Razar(Character):
    def __init__(self, player_id):
        razar_id = 3
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT *
                          FROM General_character''')

        stats = cursor.fetchall()

        stat_multiplier = Multiplier.calculate_stats(player_id, razar_id)

        stats = stats[razar_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()

    def GetHealth(self):
        return self._health

    def GetDamage(self):
        return self._damage

    def GetEvasion(self):
        return self._evasion

    def GetAp(self):
        return self._ap

    def GetDefense(self):
        return self._defense

    def GetCrit_chance(self):
        return self._crit_chance

    def GetCrit_damage(self):
        return self._crit_damage

    def GetAccuracy(self):
        return self._accuracy

    def GetCrit_avoidance(self):
        return self._crit_avoidance

    def GetSpeed(self):
        return self._speed

    def GetPotency(self):
        return self._potency

    def GetTenacity(self):
        return self._tenacity

    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):

        self._speed += round(self._speed / 20)

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        target_pos = randint(0,len(Enemies.team)-1)
        target = Enemies.team[target_pos]
        target_stats = target._get_block()
        target_stats._speed -= round(target_stats._speed / 100)
        return [buffs, debuffs, offense]

class Rinona(Character):
    def __init__(self, player_id):
        rinona_id = 4
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT *
                          FROM General_character''')

        stats = cursor.fetchall()

        stat_multiplier = Multiplier.calculate_stats(player_id, rinona_id)

        stats = stats[rinona_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()

    def GetHealth(self):
        return self._health

    def GetDamage(self):
        return self._damage

    def GetEvasion(self):
        return self._evasion

    def GetAp(self):
        return self._ap

    def GetDefense(self):
        return self._defense

    def GetCrit_chance(self):
        return self._crit_chance

    def GetCrit_damage(self):
        return self._crit_damage

    def GetAccuracy(self):
        return self._accuracy

    def GetCrit_avoidance(self):
        return self._crit_avoidance

    def GetSpeed(self):
        return self._speed

    def GetPotency(self):
        return self._potency

    def GetTenacity(self):
        return self._tenacity

    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):
        # grants defense up
        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, [6])

        new_buffs = ["defense up"]

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        self._defense += round(self._defense / 10)
        return [buffs, debuffs, offense]


class Laval(Character):
    def __init__(self, player_id):
        laval_id = 5
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT *
                          FROM General_character''')

        stats = cursor.fetchall()

        stat_multiplier = Multiplier.calculate_stats(player_id, laval_id)

        stats = stats[laval_id]
        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier) / 100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier) / 100000)
        self._evasion = round((stats[2] * stat_multiplier) / 100000)
        self._ap = round((stats[3] * stat_multiplier) / 100000)
        self._defense = round((stats[4] * stat_multiplier) / 100000)
        self._crit_chance = round((stats[5] * stat_multiplier) / 100000)
        self._crit_damage = round((stats[6] * stat_multiplier) / 100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier) / 100000)
        self._speed = round((stats[9] * stat_multiplier) / 100000)
        self._potency = round((stats[10] * stat_multiplier) / 100000)
        self._tenacity = round((stats[11] * stat_multiplier) / 100000)

        conn.close()

    def GetHealth(self):
        return self._health

    def GetDamage(self):
        return self._damage

    def GetEvasion(self):
        return self._evasion

    def GetAp(self):
        return self._ap

    def GetDefense(self):
        return self._defense

    def GetCrit_chance(self):
        return self._crit_chance

    def GetCrit_damage(self):
        return self._crit_damage

    def GetAccuracy(self):
        return self._accuracy

    def GetCrit_avoidance(self):
        return self._crit_avoidance

    def GetSpeed(self):
        return self._speed

    def GetPotency(self):
        return self._potency

    def GetTenacity(self):
        return self._tenacity

    def GetName(self):
        return self.name

    def _basic(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs, tenacity):

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        new_buffs = []

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 200, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense, evasion, crit_avoidance, health, buffs, debuffs, offense, cbuffs, cdebuffs):

        cbuffs.append(1)
        cbuffs.append(4)

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        for friend in Friends.team:
            friend._offense += round(friend._offense / len(Friends.team))
            offense = friend._offense

        return [buffs, debuffs, offense]



