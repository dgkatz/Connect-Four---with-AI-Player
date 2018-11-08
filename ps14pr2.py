## Dan Katz - dgkatz@bu.edu
# ps14pr2.py (Problem Set 14, Problem 2)
#
# A Connect Four Player class 
#

from ps14pr1 import Board

class Player:


    def __init__(self, checker):
        '''constructs a new Player object
        '''
        assert(checker == 'X' or checker == 'O')

        self.checker = checker
        self.num_moves = 0

    def __repr__(self):
        '''prints the player object
        '''
        s = 'Player ' + self.checker
        return s

    def opponent_checker(self):
        '''returns a one-character string representing the
           checker of the Player object’s opponent
        '''
        if self.checker == 'X':
            return 'O'
        return 'X'

    def next_move(self, board):
        '''returns the column where the player wants to make
           the next move
        '''
        column = int(input('Enter a column number: '))
        while board.can_add_to(column) != True:
            print('Try again!')
            column = int(input('Enter a column number: '))
        self.num_moves += 1
        return column
    
        

