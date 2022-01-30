"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    The code references Marble.py provided as class material.
    This program creates a class that simulates Marbles for the game board.
"""
import turtle


class Marble:
    """
        Class: Marble
        Marble is used to create marbles on the gameboard. It sets color of
        marble, retrieves color of the marble, sets position of marbles,
        draws the marble, draws empty marbles without color, erases marbles from
        the screen, stamps the marble on the screen, and checks if the marble
        was clicked from screen.
    """
    def __init__(self, position, size, color="white"):
        self.color = color
        self.size = size
        self.position = position
        self.visible = False
        self.is_empty = True
        self.pen = self.new_pen()
        self.pen.hideturtle()
        self.pen.speed(0)

    def new_pen(self):
        """
            Function -- new_pen
                Initializes pen to draw on marbles on screen.
            Returns turtle object.
        """
        return turtle.Turtle()

    def set_color(self, color):
        """
            Function -- set_color
                Sets color of marble to draw
        """
        self.color = color
        self.is_empty = False

    def get_color(self):
        """
            Function -- get_color
                Return color of marble instance.
        """
        return self.color

    def set_position(self, position):
        """
            Function -- set_position
                 Sets position to draw marble
        """
        self.position = position

    def draw(self):
        """
            Function -- draw
                Draws marble on screen.
        """
        self.pen.hideturtle()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.fillcolor(self.color)
        self.pen.begin_fill()
        self.pen.circle(self.size)
        self.pen.end_fill()

        self.visible = True
        self.is_empty = False

    def draw_empty(self):
        """
            Function -- draw_empty
                Draws empty marbles with no fills.
        """
        self.erase()
        self.pen.up()
        self.pen.goto(self.position.x, self.position.y)
        self.pen.down()
        self.pen.circle(self.size)

        self.is_empty = True

    def erase(self):
        """
            Function -- erase
                Erases marble from screen.
        """
        self.visible = False
        self.pen.clear()

    def clicked_in_region(self, x: int, y: int) -> bool:
        """
            Function -- clicked_in_region
                Checks if the given position is inside the marble.
            Paramenters:
                x (int) -- position x
                y (int) -- position y
            Returns a boolean. True if the position is in the region and button
                is visible on screen or False if the position is out of region.
        """

        if self.visible \
                and abs(x - self.position.x) <= self.size * 2 \
                and abs(y - self.position.y) <= self.size * 2:

            return True

        return False

    def stamp(self):
        """
            Function -- stamp
                Stamps marbles on screen.
        """
        Marble(self.position, self.size, self.color).draw()
