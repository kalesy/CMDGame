import random as r
from funcs import *
from const import DamageColor, End, Red, Blue, Green
from scene import prepare, battle, transaction


def main():
    p = Character()

    running = True
    currentScene = None
    prepareScene = prepare.Prepare()
    battleScene = battle.Battle()
    transactionScene = transaction.Transaction([])

    while(running):


if __name__ == '__main__':
    main()
