import random as r
from funcs import *
from const import DamageColor, End, Red, Blue, Green
from scene import prepare, battle, transaction


def main():
    p = Character()

    running = True
    prepareScene = prepare.Prepare()
    battleScene = battle.Battle()
    transactionScene = transaction.Transaction({"prepare":prepareScene, "battleScene":battleScene})

    while(running):
        transactionScene.run()


if __name__ == '__main__':
    main()
