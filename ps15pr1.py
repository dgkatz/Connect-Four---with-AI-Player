## Dan Katz - dgkatz@bu.edu
# ps15pr1.py (Problem Set 15, Problem 1)
#
# An RandomPlayer for use in Connect Four
#

import random
from ps14pr3 import * # to use the connect_four and process_move functions

class RandomPlayer(Player):

    def next_move(self, board):
        '''uses random class to return random move'''
        choices = []
        for c in range(board.width):
            if board.can_add_to(c):
                choices += [c]
        column = random.choice(choices)
        self.num_moves += 1
        return column
