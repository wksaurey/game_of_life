empty_board = [[0 * 10] * 10] * 10
simple_glider = [
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 1, 1],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
loaf_pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
rocket = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]

class Board:

    def __init__(self, board):
        self.board = board
        self.alive_cell_coordinates = set()

    def print_board(self):
        for row in self.board:
            print(row)

    def find_initial_alive(self):
        for rowIndex, row in enumerate(self.board):
            for columnIndex, cell in enumerate(row):
                if cell == 1:
                    self.alive_cell_coordinates.add((columnIndex, rowIndex))

    def make_dead(self, coordinates):
            self.board[coordinates[1]][coordinates[0]] = 0
            self.alive_cell_coordinates.remove(coordinates)

    def make_alive(self, coordinates):
        self.board[coordinates[1]][coordinates[0]] = 1 # 1 == true, 0 == false, self.board[y][x]
        self.alive_cell_coordinates.add(coordinates)

    def update_board(self):
        for coordinates in self.alive_cell_coordinates:
            # check all 9 cells in block around live cell
            check_cell(coordinates[0], coordinates[1])
    
    def check_cell(self,x, y):
        # find alive_count around cell
        pass





myBoard = Board(simple_glider)
myBoard.print_board()
myBoard.find_initial_alive()
print(myBoard.alive_cell_coordinates)
myBoard.make_dead((8, 0))
myBoard.print_board()
print(myBoard.alive_cell_coordinates)
myBoard.make_alive((8, 0))
myBoard.make_alive((8, 0))
print(myBoard.alive_cell_coordinates)
myBoard.print_board()

