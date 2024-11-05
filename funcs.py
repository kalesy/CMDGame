import random as r
import json, os
class unit:
    def __init__(self, level = 1, hp = 100, attack = 5, defence = 5, equipments = [], skills = []):
        self.equipments = equipments
        self.skills = skills
        self.level = level
        self.hp = self.maxhp = hp
        self.damageTaken = 0
        self.attack = attack
        self.defence = defence
    def HP(self):
        return self.hp
    def IsDefeated(self):
        return self.hp < 0

    def buffSum(self):
        for s in self.skills:
            eval(s.formula)


    def TakeDamage(self, damage):
        if(damage < self.defence):
            self.hp -= 1
        else:
            self.hp -= damage - self.defence

class Character(unit): 
    def __init__(self):
        if(os.path.exists("save.json")):
            f = open("save.json", 'r')
            save = json.load(f)
            unit.__init__(self, save['level'], save['hp'], save['attack'], save['defence'], save['equipments'], save['skills'])
        else:
            unit.__init__(self)
        print(f'Initialization complete.\n==================================\nYou are a hero of {self.hp} Hp and {self.attack} Attack\n==================================')
        self.exp = 0
    def GainExp(self, unit):
        i = unit.maxhp / self.maxhp * 100 
        self.exp += i
        print('You gain %d exp of total %d requiring %d' % (i, self.exp, self.__levelRequire()))
        if(self.exp > self.__levelRequire()):
            self.__levelUp()
    def __levelUp(self):
        self.level += 1
        self.hp = self.maxhp + self.__levelUpRandom(1, 5)
        self.maxhp = self.hp
        self.attack = self.attack + self.__levelUpRandom(1, 3)
        print('Congratulations! Level up to %d of %d hp and %d attack'%(self.level, self.hp, self.attack))
    def __levelUpRandom(self, min, max):
        return r.randint(min, max)

    def __levelRequire(self):
        return self.level * 100 * 0.8

class EnemeyFactory:
    def __init__(self, EnemyCount):
        self.array = [unit(r.randint(1,5),r.randint(20,50), r.randint(2,7), 0) for x in range(0, EnemyCount)]
        self.currentEnemyIndex = -1
    def GetEnemy(self):
        l = len(self.array)
        if(l < 1):
            return None
        else:
            self.currentEnemyIndex = r.randint(0, len(self.array) - 1)
            return self.array[self.currentEnemyIndex]
    def EnemeyDefeat(self):
        self.array.pop(self.currentEnemyIndex)
    def EnemyCountLeft(self):
        return len(self.array)
