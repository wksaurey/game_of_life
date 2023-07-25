import time

empty_board = [[0 * 10] * 10] * 10
simple_repeater = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
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
        self.willDie = set()
        self.willLive = set()

    def print_board(self):
        for row in self.board:
            print(row)
        print('------------------------------')

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
            # check all 9 cells in block around live cell (including live cell)
            for x in range(coordinates[0]-1, coordinates[0]+2):
                for y in range(coordinates[1]-1, coordinates[1]+2):
                    x = min(max(x, 0), 9)
                    y = min(max(y, 0), 9)
                    self.check_cell([x, y])
    
    def check_cell(self, coordinates):
        # find alive_count around cell (don't include the cell itself)
        alive_count = 0
        for x in range(coordinates[0]-1, coordinates[0]+2):
            for y in range(coordinates[1]-1, coordinates[1]+2):
                if x == coordinates[0] and y == coordinates[1]:
                    continue  # Skip the current cell itself
                x = min(max(x, 0), 9)
                y = min(max(y, 0), 9)
                a = self.board[y][x]
                if self.board[y][x]:
                    alive_count += 1
        # add cells to sets to update at resolution of move
        if alive_count < 2 or alive_count > 3: self.willDie.add(tuple(coordinates))
        if alive_count == 3: self.willLive.add(tuple(coordinates))

    def game_loop(self):
        self.update_board()
        self.print_board()
        for coordinates in self.willDie:
            self.board[coordinates[1]][coordinates[0]] = 0
        for coordinates in self.willLive:
            self.board[coordinates[1]][coordinates[0]] = 1
        time.sleep(1)
        self.willDie = set()
        self.willLive = set()
        self.game_loop()

    def start_game(self):
        self.find_initial_alive()
        self.game_loop()



myBoard = Board(rocket)
myBoard.start_game()