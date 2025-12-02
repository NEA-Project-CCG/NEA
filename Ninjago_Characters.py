from Battle_Classes import Character
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier
from Database_Querying import Database


class Kai(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        kai_id = 6
        stats = Database.Get_stats(kai_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, kai_id)

        self.name = stats[0][1]

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
        self._health += damage
        if self._health > self.__max_health:
            self._health = self.__max_health
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
        self._health -= round((self.__max_health * (10 - len(buffs) * 5)) / 100)
        if self._health <= 0:
            self._health = 1
        buffs = ["offense up", "accuracy up", "crit chance up", "crit damage up", "crit avoidance up", "defense up", "evasion up", "potency up", "tenacity up"]
        return [buffs, debuffs, offense]


class Zane(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        zane_id = 7
        stats = Database.Get_stats(zane_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, zane_id)

        stats = stats[zane_id]
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


        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        cbuffs = Battle_Calculators.Buff_calculator(calc_buffs_and_debuffs[0], [4])

        new_buffs = [4]

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

    def _passive(self, debuffs, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        self._ap += round(self._ap / 10)
        return [buffs, debuffs, offense]


class Cole(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        cole_id = 8
        stats = Database.Get_stats(cole_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, cole_id)

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

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        new_buffs = []

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 300, calc_buffs, calc_debuffs,
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
        self._potency += round(self._potency / 5)
        return [buffs, debuffs, offense]


class Jay(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        jay_id = 9
        stats = Database.Get_stats(jay_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, jay_id)

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
        self._speed = round(self._speed / len(Friends.team))
        return [buffs, debuffs, offense]

class Lloyd(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        lloyd_id = 10
        stats = Database.Get_stats(lloyd_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, lloyd_id)


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




        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["offense up", "crit damage up", "tenacity up"])

        new_buffs = ["offense up", "crit damage up", "tenacity up"]

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

        targ = randint(0, len(Enemies.team)-1)

        for i in range(len(Enemies.team)-1, -1, -1):
            if i == targ:
                Enemies.team.targ._health -= Enemies.team.targ._remove_health(round(self.__max_health / 10))


        return [buffs, debuffs, offense]


class Wu(Character):
    def __init__(self, player_id=None, stat_multiplier=None):
        wu_id = 11
        stats = Database.Get_stats(wu_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, wu_id)

        self.name = stats[1]
        stats = stats[2:]

        self.__max_health = round((stats[0] * stat_multiplier)/100000)
        self._health = self.__max_health
        self._damage = round((stats[1] * stat_multiplier)/100000)
        self._evasion = round((stats[2] * stat_multiplier)/100000)
        self._ap = round((stats[3] * stat_multiplier)/100000)
        self._defense = round((stats[4] * stat_multiplier)/100000)
        self._crit_chance = round((stats[5] * stat_multiplier)/100000)
        self._crit_damage = round((stats[6] * stat_multiplier)/100000)
        self._accuracy = stats[7]
        self._crit_avoidance = round((stats[8] * stat_multiplier)/100000)
        self._speed = round((stats[9] * stat_multiplier)/100000)
        self._potency = round((stats[10] * stat_multiplier)/100000)
        self._tenacity = round((stats[11] * stat_multiplier)/100000)


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
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _passive(self, offense, Friends, Enemies, kbuffs):
        buffs = kbuffs
        debuffs = []
        for friend in Friends.team:
            friend.character._speed += round(friend.character._speed / 5)

        return [buffs, debuffs, offense]



