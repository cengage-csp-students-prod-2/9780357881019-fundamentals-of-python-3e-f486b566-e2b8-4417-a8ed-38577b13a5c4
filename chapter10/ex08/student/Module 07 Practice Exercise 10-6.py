"""
Author: Ashley Francis
Date written: 03/03/2025
Assignment: Module 07 Practice Exercise 10-6
"""

import random

class Player:
    def __init__(self):
        self.roll = None
        self.rollsCount = 0
        self.atStartup = True
        self.winner = False
        self.loser = False

    def rollDice(self):
        die1 = random.randint(1, 6)
        die2 = random.randint(1, 6)
        self.roll = f"{die1} + {die2} = {die1 + die2}"
        self.rollsCount += 1
        self.atStartup = False
        self.checkWinLose(die1 + die2)
        return (die1, die2)

    def checkWinLose(self, total):
        if self.atStartup:
            if total in (7, 11):
                self.winner = True
            elif total in (2, 3, 12):
                self.loser = True
        else:
            if total == 7:
                self.loser = True
            elif total == self.point:
                self.winner = True

    def getNumberOfRolls(self):
        return self.rollsCount

    def isWinner(self):
        return self.winner

    def isLoser(self):
        return self.loser

def playOneGame():
    player = Player()
    while not player.isWinner() and not player.isLoser():
        player.rollDice()
        print(player.roll)

def playManyGames(n):
    for _ in range(n):
        playOneGame()
        print("-----")
