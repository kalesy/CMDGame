import random as r
class unit:
    def __init__(self, level, hp, attack, block):
        self.level = level
        self.hp = self.maxhp = hp
        self.damageTaken = 0
        self.attack = attack
        self.block = block
    def HP(self):
        return self.hp
    def IsDefeated(self):
        return self.hp < 0
    def TakeDamage(self, damage):
        self.hp -= damage - self.block 

class Character(unit): 
    def __init__(self):
        unit.__init__(self, 1, 100, 5, 0)
        print('Initialization complete, You are a hero of %d Hp and %d Attack'%(self.hp, self.attack))
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
