# -*- coding: utf-8 -*-


class GameException(Exception):
    pass


class Game(object):
    """ Tic Tac Toe game with grid implemented as a matrix of composed dictionaries.
    Each cell of the dictionary contains
    a Token, indexed as grid[row][column]
    (where rows and columns are 1-indexed rather than 0-indexed)
    ie, grid = {1:{1: Token, 2:Token, 3:Token}, ...}
        where each token is either "X" or "O"
    """

    X = "X"
    O = "O"
    grid_size = 3
    indices = [i for i in range(1, grid_size + 1)]


    def __init__(self):
        self.grid = {row: {} for row in self.indices}
        self.winner = None
        self.next_token = self.X


    def __repr__(self):
        """ Represents grid as 3x3 array surrounded by newlines.
            Empty cells are indicated with a dash: '-'
        """
        row_strings = []
        for r in reversed(self.indices):
            r_tokens = [self.get_token(r, c) for c in self.indices]
            r_string = "".join([t if t is not None else "-" for t in r_tokens])
            row_strings.append(r_string)
        return "\n{}\n".format("\n".join(row_strings))


    def handle_token(self, column):
        """ Returns the (row, column) index of the newly added token. """
        if self.winner:
            raise GameException("Game already has winner: " + str(self.winner))

        try:
            column = int(column)
        except TypeError:
            raise GameException("Unrecognized column")

        if column not in self.indices:
            raise GameException("Unrecognized column")

        cell = self.add_token(self.next_token, column)
        self.next_token = self.O if self.next_token == self.X else self.X
        self.winner = self.get_winner()
        return cell


    def add_token(self, token, column):
        # Put the token in the lowest available row for given column
        for row in self.indices:
            if self.get_token(row, column) is None:
                self.grid[row][column] = token
                return (row, column)

        raise GameException("Column filled")


    def get_token(self, row, column):
        if (row in self.grid) and column in self.grid[row]:
            return self.grid[row][column]


    def get_winner(self):
        """ Returns winner token if there is a winner,
            otherwise None.

            Checks rows, columns, diagonals
        """
        # Check for horizontal wins
        for r in self.indices:
            line = [self.get_token(r, c) for c in self.indices]
            if line[0] and all(line[0] == i for i in line):
                return line[0]

        # Check for vertical wins
        for c in self.indices:
            line = [self.get_token(r, c) for r in self.indices]
            if line[0] and all(line[0] == i for i in line):
                return line[0]

        # Check for diagonal wins
        line = [self.get_token(i, i) for i in self.indices]
        if line[0] and all(line[0] == i for i in line):
            return line[0]
        line = [self.get_token(i, self.grid_size - i) for i in self.indices]
        if line[0] and all(line[0] == i for i in line):
            return line[0]
