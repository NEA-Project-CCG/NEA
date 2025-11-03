

class BattleField:
    def __init__(self):
        self.__battlefield: list[Team] = []

    def check_victory(self, Battle) -> bool:
        if Battle.__battlefield[0].team != [] and Battle.__battlefield[1].team == []:
            Battle.__reset_battlefield()
            print("victory")
            return True
        return False

    def check_defeat(self, Battle) -> bool:
        if Battle.__battlefield[0] == [] and Battle.__battlefield[1] != []:
            Battle.__reset_battlefield()
            print("lose")
            return True
        return False

    def add_team(self, team):
        self.__battlefield.append(team)


    def __reset_battlefield(self):
        self.__battlefield = []

    def display_battlefield(self):
        for i in range(2):
            print(f"Team {i + 1}:")
            self.__battlefield[i]._display_team()


class Team(BattleField):
    def __init__(self):
        BattleField.__init__(self)
        self.team: list[Character] = []

    def add_character(self, character):
        self.team.append(character)

    def remove_character(self, Team, Battle):
        Team.team.remove(self)
        if Battle.check_victory(Battle):
            return True
        Battle.check_defeat(Battle)

    def _display_team(self):
        string = ""
        for character in self.team:
            string += character._display_character()
            string += ", "

        string = string[:-2]
        string = "[" + string + "]"
        print(string)



class Character(Team):
    def __init__(self, character):
        Team.__init__(self)
        self.character = character

        self._offense = 100
        self._buffs = []
        self._debuffs = []
        self._target = 0
        self._continuing_buffs = []

    def _remove_health(self, reduced_health, Team, Battle):
        self.character._health = reduced_health
        if self.character._health <= 0:
            self.remove_character(Team, Battle)

    def __ult_remove_health(self, reduced_health, Team, Battle):
        self.character._health = reduced_health

    def basic(self, Team: list, Battle):
        attacking_character_char = Team.team[self._target]
        attacking_character = attacking_character_char._get_block()

        reduced_health = self.character._basic(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                               attacking_character.GetCrit_avoidance(), attacking_character.GetHealth(),
                                               attacking_character_char._buffs, attacking_character_char._debuffs,
                                               self._offense, self._buffs, self._debuffs)

        attacking_character_char._remove_health(reduced_health, Team, Battle)

    def special(self, Team: list, Battle):
        attacking_character_char = Team.team[self._target]
        attacking_character = attacking_character_char._get_block()

        special_data = self.character._special(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                               attacking_character.GetCrit_avoidance(), attacking_character.GetHealth(),
                                               attacking_character_char._buffs, attacking_character_char._debuffs,
                                               self._offense, self._buffs, self._debuffs, attacking_character.GetTenacity())

        attacking_character_char._remove_health(special_data[0], Team, Battle)
        attacking_character_char._buffs = special_data[1]
        attacking_character_char._debuffs = special_data[2]
        self._buffs = special_data[3]
        self._debuffs = special_data[4]
        self._offense = special_data[5]
        self._continuing_buffs = special_data[6]

    def ultimate(self, Team: list, Battle):
        attacking_character_char = Team.team

        for character in attacking_character_char:
            attacking_character = character._get_block()

            reduced_health = (self.character._ultimate(attacking_character.GetDefense(), attacking_character.GetEvasion(),
                                                   attacking_character.GetCrit_avoidance(),
                                                   attacking_character.GetHealth(),
                                                   character._buffs, character._debuffs,
                                                   self._offense, self._buffs, self._debuffs))

            character.__ult_remove_health(reduced_health, Team, Battle)

        for i in range(len(attacking_character_char)-1, -1, -1):
            attacking_character_char[i]._remove_health(attacking_character_char[i]._get_block()._health, Team, Battle)




    def passive(self, Team1, Team2):
        changes = self.character._passive(self._buffs, self._debuffs, self._offense, Team1, Team2, self._continuing_buffs)

        self._buffs = changes[0]
        self._debuffs = changes[1]
        self._offense = changes[2]




    def _display_character(self):
        return self.character.GetName()

    def _get_block(self):
        return self.character











