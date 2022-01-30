"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This program is the driver to run the game.
   This program imports Controller class from Controller.py
"""
import turtle
from Controller import Controller


def count_bulls_and_cows(secret_code, guess):
    play = Controller()
    return play.player_stat.count_bulls_and_cows(secret_code, guess)


def main():
    play = Controller()
    print(play.secret_code)
    play.gui.show_start_screen()
    play.gui.board.screen.onclick(play.run_program)
    turtle.done()


if __name__ == '__main__':
    main()
