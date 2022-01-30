"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This program creates a class that returns points on screen.
   This code was provided as starter code in class.
"""


class Point:
    def __init__(self, x, y) -> object:
        self.x = x
        self.y = y

    def delta_x(self, other):
        return abs(self.x - other.x)

    def delta_y(self, other):
        return abs(self.y - other.y)
