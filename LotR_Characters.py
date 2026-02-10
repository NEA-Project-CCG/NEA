
from Battle_Classes import Character
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier
from Database_Querying import Database


class Aragorn(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        aragorn_id = 30
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            aragorn_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, aragorn_id)


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

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)
        new_buffs = []

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap**2, self._crit_chance, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

        health -= damage

        self._special_cooldown = 2

        return [health, buffs, debuffs, cbuffs, cdebuffs, offense, new_buffs]

    def _ultimate(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str]) -> int:
        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 150, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        debuffs = []
        buffs = kbuffs

        self._ap += round(self._ap / len(Enemies))



        return [buffs, debuffs, offense]


class Tom(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        tom_id = 31
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            tom_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, tom_id)


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

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 50, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)
        health -= damage
        return health


    def _special(self, defense: int, evasion: int, crit_avoidance: int, health: int, buffs: list[str], debuffs: list[str], offense: int, cbuffs: list[str], cdebuffs: list[str], tenacity: int) -> list[int, list[str], list[str], list[str], list[str], int, list[str]]:

        new_buffs = []

        calc_buffs_and_debuffs = Battle_Calculators.resolve_damage_buffs(buffs, debuffs, cbuffs, cdebuffs)

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]


        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, self._crit_chance, self._crit_damage, 60, calc_buffs, calc_debuffs, self._accuracy, crit_avoidance, defense, evasion)

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
        return [buffs, debuffs, offense]


class Samwise(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        samwise_id = 32
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            samwise_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, samwise_id)


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

        self.__max_health = round(self.__max_health / 100)

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
                                                      self._crit_damage, 70, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self.__max_health += round(self.__max_health / 10)
        self._health += round(self.__max_health / 10)
        if self._health > self.__max_health:
            self._health = self.__max_health
        return [buffs, debuffs, offense]


class Sauron(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        sauron_id = 33
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            sauron_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, sauron_id)


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
        if damage > 0:
            print("You trifled with the wrong wizard!")

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

        if damage > 0:
            print("You trifled with the wrong wizard!")

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
        if damage > 0:
            print("You trifled with the wrong wizard!")

        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self.__turns += 1
        self._accuracy += (1 * (self.__turns**self.__turns))
        return [buffs, debuffs, offense]

class Gollum(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        gollum_id = 34
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            gollum_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, gollum_id)


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
        cbuffs = Battle_Calculators.Buff_calculator(cbuffs, ["defense up"])

        new_buffs = ["defense up"]

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
        self._health = self.__max_health
        return [buffs, debuffs, offense]


class Gandalf(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        gandalf_id = 35
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            gandalf_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, gandalf_id)

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
        for friend in Friends.team:
            friend._accuracy += round(friend._accuracy / len(Friends.team))

        return [buffs, debuffs, offense]



