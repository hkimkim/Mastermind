"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This program creates a class that simulates PopUp on GUI.
   This program uses constants from constants.py file.
"""
import turtle
from constants import POPUP_POS


class PopUp:
    """
        Class: PopUp
        PopUp is used to create popups on screen. It initializes the turtle
        to create popups, shows popup on screen, closes popup on screen.
    """
    def __init__(self, img_path):
        self.position = POPUP_POS
        self.img_path = img_path
        self.popup = self.initialize_popup()
        self.popup.hideturtle()
        self.popup.speed("fastest")

    def initialize_popup(self):
        """
            Function -- initialize_popup
                Initializes popup to display on screen.
            Returns turtle object.
        """
        return turtle.Turtle(shape=self.img_path)

    def show(self):
        """
            Function -- show
                Shows popup on screen.
        """
        self.popup.penup()
        self.popup.setpos(self.position.x, self.position.y)
        self.popup.showturtle()

    def close(self):
        """
            Function -- close
                Hides popup on screen.
        """
        self.popup.hideturtle()



