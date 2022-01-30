"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    This program creates a class that simulates Game board for gui.
    This program imports constants from constants.py file.
"""
import turtle
from constants import *


class Board:
    """
        Class: Board
        Board creates elements of the gameboard. It initializes the gui screen,
        it registers image paths for buttons and popups, creates pen to draw
        elements of the gameboard, and creates popup for user to input name via
        screen, draws box for panels of the gameboard, writes texts such as titles
        on the gameboard, updates rounds played on the screen, draws circles,
        draw marbles, draw score_pegs, and draw chosen marbles for each round.
    """
    def __init__(self):
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        self.screen = self.initialize_screen()
        self.screen.title("CS5001 MasterMind")

        # Create pens to draw elements of gameboard
        self.box_pen = self.new_pen()
        self.text_pen = self.new_pen()
        self.pointer_pen = self.new_pen()
        self.rounds_pen = self.new_pen()

    def initialize_screen(self) -> object:
        """
            Function -- initialize_screen
                Initializes gui screen to display gameboard.
            Returns turtle screen object.
        """
        screen = turtle.Screen()
        screen.setup(self.width, self.height)
        return screen

    def register_image(self, img_path: str):
        """
            Function -- register_image
                Registers image path to screen.
            Parameters:
                img_path (str) -- image directory
        """
        self.screen.register_shape(img_path)

    def new_pen(self) -> object:
        """
            Function -- new_pen
                Initializes turtle pen.
            Returns a turtle.
        """
        pen = turtle.Turtle()
        pen.hideturtle()
        pen.speed("fastest")

        return pen

    def ask_name(self) -> str:
        """
            Function -- ask_name
                Initializes a popup that asks user to input name via screen.
            Returns a name of player
        """
        name = self.screen.textinput("CS5001 MasterMind", "Your Name:")
        return name

    def draw_box(self, pen_color: str, position: object, width: int, height: int):
        """
            Function -- draw_box
                Draws outline of parts of the gameboard such as guess panel
                  and leaderboard.
            Parameters:
                pen_color (str) -- color of line of box
                position (object) -- Points to start drawing box
                width (int) -- width of box
                height (int) -- height of box
        """
        # Set pen size and color
        self.box_pen.pensize(6)
        self.box_pen.color(pen_color)

        # Move turtle to the position to start drawing box
        self.box_pen.up()
        self.box_pen.setpos(position.x, position.y)

        # Draw box
        self.box_pen.down()
        self.box_pen.forward(width)
        self.box_pen.left(90)
        self.box_pen.forward(height)
        self.box_pen.left(90)
        self.box_pen.forward(width)
        self.box_pen.left(90)
        self.box_pen.forward(height)
        self.box_pen.left(90)

    def write_text(self, text: str, position: object):
        """
             Function -- write_text
                 Writes text such as title on the gameboard screen.
             Parameters:
                 text (str) -- color of line of box
                 position (object) -- Points to start drawing box

         """
        self.text_pen.up()
        self.text_pen.setpos(position.x, position.y)
        self.text_pen.down()
        self.text_pen.write(text, font=(FONT, 25, "bold"))

    def update_rounds_display(self, rounds=1):
        """
             Function -- update_rounds_display
                 Updates number of rounds on screen as rounds increment in game.
             Parameters:
                 rounds (int) -- number of rounds to update. Default value is 1.
         """
        # Update rounds up to 10
        if rounds < 11:
            self.rounds_pen.up()
            self.rounds_pen.setpos(ROUNDS_DISPLAY_POS.x, ROUNDS_DISPLAY_POS.y)
            self.rounds_pen.down()
            self.rounds_pen.clear()
            self.rounds_pen.write(str(rounds), font=(FONT, 25, "bold"))

    def draw_circle(self, position: object, radius: int):
        """
             Function -- draw_circle
                 Draws circle of given radius at given position.
             Parameters:
                 position (object) -- number of rounds to update.
                 radius (int) -- radius of circle to draw
         """
        self.box_pen.pensize(1)
        self.box_pen.up()
        self.box_pen.goto(position.x, position.y)
        self.box_pen.down()
        self.box_pen.circle(radius)

    def draw_marbles(self, position: object, radius: int, width: int, repeat: int):
        """
             Function -- draw_marbles
                 Draws given radius of marble n times, starting at given position,
                    spaced given width apart.
             Parameters:
                 position (object) -- position to draw marble
                 radius (int) -- radius of marble to draw
                 width (int) -- space between marbles
                 repeat (int) -- number of times to repeat drawing marbles
         """
        x_pos = position.x

        for i in range(repeat):
            self.draw_circle(Point(x_pos, position.y), radius)
            x_pos += width

    def draw_score_pegs(self, position: object):
        """
             Function -- draw_score_pegs
                 Draws outline of score pegs.
             Parameters:
                 position (object) -- position to start drawing pegs
         """
        # Draw first row of score pegs
        self.draw_marbles(Point(position.x + 270, position.y + 20),
                          SCORING_RADIUS, width=20, repeat=2)

        # Draw second row of score pegs
        self.draw_marbles(Point(position.x + 270, position.y),
                          SCORING_RADIUS, width=20, repeat=2)

    def draw_marble_setup(self, position: object):
        """
              Function -- draw_marble_setup
                  Draws outline of guess marbles and score pegs for status panel
              Parameters:
                  position (object) -- position to start drawing pegs
        """
        row = 0

        # Draw 10 rows of status marbles
        while row < MAX_NUM_ROUNDS:

            # Draw outline of guess marbles from user
            self.draw_marbles(position, CODE_RADIUS, width=50, repeat=4)

            # Draw outline of score pegs
            self.draw_score_pegs(position)

            # Move down to next row
            position.y -= 50
            row += 1



