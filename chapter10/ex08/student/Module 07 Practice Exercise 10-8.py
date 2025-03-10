"""
Author: Ashley Francis
Date written: 03/03/2025
Assignment: Module 07 Practice Exercise 10-8
"""

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.faceup = False

    def turn(self):
        self.faceup = not self.faceup
