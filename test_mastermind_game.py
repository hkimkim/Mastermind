"""
   CS5001
   Spring 2021
   Heekyung Kim
   Final Project: Mastermind

   This program uses class imported from Model.py file.
   This program tests Model class.
"""
import unittest
from Model import Model
from constants import COLORS


class TestModel(unittest.TestCase):
    """
        Class: TestModel
        TestModel is used to test Model class from Model.py.

        It tests
        class initialization, and class methods -- make_reciprocal, validate,
        check_zero_denominator, check_sign, multipy, divide, __str__,
        and __eq__.
    """

    def test_init(self):
        model = Model()

        self.assertEqual(model.rounds, 0)
        self.assertEqual(model.num_guess, 0)
        self.assertEqual(model.player, "")
        self.assertEqual(model.player_guess, ["white", "white", "white", "white"])
        self.assertEqual(model.score_pegs, [])

    def test_set_player(self):
        model = Model()
        model.set_player("joshua")
        self.assertEqual(model.player, "joshua")

    def test_set_num_guess(self):
        model = Model()
        model.set_num_guess(3)
        self.assertEqual(model.num_guess, 3)

    def test_set_rounds(self):
        model = Model()
        model.set_rounds(4)
        self.assertEqual(model.rounds, 4)

    def test_update_player_guess(self):
        model = Model()

        self.assertEqual(model.player_guess, ["white", "white", "white", "white"])

        model.set_num_guess(3)
        model.update_player_guess('green')
        self.assertEqual(model.player_guess, ["white", "white", "white", "green"])

        model.set_num_guess(1)
        model.update_player_guess('yellow')
        self.assertEqual(model.player_guess, ["white", "yellow", "white", "green"])

        model.set_num_guess(3)
        model.update_player_guess('red')
        self.assertEqual(model.player_guess, ["white", "yellow", "white", "red"])

    def test_sort(self):
        # When both lists are empty
        list_of_top_scores = []
        list_of_top_players = []

        model = Model()

        actual = model.sort(list_of_top_scores, list_of_top_players)
        expected = []

        self.assertEqual(actual, expected)

        # When there are more than two elements in lists
        list_of_top_scores = [10, 1, 8, 9, 5]
        list_of_top_players = ['jake', 'marry', 'jill', 'berry', 'amy']

        model = Model()

        actual = model.sort(list_of_top_scores, list_of_top_players)
        expected = [('marry', 1), ('amy', 5), ('jill', 8),
                    ('berry', 9), ('jake', 10)]

        self.assertEqual(actual, expected)

        # When there are two elements in the lists
        list_of_top_scores = [10, 1]
        list_of_top_players = ['jake', 'marry']

        model = Model()

        actual = model.sort(list_of_top_scores, list_of_top_players)
        expected = [('marry', 1), ('jake', 10)]

        self.assertEqual(actual, expected)

    def test_update_leaderboard(self):
        # Test when size of leader board is 0
        model = Model()
        model.leaderboard = []
        model.player = 'jerry'
        model.rounds = 1
        model.update_leaderboard()

        expected = [('jerry', 1)]

        self.assertEqual(model.leaderboard, expected)

        # Test when size of leader board is less than 2
        model = Model()
        model.leaderboard = [('amy', 5)]
        model.player = 'john'
        model.rounds = 2
        model.update_leaderboard()

        expected = [('john', 2), ('amy', 5)]

        self.assertEqual(model.leaderboard, expected)

        # Test when size of leader board is less than 2
        model = Model()
        model.leaderboard = [('amy', 5)]
        model.player = 'john'
        model.rounds = 7
        model.update_leaderboard()

        expected = [('amy', 5), ('john', 7)]

        self.assertEqual(model.leaderboard, expected)

        # Test when size of leader board is greater than 2
        model = Model()
        model.leaderboard = [('marry', 1), ('amy', 5), ('jill', 8),
                             ('berry', 9), ('jake', 10)]
        model.player = 'diaz'
        model.rounds = 4
        model.update_leaderboard()

        expected = [('marry', 1), ('diaz', 4), ('amy', 5), ('jill', 8),
                    ('berry', 9), ('jake', 10)]

        self.assertEqual(model.leaderboard, expected)

        # Test when size of leader board is greater than 2
        model = Model()
        model.leaderboard = [('marry', 1), ('amy', 5), ('jill', 8),
                             ('berry', 9), ('jake', 9)]
        model.player = 'diaz'
        model.rounds = 10
        model.update_leaderboard()

        expected = [('marry', 1), ('amy', 5), ('jill', 8), ('berry', 9),
                    ('jake', 9), ('diaz', 10)]

        self.assertEqual(model.leaderboard, expected)

    def test_count_bulls_and_cows(self):
        model = Model()

        # When guessed all correct color, but two wrong position
        secret_code = ['green', 'blue', 'yellow', 'red']
        final_guess = ['green', 'blue', 'red', 'yellow']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (2, 2)

        self.assertEqual(actual, expected)

        # When one correct position and two correct color
        secret_code = ['green', 'blue', 'yellow', 'red']
        final_guess = ['black', 'purple', 'blue', 'red']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (1, 1)
        self.assertEqual(actual, expected)

        # When guessed one wrong
        secret_code = ['green', 'blue', 'yellow', 'red']
        final_guess = ['green', 'blue', 'yellow', 'purple']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (3, 0)
        self.assertEqual(actual, expected)

        # When all correct color but all wrong position
        secret_code = ['green', 'blue', 'yellow', 'red']
        final_guess = ['blue', 'green', 'red', 'yellow']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (0, 4)
        self.assertEqual(actual, expected)

        # When one correct position and three color correct
        secret_code = ['blue', 'green', 'yellow', 'red']
        final_guess = ['black', 'yellow', 'green', 'red']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (1, 2)
        self.assertEqual(actual, expected)

        # When two correct position and three correct color
        secret_code = ['blue', 'green', 'yellow', 'red']
        final_guess = ['blue', 'green', 'black', 'yellow']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (2, 1)
        self.assertEqual(actual, expected)

        # When guessed secret code
        secret_code = ['blue', 'green', 'red', 'yellow']
        final_guess = ['blue', 'green', 'red', 'yellow']

        actual = model.count_bulls_and_cows(secret_code, final_guess)
        expected = (4, 0)
        self.assertEqual(actual, expected)

    def test_update_score(self):
        model = Model()

        # When guessed all cows
        bulls = 0
        cows = 4

        model.update_score(bulls, cows)

        actual = model.score_pegs
        expected = ["red", "red", "red", "red"]

        self.assertEqual(actual, expected)

        # When one bulls and two cows
        bulls = 1
        cows = 2

        model.update_score(bulls, cows)

        actual = model.score_pegs
        expected = ["black", "red", "red", "white"]

        self.assertEqual(actual, expected)

        # When guessed secret code
        bulls = 4
        cows = 0

        model.update_score(bulls, cows)

        actual = model.score_pegs
        expected = ["black", "black", "black", "black"]

        self.assertEqual(actual, expected)

    def test_create_secret_code(self):
        model = Model()
        secret_code = model.create_secret_code()

        # Check the len created secret code is 4
        self.assertEqual(len(secret_code), 4)
        self.assertFalse(len(secret_code) == 5)

        # Check that secret code only have defined colors
        for color in secret_code:
            self.assertIn(color, COLORS)


def main():
    unittest.main()


if __name__ == '__main__':
    main()


