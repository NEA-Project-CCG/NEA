class Speed_Queue:
    def __init__(self, characters):
        self.__chars = characters
        self.__set_speeds()
        self.__priority()


    def __set_speeds(self):
        self.__speeds = []
        for i in range(10):
            speed = [self.__chars[i].character._speed, i]
            self.__speeds.append(speed)


    def __priority(self):
        self.__speeds.sort(reverse=True)

    def speed_turn(self):
        for i in range(10):
            self.__speeds[i][0] += + self.__chars[self.__speeds[i][1]].character.GetSpeed()



        self.__priority()

        self.__take_turn()







    def __take_turn(self):
        if self.__speeds[0][0] >= 1000:
            index = self.__speeds[0][1]
            self.__Character_for_turn = self.__chars[index]
            self.__speeds[index][0] = 0
            print("working")
        else:
            self.speed_turn()







    def GetQueue(self):
        return self.__chars

    def Get_character_for_turn(self):
        return self.__Character_for_turn

