import asyncio
import random as r
from funcs import *

async def userInputAsync():
    userInput = await asyncio.get_event_loop().run_in_executor(None, input, 'input')
    print(userInput)

loop = asyncio.get_event_loop()
loop.run_until_complete(userInputAsync())

p = Character()
es = EnemeyFactory(20)
while(True):
    if(p.IsDefeated()):
        print('Game over')
        break
    # get the enemy
    currentEnemey = es.GetEnemy()
    if(currentEnemey == None):
        print('Game over')
        break 
    print('You get an enemy, asshole! Enemy Hp = %d Atk = %d' % (currentEnemey.HP(), currentEnemey.attack))
    # engage
    while(True):
        c = input('What would you do? a. attack, e. Escape\n')
        match(c):
            case 'a':
                currentEnemey.TakeDamage(p.attack)
                print('You attack the enemy! Enemy Hp = %d' % (currentEnemey.HP()))
                if(currentEnemey.IsDefeated()):
                    print('You defeat the enemy! Your Hp = %d' %(p.HP()))
                    p.GainExp(currentEnemey)
                    es.EnemeyDefeat()
                    break
                p.TakeDamage(currentEnemey.attack)
                print('The enemy attack you! Your Hp = %d' %(p.HP()))
                if(p.IsDefeated()):
                    print('You are defeated!')
                    break
            case _:
                break
