import time

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
        self.willDie = set()
        self.willLive = set()

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
            self.check_cell([coordinates[-1], coordinates[-1]])
            self.check_cell([coordinates[-1], coordinates[0]])
            self.check_cell([coordinates[-1], coordinates[1]])
            self.check_cell([coordinates[0], coordinates[-1]])
            self.check_cell([coordinates[0], coordinates[0]])
            self.check_cell([coordinates[0], coordinates[1]])
            self.check_cell([coordinates[1], coordinates[-1]])
            self.check_cell([coordinates[1], coordinates[0]])
            self.check_cell([coordinates[1], coordinates[1]])
    
    def check_cell(self, coordinates):
        # find alive_count around cell
        alive_count = 0
        if self.board[coordinates[1]-1, coordinates[0]]-1:
            alive_count += 1
        if self.board[coordinates[1]-1, coordinates[0]]:
            alive_count += 1
        if self.board[coordinates[1]-1, coordinates[0]]+1:
            alive_count += 1
        if self.board[coordinates[1], coordinates[0]]-1:
            alive_count += 1
        if self.board[coordinates[1], coordinates[0]]:
            alive_count += 1
        if self.board[coordinates[1], coordinates[0]]+1:
            alive_count += 1
        if self.board[coordinates[1]+1, coordinates[0]]-1:
            alive_count += 1
        if self.board[coordinates[1]+1, coordinates[0]]:
            alive_count += 1
        if self.board[coordinates[1]+1, coordinates[0]]+1:
            alive_count += 1
        # add cells to sets to update at resolution of move
        if alive_count < 2 or alive_count > 3: self.willDie.add(coordinates)
        if alive_count == 3: self.willLive.add(coordinates)

        def game_loop(self):
            self.update_board()
            self.print_board()
            for coordinates in self.willDie:
                self.board[coordinates[1], coordinates[0]] = 0
            for coordinates in self.willLive:
                self.board[coordinates[1], coordinates[0]] = 1
            time.sleep(1)
            self.game_loop()
    
        def start_game(self):
            self.find_initial_alive()
            self.game_loop()



myBoard = Board(simple_glider)