class Speed_Queue:
    def __init__(self, characters):
        self._chars = []
        self.__set_chars(characters)
        self.__set_speeds()

        self.__priority()


    def __set_chars(self, characters):
        for i in range(10):
            self._chars.append([characters[i], True])



    def __set_speeds(self):
        self._speeds = []
        for i in range(len(self._chars)):
            speed = [self._chars[i][0].character._speed, i]
            self._speeds.append(speed)


    def __priority(self):
        self._speeds.sort(reverse=True)

    def speed_turn(self):
        for i in range(len(self._chars)):
            self._speeds[i][0] += self._chars[self._speeds[i][1]][0].character.GetSpeed()



        self.__priority()

        self.__take_turn()


    def remove_character(self, character):

        for i in range(len(self._chars)):
            if self._chars[i][1] == True:
                if self._chars[i][0].character.GetHealth() == 0 and self._chars[i][0].character == character.character:
                    self._chars[i][1] = False










    def __take_turn(self):
        if self._speeds[0][0] >= 1000:
            index = self._speeds[0][1]
            if self._chars[index][1] == True:
                self.__Character_for_turn = self._chars[index][0]
                self._speeds[0][0] = 0
                self.__priority()
            else:
                self._speeds[0][0] = 0
                self.__priority()

        else:
            self.speed_turn()







    def GetQueue(self):
        return self._chars

    def Get_character_for_turn(self):
        return self.__Character_for_turn

