from funcs import Character, EnemeyFactory
from const import *
class Battle:
    def __init__(self) -> None:
        self.battling = True

    def set(self, p:Character, es:EnemeyFactory):
        self.p = p
        self.es = es

    def run(self):
        while(self.battling):
            if(self.p.IsDefeated()):
                print(f'{Red}吔屎啦你{End}')
                break
            # get the enemy
            currentEnemey = es.GetEnemy()
            if(currentEnemey == None):
                print('吔屎啦你')
                break 
            print(f'遇到了一个敌人! {Green}HP {currentEnemey.showHP()}{End} {Red}Atk {currentEnemey.attack}{End}')
            # engage
            c = input(f'要干嘛? {Blue}攻击(回车){End}, {Red}快溜(Q){End}\n')
            match(c.strip().lower()):
                case 'a'|"":
                    print(f"攻击! {DamageColor}{currentEnemey.TakeDamage(self.p.attack)}{End}, 敌人{HPColor}{currentEnemey.showHP()}{End}")
                    if(currentEnemey.IsDefeated()):
                        print(f'胜利! 你的{HPColor}{self.p.showHP()}{End}')
                        self.p.GainExp(currentEnemey)
                        self.es.EnemeyDefeat()
                        break
                    print(f'敌人来干你了! {DamageColor}{self.p.TakeDamage(currentEnemey.attack)}{End}, 你的{HPColor}{self.p.showHP()}{End}')
                    if(self.p.IsDefeated()):
                        print('你凉了')
                        break
                case 'q':
                    print('溜了')
                case 'e':
                    print('不玩了, 退钱!')
                    battling = False
                case _:
                    print(f'没有{c}这个指令!')
