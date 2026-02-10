
from Battle_Classes import Character
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier
from Database_Querying import Database


class Luke(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        luke_id = 18
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            luke_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, luke_id)


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
        new_buffs = []

        self._damage += defense

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        debuffs = []
        buffs = kbuffs



        return [buffs, debuffs, offense]


class Kenobi(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        kenobi_id = 19
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            kenobi_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, kenobi_id)


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
        #grants defense up



        new_buffs = []

        #applies defense down

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
        target_stats._accuracy -= round(target_stats._accuracy / 100)
        return [buffs, debuffs, offense]


class Dooku(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        dooku_id = 20
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            dooku_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, dooku_id)


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

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 300, calc_buffs, calc_debuffs,
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
        self._accuracy += round(self._accuracy / 5)
        return [buffs, debuffs, offense]


class Ahsoka(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        ahsoka_id = 21
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            ahsoka_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, ahsoka_id)


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

        self._speed += round(self._speed / 20)

        new_buffs = []

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
        self._speed += round(self._speed / 50)
        return [buffs, debuffs, offense]

class Din(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        din_id = 22
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            din_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, din_id)


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

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 150, calc_buffs, calc_debuffs,
                                                      self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance,
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self._crit_avoidance += round(self._ap / 10)
        return [buffs, debuffs, offense]


class Maul(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        maul_id = 23
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            maul_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, maul_id)


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
        self.__turns = 0



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

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        new_buffs = []

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
                                                      self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self.__turns += 1
        self._damage += round(self._health/100) * (2**self.__turns)
        self._crit_damage += round(self._health / 100) * (2 ** self.__turns)
        self._ap += round(self._health / 100) * (2 ** self.__turns)
        self._speed += round(self._health / 100) * (2 ** self.__turns)
        self._health -= round(self._health / 1000) * (2 ** self.__turns)

        return [buffs, debuffs, offense]



