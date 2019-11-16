class GameOfLife:
    def __init__(self, board):
        self.board = board

    def nextGen(self):
        for row in range(len(self.board)):
            for column in range(len(self.board[0])):
                neighbours = self.countNeighbours(row, column)
                    
        self.board = [[False, False, False],
                     [False, False, False],
                     [False, False, False]]

    def countNeighbours(self, row, column):
        count = 0
        if ((row - 1 >= 0) and (column - 1 >= 0)):
            if self.board[row-1][column-1]:
                count += 1
        if (row -1 >= 0):
            if self.board[row-1][column]:
                count += 1
        if ((row-1 >= 0) and (column +1 >= 0))




