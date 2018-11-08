## Dan Katz - dgkatz@bu.edu
# ps14pr1
#
class Board:
    ''' '''
    def __init__(self,height,width):
        ''' initiallizes a board object with width width and height height '''
        self.height = height
        self.width = width
        slots = []
        for r in range(height):
            row = []
            for c in range(width):
                row += [' ']
            slots += [row]
        self.slots = slots


    def __repr__(self):
        ''' returns a string representation of a Board '''
        s = ''

        for row in range(self.height):
            s += '|'
            for col in range(self.width):
                s += self.slots[row][col] + '|'
            s += '\n'

        for c in range(self.width * 2 + 1):
            s += '_'
        s += '\n'
        count = 0
        for j in range(self.width * 2 + 1):
            if j % 2 != 0:
                s += str(count)
                count += 1
                if count == 10:
                    count = 0
            else:
                s += ' '
        return s

    def add_checker(self, checker, col):
        ''' adds a checker to column col and checker piece checker '''
        assert(checker == 'X' or checker == 'O')
        assert(0 <= col < self.width)

        for r in range(self.height)[::-1]:
            if self.slots[r][col] == ' ':
                self.slots[r][col] = checker
                return

    def reset(self):
        ''' clears all board data '''
        n_board = Board(self.height,self.width)
        self.slots = n_board.slots

    def add_checkers(self, colnums):
        """ takes in a string of column numbers and places alternating
            checkers in those columns of the called Board object, 
            starting with 'X'.
        """
        checker = 'X'   # start by playing 'X'
    
        for col_str in colnums:
            col = int(col_str)
            if 0 <= col < self.width:
                self.add_checker(checker, col)
    
            # switch to the other checker
            if checker == 'X':
                checker = 'O'
            else:
                checker = 'X'
        
    def can_add_to(self, col):
        '''returns True if it is valid to place a checker in the column col'''
        if 0 <= col < self.width and self.slots[0][col] == ' ':
            return True
        else:
            return False

    def is_full(self):
        '''returns True if the called Board object is completely full of checkers'''
        for c in range(self.width):
            if self.can_add_to(c) == True:
                return False
        return True

    def remove_checker(self, col):
        '''removes the top checker from column col'''
        for r in range(self.height):
            if self.slots[r][col] != ' ':
                self.slots[r][col] = ' '
                return

    def is_win_for(self, checker):
        ''' checks if there is a win on the board for a specific player'''
        assert(checker == 'X' or checker == 'O')
        if self.is_vertical_win(checker) or \
           self.is_horizontal_win(checker) or \
           self.is_down_diagonal_win(checker) or \
           self.is_up_diagonal_win(checker):
            return True
        else:
            return False
        
    def is_horizontal_win(self, checker):
        """ Checks for a horizontal win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row][col + 1] == checker and \
                   self.slots[row][col + 2] == checker and \
                   self.slots[row][col + 3] == checker:
                    return True
    
        # if we make it here, there were no horizontal wins
        return False

    def is_vertical_win(self, checker):
        """ Checks for a vertical win for the specified checker.
        """
        for row in range(self.height - 3):
            for col in range(self.width):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col] == checker and \
                   self.slots[row + 2][col] == checker and \
                   self.slots[row + 3][col] == checker:
                    return True
    
        # if we make it here, there were no horizontal wins
        return False

    def is_down_diagonal_win(self, checker):
        """ Checks for a down - diag win for the specified checker.
        """        
        for row in range(self.height - 3):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row + 1][col + 1] == checker and \
                   self.slots[row + 2][col + 2] == checker and \
                   self.slots[row + 3][col + 3] == checker:
                    return True
        return False


    def is_up_diagonal_win(self, checker):
        """ Checks for a up - diag win for the specified checker.
        """
        for row in range(self.height):
            for col in range(self.width - 3):
                # Check if the next four columns in this row
                # contain the specified checker.
                if self.slots[row][col] == checker and \
                   self.slots[row - 1][col + 1] == checker and \
                   self.slots[row - 2][col + 2] == checker and \
                   self.slots[row - 3][col + 3] == checker:
                    return True
        return False




        
            
        
