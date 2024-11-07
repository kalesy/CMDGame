import random as r
from funcs import *
from const import DamageColor, End, Red, Blue, Green

p = Character()
es = EnemeyFactory(20)

running = True
battling = True

while(running):
    if(p.IsDefeated()):
        print(f'{Red}吔屎啦你{End}')
        break
    # get the enemy
    currentEnemey = es.GetEnemy()
    if(currentEnemey == None):
        print('吔屎啦你')
        break 
    print(f'遇到了一个敌人! {Green}HP {currentEnemey.showHP()}{End} {Red}Atk {currentEnemey.attack}{End}')
    # engage
    while(battling):
        c = input(f'要干嘛? {Blue}攻击(回车){End}, {Red}快溜(Q){End}\n')
        match(c.strip().lower()):
            case 'a'|"":
                print(f"攻击! {DamageColor}{currentEnemey.TakeDamage(p.attack)}{End}, 敌人{HPColor}{currentEnemey.showHP()}{End}")
                if(currentEnemey.IsDefeated()):
                    print(f'胜利! 你的{HPColor}{p.showHP()}{End}')
                    p.GainExp(currentEnemey)
                    es.EnemeyDefeat()
                    break
                print(f'敌人来干你了! {DamageColor}{p.TakeDamage(currentEnemey.attack)}{End}, 你的{HPColor}{p.showHP()}{End}')
                if(p.IsDefeated()):
                    print('你凉了')
                    break
            case 'q':
                print('溜了')
            case 'e':
                print('不玩了, 退钱!')
                running = False
                battling = False
                
            case _:
                print(f'没有{c}这个指令!')
