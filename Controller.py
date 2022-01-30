"""
    CS5001 SPR
    Heekyung Kim
    Final Project: MasterMind

    This program creates a class that links data to gui. It controls and
    manipulates data from player statistics and receives input and sends
    output to gui.

    This program uses Model class imported from Model.py and View class imported
    from View.py.

    This program uses constants imported from constants.py file.
"""
import time
from Model import Model
from View import View
from constants import MAX_NUM_ROUNDS, MAX_NUM_GUESS


class Controller:
    def __init__(self):
        """
            Class: Controller
            Controller links data from Model class to gui from View class.
            It displays start screen, gets leaderboard data from Model and sends
            it to gui to display on screen, displays error message if there is
            an error while loading leaderboard data, resets number of guess to 0
            on Model when the player clicks the reset button and redraws the
            choice marbles and clears marbles of current round on status panel
            of screen, ends the program when the player clicks the quit button,
            draws marbles that was chosen by the player on status panel of screen
            and saves the chosen marble color on Model, receives calculated cows
            and bulls from model and sends calculated score pegs to draw on screen,
            displays win popup when the player guesses the secret code in 10 guess,
            and displays lose popup when the player fails to guess the secret code
            in 10 rounds.
        """

        # Initialize Model and View
        self.player_stat = Model()
        self.gui = View()

        # Display start screen
        self.gui.show_start_screen()

        # Create secret code
        self.secret_code = self.player_stat.create_secret_code()

    def display_leaderboard(self):
        """
            Function -- display_leaderboard
                Displays leaderboard based on data loaded from Model class.
        """

        # When the data file loaded is corrupt and raises error
        if self.player_stat.load_leaderboard() == -1:
            # Display popup about the error
            self.gui.show_popup("corrupt_file")

            # End program
            self.quit_program()

        else:
            # Send leaderboard data to display on screen
            self.gui.display_top_players(self.player_stat.leaderboard)

    def reset_guess(self):
        """
            Function -- reset_guess
                Resets number of guess to 0 on Model when the player clicks
                the reset button and redraws the choice marbles and clears
                marbles of current round on status panel of screen.
        """

        # Reset number of guess to 0
        self.player_stat.set_num_guess(0)

        # Clear guess and redraw choice marbles
        self.gui.clear_guess()
        self.gui.draw_choice_marbles()

    def quit_program(self):
        """
            Function -- quit_program
                Displays a popup that notifies player the program is quitting,
                 and ends the program when the player clicks quit button.
        """
        # Display quit message
        self.gui.show_popup("quit_msg")

        # End program after two seconds
        time.sleep(2)
        self.gui.board.screen.bye()

    def play_game(self, x: int, y: int):
        """
            Function -- play_game
                Plays the game 10 rounds until the user guess the secret code.
                For each round, player has to guess color for four positions.
                Guess of each round that was clicked on screen from user
                is saved to Model. At the end of each round, cows and bulls
                are calculated and displayed on score peg of the screen. User
                can click buttons and marbles on the screen, which prompts
                matching actions.
            Paramenters:
                x (int) -- x point clicked on screen
                y (int) -- y point clicked on screen
        """
        # Players given 10 rounds to guess
        if self.player_stat.rounds <= MAX_NUM_ROUNDS:

            # Player given 4 guess for each round
            if self.player_stat.num_guess < MAX_NUM_GUESS:
                clicked_marble = self.gui.check_button_clicked(x, y)

                # When player clicks reset button
                if clicked_marble == "reset":
                    self.reset_guess()

                # When player clicks quit button
                elif clicked_marble == "quit":
                    self.quit_program()

                # When player clicks submit button, do nothing
                elif clicked_marble == "submit":
                    pass

                # When player clicks a choice marble
                elif clicked_marble is not None:
                    # Draw the chosen marble to status panel
                    self.gui.draw_guess(self.player_stat.num_guess,
                                        clicked_marble)

                    # Add chosen marble to player guess
                    self.player_stat.update_player_guess(clicked_marble)

                    # Increment number of guess
                    self.player_stat.num_guess += 1

            # When player filled 4 guesses
            else:
                # Disable choice marbles
                self.gui.disable_choice_marble()

                # When player clicks reset button
                if self.gui.check_button_clicked(x, y) == "reset":
                    self.reset_guess()

                # When player clicks quit button
                elif self.gui.check_button_clicked(x, y) == "quit":
                    self.quit_program()

                # When player clicks submit button
                elif self.gui.check_button_clicked(x, y) == "submit":

                    # Calculate bulls and cows
                    bulls, cows = self.player_stat.count_bulls_and_cows(
                        self.secret_code, self.player_stat.player_guess)

                    # Update score pegs on player stat
                    self.player_stat.update_score(bulls, cows)

                    # Draw score pegs
                    self.gui.draw_score(self.player_stat.score_pegs)

                    # When player guessed the secret code
                    if bulls == 4:
                        # Disable reset button
                        self.gui.reset_button.visible = False

                        # Display win message
                        self.gui.show_popup("win_msg")

                        # Increment number of rounds
                        self.player_stat.rounds += 1

                        # Update leaderboard with current player's socre
                        self.player_stat.update_leaderboard()

                        # Save score of player
                        self.player_stat.save_leaderboard()

                    # Reset for next round when user did not guess code
                    else:
                        # Stamp user guess to status panel
                        self.gui.stamp_guess()

                        # Reset choice marbles in view
                        self.gui.draw_choice_marbles()

                        # Reset number of guess in model
                        self.player_stat.set_num_guess(0)

                        # Update pointer position in view
                        self.gui.pointer.y = self.gui.current_y_pos - 30
                        self.gui.pointer.draw_pointer()

                        # Update current y position in model
                        self.gui.current_y_pos -= 50

                        # Increment rounds in model
                        self.player_stat.rounds += 1

                        # Update rounds displayed in gui
                        self.gui.board.update_rounds_display(
                            self.player_stat.rounds + 1)

                        # When user played 10 rounds
                        if self.player_stat.rounds == MAX_NUM_ROUNDS:

                            # Disable choice marble clicks
                            self.gui.disable_choice_marble()

                            # Disable submit and reset button
                            self.gui.submit_button.visible = False
                            self.gui.reset_button.visible = False

                            # Display lose popup message
                            self.gui.show_popup("lose_msg")

                            # End program on quit button
                            if self.gui.check_button_clicked(x, y) == "quit":
                                self.quit_program()

    def run_program(self, x, y):
        """
            Function -- run_program
                Starts game when player clicks start button. It then setups
                the gameboard, and load the leaderboard data to display on
                screen. If there is an error in loading the leaderboard data
                because the file is corrupt, it displays an popup on the error
                on screen. If no error, the program proceeds to playing the game.
            Paramenters:
                x (int) -- x point clicked on screen
                y (int) -- y point clicked on screen
        """

        # When user clicks start button
        if self.gui.check_button_clicked(x, y) == "start":

            # Clear start screen
            self.gui.clear_start_screen()

            # Ask user for name and save to model
            self.player_stat.player = self.gui.ask_player_name()

            # Draw gameboard
            self.gui.setup_board()

            # When error loading leaderboard
            if self.player_stat.load_leaderboard() == -1:
                # Display error message and quit the program
                self.gui.show_popup("corrupt_file")
                self.quit_program()

            else:
                # Display loaded leaderboard data on screen
                self.gui.display_top_players(self.player_stat.leaderboard)

                # Display the name of player
                self.gui.display_name(self.player_stat.player)

                # Set the round to 1
                self.gui.board.update_rounds_display()

                # Play the game
                self.gui.board.screen.onclick(self.play_game)

