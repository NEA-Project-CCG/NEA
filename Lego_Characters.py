
from Battle_Classes import Character
from Battle_Calculators import Battle_Calculators
from random import randint
from Multiplier_Calculator import Multiplier
from Database_Querying import Database


class Chase(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        chase_id = 40
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            chase_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, chase_id)


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

        calc_buffs = calc_buffs_and_debuffs[0]
        calc_debuffs = calc_buffs_and_debuffs[1]

        damage = Battle_Calculators.Damage_calculator(self._damage, offense, self._ap, 1000, self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy, 0, defense, evasion)

        health -= damage

        self._special_cooldown = 2

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

        self._crit_avoidance += round(self._crit_avoidance / 10)



        return [buffs, debuffs, offense]


class Gold(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        gold_id = 36
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            gold_id )

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, gold_id)


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
        self._crit_avoidance += round((10 * self._crit_avoidance) / 100)
        return [buffs, debuffs, offense]


class JarJar(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        jarjar_id = 37
        self.stat_multiplier = stat_multiplier
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            jarjar_id)

        if player_id is not None:
            self.stat_multiplier = Multiplier.calculate_stats_player(player_id, jarjar_id)

        self.name: str = stats[1]
        self.stats = stats[2:]

        self.__max_health: int = round((stats[0] * self.stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((stats[1] * self.stat_multiplier) / 1972)
        self._evasion = round((stats[2] * self.stat_multiplier) / 1972)
        self._ap: int = round((stats[3] * self.stat_multiplier) / 1972)
        self._defense: int = round((stats[4] * self.stat_multiplier) / 1972)
        self._crit_chance: int = round((stats[5] * self.stat_multiplier) / 1972)
        self._crit_damage: int = stats[6]
        self._accuracy: int = stats[7]
        self._crit_avoidance: int = round((stats[8] * self.stat_multiplier) / 1972)
        self._speed: int = stats[9]
        self._potency: int = round((stats[10] * self.stat_multiplier) / 1972)
        self._tenacity: int = round((stats[11] * self.stat_multiplier) / 1972)
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
                                                      self._crit_damage, 100, calc_buffs, calc_debuffs, self._accuracy,
                                                      crit_avoidance, defense, evasion)
        health -= damage
        self._ultimate_cooldown = 4
        return health

    def _passive(self, offense: int, Friends: list[str], Enemies: list[str], kbuffs: list[str]) -> list[list[str], list[str], int]:
        buffs = kbuffs
        debuffs = []
        self.__max_health: int = round((randint(0,100000) * self.stat_multiplier) / 1972)
        self._health: int = self.__max_health
        self._damage: int = round((randint(0,11000) * self.stat_multiplier) / 1972)
        self._evasion = round((randint(0,100) * self.stat_multiplier) / 1972)
        self._ap: int = round((randint(0,1000) * self.stat_multiplier) / 1972)
        self._defense: int = round((randint(0,1000) * self.stat_multiplier) / 1972)
        self._crit_chance: int = round((randint(0,150) * self.stat_multiplier) / 1972)
        self._crit_damage: int = randint(100,150)
        self._crit_avoidance: int = round((randint(0,100) * self.stat_multiplier) / 1972)
        self._speed: int = randint(0,600)
        self._potency: int = round((randint(0,100) * self.stat_multiplier) / 1972)
        self._tenacity: int = round((randint(0,100) * self.stat_multiplier) / 1972)
        return [buffs, debuffs, offense]


class Lincoln(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        lincoln_id = 38
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            lincoln_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, lincoln_id)


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
        target_pos = randint(0,len(Enemies.team)-1)
        target = Enemies.team[target_pos]
        target.remove_character(target)
        return [buffs, debuffs, offense]

class Business(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        business_id = 39
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            business_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, business_id)


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
        target_pos = randint(0, len(Enemies.team) - 1)
        target = Enemies.team[target_pos]
        target_stats = target._get_block()
        target_stats._speed -= round(target_stats._speed / 100)
        target_stats._crit_chance -= round(target_stats._crit_chance / 100)
        target_stats._ap -= round(target_stats._ap / 100)
        target_stats._damage -= round(target_stats._damage / 100)
        return [buffs, debuffs, offense]


class Clutch(Character):
    def __init__(self, player_id: int = None, stat_multiplier: int = None, Battle_id: int = None):
        clutch_id = 41
        stats: list[int, str, int, int, int, int, int, int, int, int, int, int, int, int, int] = Database.Get_stats(
            clutch_id)

        if player_id is not None:
            stat_multiplier = Multiplier.calculate_stats_player(player_id, clutch_id)



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
            friend._crit_chance += round(friend._crit_chance / len(Friends.team))
        return [buffs, debuffs, offense]



