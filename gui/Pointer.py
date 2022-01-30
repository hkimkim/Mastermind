"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    This program creates a class that simulates pointer for the game board.
    This program uses constants imported from constants.py file.
"""
import turtle
from constants import POINTER_POS


class Pointer:
    """
        Class: Pointer
        Pointer is used to create pointer on screen to indicate which row
        the player is on the status panel. It can draw pointer on the screen.
    """
    def __init__(self):
        self.pen = turtle.Turtle()
        self.pen.hideturtle()
        self.pen.speed("fastest")
        self.pen.color("red")
        self.pen.shapesize(2)
        self.x = POINTER_POS.x
        self.y = POINTER_POS.y

    def draw_pointer(self):
        """
            Function -- draw_pointer
                Draws pointer that indicates row on status panel.
        """
        # Move pointer up to -255 on y of screen
        if self.y > -225:
            self.pen.penup()
            self.pen.setpos(self.x, self.y)
            self.pen.down()
            self.pen.showturtle()

