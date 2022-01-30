"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    The code references Marble.py provided as class material.
    This program creates a class that simulates button for the game board.
"""
import turtle


class Button:
    """
        Class: Button
        Button is used to create buttons such as submit and quit button on
        gameboard. It initializes the turtle to create buttons, draws buttons,
        erases buttons, and checks if the button was clicked.
    """
    def __init__(self, position: object, img_path: str, size=18):
        self.position = position
        self.img_path = img_path
        self.size = size
        self.visible = True
        self.button = self.initialize_button()
        self.button.hideturtle()
        self.button.speed("fastest")

    def initialize_button(self):
        """
            Function -- initialize_button
                Initializes button to display on gameboard.
            Returns turtle object.
        """
        return turtle.Turtle(shape=self.img_path)

    def draw(self):
        """
            Function -- draw
                Draws button on gameboard.
        """
        self.button.penup()
        self.visible = True
        self.button.setpos(self.position.x, self.position.y)
        self.button.showturtle()

    def erase(self):
        """
            Function -- erase
                Erases button from gameboard.
        """
        self.visible = False
        self.button.hideturtle()
        self.button.clear()

    def clicked_in_region(self, x: int, y: int) -> bool:
        """
            Function -- clicked_in_region
                Checks if the given position is inside the button.
            Paramenters:
                x (int) -- position x
                y (int) -- position y
            Returns a boolean. True if the position is in the region and button
                is visible on screen or False if the position is out of region.
        """
        if abs(x - self.position.x) <= self.size * 2 \
                and abs(y - self.position.y) <= self.size * 2 \
                and self.visible:
            return True

        return False
