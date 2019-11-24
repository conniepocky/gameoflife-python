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
        try:
            if ((row - 1 >= 0) and (column - 1 >= 0)):
                if self.board[row-1][column-1]:
                    count += 1
            if (row -1 >= 0):
                if self.board[row-1][column]:
                    count += 1
            if (row -1 >= 0) and (column +1 >= 0):
                if self.board[row-1][column+1]:
                    count+= 1
            if (column -1 >= 0):
                if self.board[row][column-1]:
                    count += 1
            if (column +1 < len(self.board[0])):
                if self.board[row][column+1]:
                    count += 1

            # from here on, all "row +1 >= 0" conditions have to change. You need to check if row +1 is strictly smaller than the length of the entire board (the number of rows).
            # and, all "column +1 >= 0" conditions have to change. You need to check if column +1 < len(self.board[0]).
            if (row +1 >= 0) and (column -1 >= 0):
                if self.board[row+1][column-1]:
                    count += 1
            if (row +1 >= 0):
                if self.board[row+1][column]:
                    count += 1
            if (row +1 >= 0) and (column +1 >= 0):
                if self.board[row+1][column+1]:
                    count += 1

            if count > 3 or count < 2:
                self.board[row][column] = False
            else:
                self.board[row][column] = True
        except Exception as e:
            print(e)
            print("row {}, column {}".format(row, column))
            print(self.board)
            raise




