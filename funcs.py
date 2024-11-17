from collections.abc import Sequence
import random as r
import json, os
from typing import Optional
from const import AttackColor, Green, Blue, HPColor, Red, End
class Unit:
    def __init__(self, level = 1, hp = 100, attack = 5, defence = 5, equipments = [], skills = []):
        self.equipments = equipments
        self.skills = skills
        self.level = level
        self.maxhp:int
        self.hp = self.maxhp = hp
        self.attack = attack
        self.defence = defence

    def showHP(self):
        if(self.hp > 0):
            return f"体力 {self.hp}/{self.maxhp}"
        else:
            return f"{r.choice(['死了', '臭了', '凉了', '埋了'])}"

    def IsDefeated(self) -> bool:
        return self.hp < 0

    def buffSum(self):
        # TODO: Create skill class
        for s in self.skills:
            eval(s.formula)


    def TakeDamage(self, _damage:int) -> str:
        if(_damage <= self.defence):
            self.hp -= 1
            return r.choice(['没吃饭啊!', '用力!', '啊你打了?'])
        else:
            damage = _damage - self.defence
            self.hp -= damage
            return str(damage) + '!'

class Character(Unit): 

    def __init__(self):
        if(os.path.exists("save.json")):
            f = open("save.json", 'r')
            save = json.load(f)
            super().__init__(save['level'], save['hp'], save['attack'], save['defence'], save['equipments'], save['skills'])
        else:
            super().__init__()
        print(f'肠胃通畅.\n==================================\n你现在{Green}体力 {self.hp}{End}, {Blue}攻击 {self.attack}{End}\n==================================')
        self.exp = 0

    def GainExp(self, unit:Unit):
        i = unit.maxhp / self.maxhp * 100 
        self.exp += i
        print('获得%d经验, 当前%d, 还需要%d' % (i, self.exp, self.__levelRequire() - self.exp))
        if(self.exp > self.__levelRequire()):
            self.__levelUp()

    def __levelUp(self):
        self.level += 1
        self.hp = self.maxhp + self.__levelUpRandom(1, 5)
        self.maxhp = self.hp
        self.attack = self.attack + self.__levelUpRandom(1, 3)
        print(f'升级辣! 等级{self.level}, {HPColor}体力 {self.hp}{End}, {AttackColor}攻击 {self.attack}{End}')

    def __levelUpRandom(self, min:int, max:int) -> int:
        return r.randint(min, max)

    def __levelRequire(self):
        return self.level * 100 * 0.8

class EnemeyFactory:
    def __init__(self, EnemyCount:int):
        self.array = [Unit(r.randint(1,5),r.randint(20,50), r.randint(2,7), 0) for _ in range(0, EnemyCount)]
        self.currentEnemyIndex = -1
    def GetEnemy(self) -> Unit|None:
        l = len(self.array)
        if(l < 1):
            return None
        else:
            self.currentEnemyIndex = r.randint(0, len(self.array) - 1)
            return self.array[self.currentEnemyIndex]
    def EnemeyDefeat(self):
        _ = self.array.pop(self.currentEnemyIndex)
    def EnemyCountLeft(self):
        return len(self.array)
