"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This program creates a class that manages player statistics for the game.
"""
import random
from constants import LEADERBOARD_FILENAME, COLORS


class Model:
    """
        Class: Model
        Model is used to save player statistics while playing game. It keeps
        count of rounds played by user, number of guess player used for
        each round, player's name, top player scores, player's guess final guess
        for each round, and score pegs for each round. It can set player name,
        set number of guess, set rounds played, update player guess, load top scores
        from previous game from leaderboard.txt file, sort scores from best
        to worse (best being the smallest), insert current player's score to
        previous game score, save the updated score list to leaderboard.txt,
        create leaderboard.txt file if file does not exist, calculate bulls and cows
        for each round of guess, update score pegs based on the calculated bulls
        and cows, and create secret code to guess for the game.

    """
    def __init__(self):
        self.rounds = 0
        self.num_guess = 0
        self.player = ""
        self.leaderboard = self.load_leaderboard()
        self.player_guess = ["white"] * 4
        self.score_pegs = []

    def set_player(self, name: str):
        """
            Function -- set_player
                Stores player name to self.player attribute.
            Paramenter:
                name (str) -- name of player
        """
        self.player = name

    def set_num_guess(self, num_guess: int):
        """
            Function -- set_num_guess
                Stores number of guess to self.num_guess attribute.
            Paramenter:
                num_guess (int) -- number of guess user guessed for each round
        """
        self.num_guess = num_guess

    def set_rounds(self, rounds: int):
        """
            Function -- set_rounds
                Stores number of rounds to self.rounds attribute.
            Paramenter:
                rounds (int) -- number of rounds user played.
        """
        self.rounds = rounds

    def create_secret_code(self):
        """
            Function -- create_secret_code
                Generates a list of four random colors based on list of defined
                 six colors.
            Returns a list of four colors, which represents secret code.

        """
        return random.sample(COLORS, 4)

    def update_player_guess(self, marble_color: str):
        """
            Function -- count_bulls_and_cows
                Updates player's guess list for each round. It updates the list
                    using current number of guess as index and color as value.
            Paramenters:
                marble_color (str) -- color guessed by player
        """
        self.player_guess[self.num_guess] = marble_color

    def load_leaderboard(self):
        """
            Function -- load_leaderboard
                Opens leaderboard.txt file and reads each line of data, which is
                 tokenized and saved into list of scores and list of players.
                 It is then sorted based on best to worst score. If the file is
                 is not found in the directory, a new leaderboard.txt file is
                 created. If file is corrupt, it returns the error.

            Returns sorted list of top players' scores from previous games. If
                the file does not exist in the directory, leaderboard.txt is
                created and returns an empty list. If the file is corrupt,
                it returns -1 to signify error.
        """
        try:
            with open(LEADERBOARD_FILENAME, "r") as file:
                list_of_top_scores = []
                list_of_top_players = []

                for row in file.readlines():
                    top_player = row.strip().split(",")[0]
                    top_score = int(row.strip().split(",")[1])
                    list_of_top_scores.append(top_score)
                    list_of_top_players.append(top_player)

                return self.sort(list_of_top_scores, list_of_top_players)

        except FileNotFoundError:
            # Create new leaderboard.txt file and return empty list
            self.create_leaderboard_file()
            return []

        except UnicodeError:
            return -1

    def sort(self, list_of_top_scores: list, list_of_top_players: list):
        """
            Function -- sort
                Sorts list of top scores and list of top players into best to worst,
                    where best is the smallest score. It uses the selection sort
                    logic.
            Paramenters:
                list_of_top_scores (list) -- list of top scores
                list_of_top_players (list) -- list of top players
            Returns a sorted list of top players' scores.
        """

        for i in range(len(list_of_top_scores) - 1):
            minimum = i

            # Sort by inserting each element in order
            for j in range(i + 1, len(list_of_top_scores)):
                if list_of_top_scores[j] < list_of_top_scores[minimum]:
                    minimum = j

            # Swap scores
            list_of_top_scores[i], list_of_top_scores[minimum] = \
                list_of_top_scores[minimum], list_of_top_scores[i]

            # Swap players
            list_of_top_players[i], list_of_top_players[minimum] = \
                list_of_top_players[minimum], list_of_top_players[i]

        # Zip sorted list of scores and list of players
        sorted_list = list(zip(list_of_top_players, list_of_top_scores))

        return sorted_list

    def update_leaderboard(self):
        """
            Function -- update_leaderboard
                Sorts list of top scores and list of top players into best to worst,
                    where best is the smallest score. It uses the selection sort
                    logic.
            Paramenters:
                list_of_top_scores (list) -- list of top scores
                list_of_top_players (list) -- list of top players
            Returns a sorted list of top players' scores.
        """

        # When there is no top players
        if len(self.leaderboard) == 0:
            return self.leaderboard.append((self.player, self.rounds))

        # When there is one top player
        elif len(self.leaderboard) == 1:

            # When the previous player has higher score than current player
            if self.leaderboard[0][1] < self.rounds:
                return self.leaderboard.append((self.player, self.rounds))

            # When the current player has higher score than previous player
            else:
                return self.leaderboard.insert(0, (self.player, self.rounds))

        # When there is more than two top players
        else:
            for i in range(len(self.leaderboard) - 1):

                current = self.leaderboard[i][1]
                next_item = self.leaderboard[i + 1][1]

                # Find rank of current player in the list of top players
                if current <= self.rounds <= next_item:
                    return self.leaderboard.insert(i + 1,
                                                   (self.player, self.rounds))
                else:
                    return self.leaderboard.append((self.player, self.rounds))

    def create_leaderboard_file(self):
        """
            Function -- create_leaderboard_file
                Creates leaderboard.txt file.
        """
        file = open(LEADERBOARD_FILENAME, "w")
        file.close()

    def save_leaderboard(self):
        """
            Function -- save_leaderboard
                Saves sorted list of top players including current player's score
                 to leaderboard.txt file. It saves top 5 players' scores.
        """
        with open(LEADERBOARD_FILENAME, "w") as file:

            # When the list of top players is less than 6
            if len(self.leaderboard) < 6:
                for player, score in self.leaderboard:
                    file.write(player+","+str(score)+"\n")

            # When the list of top players is greater than 5
            else:
                # Truncate list to first five elements
                for player, score in self.leaderboard[:5]:
                    file.write(player+","+str(score)+"\n")

            file.close()

    def count_bulls_and_cows(self, secret_code, final_guess):
        """
            Function -- count_bulls_and_cows
                Compares the secret code with final guess of player for a round.
            Parameters:
                secret_code (list) -- secret code of game
                final_guess (list) -- list of final four color choice of player
            Returns a 2-tuple, which contains the number of bulls and cows.
        """
        bulls = 0
        cows = 0

        for i in range(len(final_guess)):

            # Count elements that have same value and index of both lists
            if final_guess[i] == secret_code[i]:
                bulls += 1

            # Count elements of final guess that is in secret code
            if final_guess[i] in secret_code:
                cows += 1

        if cows > bulls:
            cows -= bulls

        else:
            # When cows and bulls are equal or bulls equal 4
            cows = 0

        return bulls, cows

    def update_score(self, bulls: int, cows: int):
        """
            Function -- update_score
                Updates score_pegs list based on calculated bulls and cows.
            Parameters:
                bulls (int) -- number of marbles that are in correct position
                                and have correct color
                cows (int) -- number of marbles that have correct color but
                                but wrong position
        """
        score_output = []
        blank = 4 - (cows + bulls)

        score_output.extend(["black"] * bulls)
        score_output.extend(["red"] * cows)
        score_output.extend(["white"] * blank)

        self.score_pegs = score_output