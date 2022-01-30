"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This file contains all the constants for the program.
"""
from gui.Point import Point

SCREEN_WIDTH, SCREEN_HEIGHT = 1000, 800
FONT = "Courier"

CODE_RADIUS = 18
SCORING_RADIUS = 6

MAX_NUM_ROUNDS = 10
MAX_NUM_GUESS = 4
COLORS = ["red", "blue", "green", "yellow", "purple", "black"]

LEADERBOARD_FILENAME = "leaderboard.txt"

LOGO_IMG_PATH = "img/logo.gif"
START_BUTTON_PATH = "img/start.gif"
SUBMIT_BUTTON_PATH = "img/checkbutton.gif"
RESET_BUTTON_PATH = "img/reset.gif"
QUIT_BUTTON_PATH = "img/quit.gif"

LEADERBOARD_ERROR_MSG_PATH = "img/leaderboard_error.gif"
WIN_POPUP_MSG_PATH = "img/winner.gif"
LOSE_POPUP_MSG_PATH = "img/Lose.gif"
QUIT_POPUP_MSG_PATH = "img/quitmsg.gif"

FIRST_MARBLE_POS_X = -350
SECOND_MARBLE_POS_X = -300
THIRD_MARBLE_POS_X = -250
FOURTH_MARBLE_POS_X = -200
FIFTH_MARBLE_POS_X = -150
SIXTH_MARBLE_POS_X = -100

FIRST_SCORE_POS_X = -80
SECOND_SCORE_POS_X = -60
ROUNDS_DISPLAY_POS = -100, 335

FIRST_ROW_POS_Y = -325

LOGO_IMG_POS = Point(-10, 50)
START_BUTTON_POS = Point(0, -50)
STATUS_MARBLE_POS = Point(-350, 250)
SUBMIT_BUTTON_POS = Point(0, -310)
RESET_BUTTON_POS = Point(80, -310)
QUIT_BUTTON_POS = Point(300, -310)
POPUP_POS = Point(20, 50)

STATUS_BOX_POS = Point(-490, -250)
LEADERBOARD_POS = Point(155, -250)
PLAYAREA_BOX_POS = Point(-490, -360)

LEADERBOARD_TITLE_POS = Point(210, 335)
PLAYER_DISPLAY_POS = Point(-475, 335)
PLAYER_NAME_DISPLAY_POS = Point(-350, 335)
TOP_SCORE_DISPLAY_POS = Point(-475, 335)

ROUNDS_TEXT_POS = Point(-200, 335)
ROUNDS_DISPLAY_POS = Point(-90, 335)

POINTER_POS = Point(-420, 270)

