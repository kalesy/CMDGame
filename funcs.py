import random as r
class unit:
    def __init__(self, level, hp, attack, block):
        self.level = level
        self.hp = hp
        self.damageTaken = 0
        self.attack = attack
        self.block = block
    def MaxHp(self):
        return self.hp
    def HP(self):
        return self.hp - self.damageTaken
    def IsDefeated(self):
        return self.damageTaken >= self.hp
    def TakeDamage(self, damage):
        self.damageTaken += damage - self.block 

class Character(unit): 
    def __init__(self):
        unit.__init__(self, 0, 100, 5, 0)
        self.exp = 0
    def GainExp(self, unit):
        i = unit.MaxHp() / self.MaxHp() * 100 
        self.exp += i
        print('You gain %d exp of total %d' % (i, self.exp))
    def LevelUp(self):
        self.level += 1

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
