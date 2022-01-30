"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    This program creates a class that simulates GUI for the game board.

    This program uses Board class from Board.py, Marble class from Marble.py,
    Button class from Button.py, and PopUp class from PopUp class, Pointer class
    from Pointer.py, and constants from constants.py.
"""
import time
from gui.Board import Board
from gui.Marble import Marble
from gui.Button import Button
from gui.Popup import PopUp
from gui.Pointer import Pointer
from constants import *


class View:
    def __init__(self):
        """
            Class: View
            View is used to display data on screen and receive input from player
            via screen. It prompts popup that asks player to input name, displays
            top players on leaderboard, draws choice marbles on guess panel for
            players to input, draws buttons on screen, draws chosen marble on
            guess panel, draws score key pegs, checks if the button was clicked,
            updates display of rounds on screen, displays start screen, clears
            start screen, setups the gameboard, stamps guess, clear guess,
            disables clicking on choice marbles, shows popups, and displays
            player name on screen.
        """
        self.board = Board()
        self.pointer = Pointer()

        self.current_y_pos = 250

        # Register image path for buttons
        self.board.register_image(LOGO_IMG_PATH)
        self.board.register_image(START_BUTTON_PATH)
        self.board.register_image(SUBMIT_BUTTON_PATH)
        self.board.register_image(RESET_BUTTON_PATH)
        self.board.register_image(QUIT_BUTTON_PATH)

        # Register image path for popup
        self.board.register_image(LEADERBOARD_ERROR_MSG_PATH)
        self.board.register_image(WIN_POPUP_MSG_PATH)
        self.board.register_image(LOSE_POPUP_MSG_PATH)
        self.board.register_image(QUIT_POPUP_MSG_PATH)

        # Instantiate choice marbles
        self.red_marble = Marble(Point(FIRST_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                 CODE_RADIUS, "red")
        self.blue_marble = Marble(Point(SECOND_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                  CODE_RADIUS, "blue")
        self.yellow_marble = Marble(Point(THIRD_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                    CODE_RADIUS, "yellow")
        self.green_marble = Marble(Point(FOURTH_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                   CODE_RADIUS, "green")
        self.black_marble = Marble(Point(FIFTH_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                   CODE_RADIUS, "black")
        self.purple_marble = Marble(Point(SIXTH_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                    CODE_RADIUS, "purple")

        # Instantiate marbles chosen from user
        self.position_one = Marble(Point(FIRST_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                   CODE_RADIUS)
        self.position_two = Marble(Point(SECOND_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                   CODE_RADIUS)
        self.position_three = Marble(Point(THIRD_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                     CODE_RADIUS)
        self.position_four = Marble(Point(FOURTH_MARBLE_POS_X, FIRST_ROW_POS_Y),
                                    CODE_RADIUS)

        # Instantiate button
        self.logo = Button(LOGO_IMG_POS, LOGO_IMG_PATH)
        self.start_button = Button(START_BUTTON_POS, START_BUTTON_PATH, size=25)
        self.submit_button = Button(SUBMIT_BUTTON_POS, SUBMIT_BUTTON_PATH)
        self.reset_button = Button(RESET_BUTTON_POS, RESET_BUTTON_PATH)
        self.quit_button = Button(QUIT_BUTTON_POS, QUIT_BUTTON_PATH, size=20)

        # Instantiate score pegs
        self.score_one = Marble(Point(FIRST_SCORE_POS_X,
                                      self.current_y_pos + 20), SCORING_RADIUS)
        self.score_two = Marble(Point(SECOND_SCORE_POS_X,
                                      self.current_y_pos + 20), SCORING_RADIUS)
        self.score_three = Marble(Point(FIRST_SCORE_POS_X, self.current_y_pos),
                                  SCORING_RADIUS)
        self.score_four = Marble(Point(SECOND_SCORE_POS_X,
                                       self.current_y_pos), SCORING_RADIUS)

    def ask_player_name(self):
        """
            Function -- ask_player_name
                Asks player to input name via popup prompt.
            Returns name user input.
        """
        return self.board.ask_name()

    def display_top_players(self, list_of_top_players: list):
        """
            Function -- display_top_players
                Displays top players on leaderboard on screen
            Paramenters:
                list_of_top_players (list) -- list loaded from leaderboard.txt
        """
        y_pos = 270

        # Display top player and their score on screen
        for player, score in list_of_top_players:
            text = str(score) + "  \t" + player
            self.board.write_text(text, Point(200, y_pos))

            y_pos -= 50

    def draw_choice_marbles(self):
        """
            Function -- draw_choice_marbles
                Draws choice marbles on guess panel of screen.
        """
        self.red_marble.draw()
        self.blue_marble.draw()
        self.yellow_marble.draw()
        self.green_marble.draw()
        self.black_marble.draw()
        self.purple_marble.draw()

    def draw_buttons(self):
        """
            Function -- draw_buttons
                Draws submit, reset, quit button on screen.
        """
        self.submit_button.draw()
        self.reset_button.draw()
        self.quit_button.draw()

    def draw_guess(self, position: int, color: str):
        """
            Function -- draw_guess
               Draws marble of given color in the given position on status
                    panel.
            Parameters:
                position (int) -- position of marble to guess
                color (str) -- color of clicked marble
        """

        if position == 0:
            self.position_one.position = Point(FIRST_MARBLE_POS_X,
                                               self.current_y_pos)
            self.position_one.set_color(color)
            self.position_one.draw()

        elif position == 1:
            self.position_two.position = Point(SECOND_MARBLE_POS_X,
                                               self.current_y_pos)
            self.position_two.set_color(color)
            self.position_two.draw()

        elif position == 2:
            self.position_three.position = Point(THIRD_MARBLE_POS_X,
                                                 self.current_y_pos)
            self.position_three.set_color(color)
            self.position_three.draw()

        elif position == 3:
            self.position_four.position = Point(FOURTH_MARBLE_POS_X,
                                                self.current_y_pos)
            self.position_four.set_color(color)
            self.position_four.draw()

    def draw_score(self, bulls_cows_output: list):
        """
            Function -- draw_score
               Draws score key pegs of a round.
            Parameters:
                bulls_cows_output (list) -- list of calculated bulls and cows
        """
        # Draw score peg one
        self.score_one.set_position(Point(FIRST_SCORE_POS_X,
                                          self.current_y_pos + 20))
        self.score_one.set_color(bulls_cows_output[0])
        self.score_one.draw()

        # Draw score peg two
        self.score_two.set_position(Point(SECOND_SCORE_POS_X,
                                          self.current_y_pos + 20))
        self.score_two.set_color(bulls_cows_output[1])
        self.score_two.draw()

        # Draw score peg three
        self.score_three.set_position(Point(FIRST_SCORE_POS_X,
                                            self.current_y_pos))
        self.score_three.set_color(bulls_cows_output[2])
        self.score_three.draw()

        # Draw score peg four
        self.score_four.set_position(Point(SECOND_SCORE_POS_X,
                                           self.current_y_pos))
        self.score_four.set_color(bulls_cows_output[3])
        self.score_four.draw()

    def check_button_clicked(self, x: int, y: int) -> str:
        """
            Function -- check_button_clicked
                Checks if the given position is inside a marble or
                 inside a button.

            Parameters:
                x (int) -- x point on screen
                y (int) -- y point on screen

            Returns the color of the clicked marble or the action of the clicked
               button. If point is not inside a marble or a button returns None.
        """
        if self.red_marble.clicked_in_region(x, y):
            self.red_marble.draw_empty()
            return "red"

        elif self.blue_marble.clicked_in_region(x, y):
            self.blue_marble.draw_empty()
            return "blue"

        elif self.yellow_marble.clicked_in_region(x, y):
            self.yellow_marble.draw_empty()
            return 'yellow'

        elif self.green_marble.clicked_in_region(x, y):
            self.green_marble.draw_empty()
            return "green"

        elif self.black_marble.clicked_in_region(x, y):
            self.black_marble.draw_empty()
            return "black"

        elif self.purple_marble.clicked_in_region(x, y):
            self.purple_marble.draw_empty()
            return "purple"

        elif self.submit_button.clicked_in_region(x, y):
            return "submit"

        elif self.reset_button.clicked_in_region(x, y):
            return "reset"

        elif self.quit_button.clicked_in_region(x, y):
            return "quit"

        elif self.start_button.clicked_in_region(x, y):
            return "start"

        else:
            return None

    def update_rounds_display(self, rounds=1):
        """
            Function -- update_rounds_display
                Display current round of the player on screen.
            Parameters:
                rounds (int) -- round of game. Default is one.
        """
        self.board.rounds_pen.up()
        self.board.rounds_pen.setpos(ROUNDS_DISPLAY_POS)
        self.board.rounds_pen.down()
        self.board.rounds_pen.clear()
        self.board.rounds_pen.write(str(rounds), font=(FONT, 25, "bold"))

    def show_start_screen(self):
        """
            Function -- show_start_screen
                Display start screen that has the title of the game and a
                    start button. When the start button is clicked, the game
                    starts.
        """
        self.logo.draw()
        self.start_button.draw()

    def clear_start_screen(self):
        """
            Function -- clear_start_screen
                Clears start screen.
        """
        self.logo.erase()
        self.start_button.erase()

    def setup_board(self):
        """
             Function -- setup_board
                 Draws the elements of the gameboard such as status panel,
                    leaderboard, player name, play area, status marbles, choice
                    marbles, buttons and pointer on screen.
         """
        # Draw status panel
        self.board.draw_box("black", STATUS_BOX_POS, width=600, height=580)

        # Draw leader board
        self.board.draw_box("blue", LEADERBOARD_POS, width=300, height=580)

        # Write title for leader board
        self.board.write_text("Top 5 Players", LEADERBOARD_TITLE_POS)

        # Write Player name
        self.board.write_text("Player:\t", PLAYER_DISPLAY_POS)

        # Write Rounds played
        self.board.write_text("Round:\t", ROUNDS_TEXT_POS)

        # Draw play area
        self.board.draw_box("black", PLAYAREA_BOX_POS, width=950, height=100)

        # Draw status marbles
        self.board.draw_marble_setup(STATUS_MARBLE_POS)

        # Draw choice marbles
        self.draw_choice_marbles()

        # Draw buttons
        self.draw_buttons()

        # Draw pointer
        self.pointer.draw_pointer()

    def stamp_guess(self):
        """
            Function -- stamp_guess
                Stamps the final guess on the status panel.
        """
        self.position_one.stamp()
        self.position_two.stamp()
        self.position_three.stamp()
        self.position_four.stamp()

    def clear_guess(self):
        """
            Function -- clear_guess
                Clears the guess drawn on the status panel of current round.
        """
        self.position_one.draw_empty()
        self.position_two.draw_empty()
        self.position_three.draw_empty()
        self.position_four.draw_empty()

    def disable_choice_marble(self):
        """
            Function -- disable_choice_marble
                Disables choice marbles from being clicked.
        """
        self.red_marble.visible = False
        self.blue_marble.visible = False
        self.green_marble.visible = False
        self.yellow_marble.visible = False
        self.black_marble.visible = False
        self.purple_marble.visible = False

    def show_popup(self, msg: str):
        """
            Function -- show_popup
                Displays given message on popup.
            Parameters:
                msg (str) -- message to display on popup.
        """

        # Show corrupt file error
        if msg == "corrupt_file":
            popup = PopUp(LEADERBOARD_ERROR_MSG_PATH)
            popup.show()
            time.sleep(2)
            popup.close()

        # Show win message
        elif msg == "win_msg":
            PopUp(WIN_POPUP_MSG_PATH).show()

        # Show lose message
        elif msg == "lose_msg":
            PopUp(LOSE_POPUP_MSG_PATH).show()

        # Show quit message
        elif msg == "quit_msg":
            PopUp(QUIT_POPUP_MSG_PATH).show()

    def display_name(self, name: str):
        """
            Function -- display_name
                Displays name of player on screen
            Parameters:
                name (str) -- name of player
        """
        self.board.write_text(name, PLAYER_NAME_DISPLAY_POS)
