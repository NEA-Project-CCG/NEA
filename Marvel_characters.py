
from Battle_Classes import Character
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier
from Database_Querying import Database


class Daredevil(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        daredevil_id = 12
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            daredevil_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, daredevil_id)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0



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
        return  self.name

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 130, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)
        new_buffs = ["offense up"]

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        debuffs = []
        buffs = kbuffs

        self._evasion += round(self._evasion / 50)



        return [buffs, debuffs, offense]


class Gambit(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        gambit_id = 13
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            gambit_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, gambit_id)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0





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

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:
        #grants accuracy up

        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["accuracy up"])

        new_buffs = ["accuracy up"]


        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        debuffs = Battle_Calculators.Debuff_Calculator(self._potency, tenacity, calc_buffs_and_debuffs[0], calc_buffs_and_debuffs[1], evasion, self._accuracy, ["defense down"], debuffs)

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]


        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        target_pos = randint(0, len(Enemies.team) - 1)
        target = Enemies.team[target_pos]
        target_stats = target._get_block()
        target_stats._evasion -= round(target_stats._evasion / 100)
        return [buffs, debuffs, offense]


class Spiderman(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        spiderman_id = 14
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            spiderman_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, stats)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0



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
        return  self.name

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 120, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:

        self._speed += round((2 * self._speed) / 100)

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        for i in range(2):

            damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                          self._crit_damage, 70, calc_buffs, calc_debuffs,
                                                          self._accuracy, crit_avoidance, defense, evasion)

            health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 40, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self._evasion += round(self._evasion / 50)
        return [buffs, debuffs, offense]


class Storm(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        storm_id = 15
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            storm_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, storm_id)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0


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
        return  self.name

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:

        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["crit damage up"])

        new_buffs = ["crit damage up"]

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self._crit_damage += round(self._defense / 100)
        return [buffs, debuffs, offense]

class Sentry(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        sentry_id = 16
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            sentry_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, sentry_id)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0

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
        return  self.name

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage

        return health

    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:
        # grants defense up


        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)



        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        debuffs = Battle_Calculators.Debuff_Calculator(self._potency, tenacity, calc_buffs, calc_debuffs, evasion, self._accuracy, ["offense down"], debuffs)

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 50, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 75, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self._defense += round(self._defense / 10)
        return [buffs, debuffs, offense]


class Doom(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        doom_id = 17
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            doom_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, doom_id)


        self.name: str = stats[1]
        stats = stats[2:]

        self.__max_health: int = round((stats[0] * stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * stat_multiplier) / 1972)
        self._evasion = round((stats[2] * stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * stat_multiplier) / 1972)
        self._special_cooldown: int = 0
        self._ultimate_cooldown: int = 0



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
        return  self.name

    def _basic(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health

    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:

        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["offense up", "crit damage up"])

        new_buffs = ["offense up", "crit damage up"]

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 200, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:


        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        for friend in Friends.team:
            friend._defense += round(friend._defense / len(Friends.team))


        return [buffs, debuffs, offense]



