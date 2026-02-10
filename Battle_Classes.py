

class BattleField:
    def __init__(self):
        self.battlefield: list[Team] = []
        self.__player_team = 0
        self.__enemy_team = 1

    def check_victory(self) -> bool:
        if self.battlefield[self.__player_team].team != [] and self.battlefield[self.__enemy_team].team == []:
            return True
        return False

    def check_defeat(self) -> bool:
        if self.battlefield[self.__player_team].team == [] and self.battlefield[self.__enemy_team].team != []:
            return True
        return False

    def add_team(self, team):
        self.battlefield.append(team)

    def display_battlefield(self):
        for i in range(2):
            print(f"Team {i + 1}:")
            self.battlefield[i]._display_team()

    def opposing_team(self):
        index = self.queue._speeds[9][1]
        if index >= 5:
            return self.battlefield[self.__player_team], 1
        return self.battlefield[self.__enemy_team], 0

    def add_queue(self, queue):
        self.queue = queue



class Team:
    def __init__(self, Battle):
        self.team: list[Character] = []
        self.BattleField_that_owns = Battle

    def add_character(self, character):
        self.team.append(character)

    def remove_character(self, character):
        self.team.remove(character)
        self.BattleField_that_owns.queue.remove_character(character)


    def _display_team(self):
        string = ""
        for character in self.team:
            string += character._display_character()
            string += ", "

        string = string[:-2]
        string = "[" + string + "]"
        print(string)



class Character:
    def __init__(self, character, team: Team):
        self.team_that_owns_me = team
        self.character = character

        self._offense = 100
        self._buffs = []
        self._debuffs = []
        self._target = 0
        self._continuing_buffs = []

    def _remove_health(self, reduced_health):
        self.character._health = reduced_health
        if self.character._health <= 0:
            self.character._health = 0
            self.team_that_owns_me.remove_character(self)




    def __ult_remove_health(self, reduced_health):
        self.character._health = reduced_health

    def basic(self, Team: list):
        attacking_character_char = Team.team[self._target]
        attacking_character = attacking_character_char._get_block()

        reduced_health = self.character._basic(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                               attacking_character.GetCrit_avoidance(), attacking_character.GetHealth(),
                                               attacking_character_char._buffs, attacking_character_char._debuffs,
                                               self._offense, self._buffs, self._debuffs)

        attacking_character_char._remove_health(reduced_health)

    def special(self, Team: list):
        attacking_character_char = Team.team[self._target]
        attacking_character = attacking_character_char._get_block()

        special_data = self.character._special(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                               attacking_character.GetCrit_avoidance(), attacking_character.GetHealth(),
                                               attacking_character_char._buffs, attacking_character_char._debuffs,
                                               self._offense, self._buffs, self._debuffs, attacking_character.GetTenacity())

        attacking_character_char._remove_health(special_data[0])
        attacking_character_char._buffs = special_data[1]
        attacking_character_char._debuffs = special_data[2]
        self._buffs = special_data[3]
        self._debuffs = special_data[4]
        self._offense = special_data[5]
        self._continuing_buffs = special_data[6]

    def ultimate(self, Team: list):
        attacking_character_char = Team.team


        for character in attacking_character_char:
            attacking_character = character._get_block()

            reduced_health = (self.character._ultimate(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                                   attacking_character.GetCrit_avoidance(),
                                                   attacking_character.GetHealth(),
                                                   character._buffs, character._debuffs,
                                                   self._offense, self._buffs, self._debuffs))

            character.__ult_remove_health(reduced_health)

        for i in range(len(attacking_character_char)-1, -1, -1):
            attacking_character_char[i]._remove_health(attacking_character_char[i].character._health)




    def passive(self, Team2):
        if len(Team2.team) != 0:

            changes = self.character._passive(self._offense, self.team_that_owns_me, Team2, self._continuing_buffs)

            self._buffs = changes[0]
            self._debuffs = changes[1]
            self._offense = changes[2]




    def _display_character(self):
        return self.character.GetName()

    def _get_block(self):
        return self.character











