## Dan Katz - dgkatz@bu.edu
# ps15pr2.py (Problem Set 15, Problem 2)
#
# An AI Player for use in Connect Four
#

import random
from ps14pr3 import * # to use the connect_four and process_move functions
from ps14pr2 import Player
from ps15pr1 import RandomPlayer

class AIPlayer(Player):
    def __init__(self, checker, tiebreak, lookahead):
        """ construct a random player object wich is a sublclass of player
        """
        assert(checker == 'X' or checker == 'O')
        assert(tiebreak == 'LEFT' or tiebreak == 'RIGHT' or tiebreak == 'RANDOM')
        assert(lookahead >= 0)

        self.checker = checker
        self.num_moves = 0
        self.tiebreak = tiebreak
        self.lookahead = lookahead

    def __repr__(self):
        ''' return a string representation of the player subclass AIPlayer'''
        s = "Player " + self.checker + ' (' + self.tiebreak + ', ' + str(self.lookahead) + ')'
        return s

    def max_score_column(self, scores):
        '''returns the index of the column with the maximum score'''
        max_score = max(scores)
        lc = [i for i in range(len(scores)) if scores[i] == max_score]
        if self.tiebreak == 'LEFT':
            return lc[0]
        elif self.tiebreak == 'RIGHT':
            return lc[-1]
        else:
            return random.choice(lc)

    def scores_for(self, board):
        '''reterns the list of scores derived from algorithim'''
        scores = [' '] * board.width
        for c in range(board.width):
            if board.can_add_to(c) == False:
                scores[c] = -1
            elif board.is_win_for(self.checker):
                scores[c] = 100
            elif board.is_win_for(self.opponent_checker()):
                scores[c] = 0
            elif self.lookahead == 0:
                scores[c] = 50
            else:
                board.add_checker(self.checker, c)
                opp = AIPlayer(self.opponent_checker(), self.tiebreak, self.lookahead - 1)
                opp_scores = opp.scores_for(board)
                max_opp_score = max(opp_scores)
                scores[c] = 100 - max_opp_score
                board.remove_checker(c)
        return scores

    def next_move(self, board):
        '''returns column index for AIPlayer move'''
        scores = self.scores_for(board)
        column = self.max_score_column(scores)
        self.num_moves += 1
        return column
    
    
        

        
