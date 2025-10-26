#from Character import Character
import sqlite3

class Cragger:
    def __init__(self):
        conn = sqlite3.connect("NEA Database.db")
        cursor = conn.cursor()
        cursor.execute('''SELECT * FROM General_character''')

        stats = cursor.fetchall()

        stats = stats[0]
        stats = stats[2:]

        self.health = stats[0]
        self.damage = stats[1]
        self.evasion = stats[2]
        self.ap = stats[3]
        self.defense = stats[4]
        self.crit_chance = stats[5]
        self.crit_damage = stats[6]
        self.accuracy = stats[7]
        self.crit_avoidance = stats[8]
        self.speed = stats[9]



if __name__ == '__main__':
    Char = Cragger()

