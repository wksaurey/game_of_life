import time
import pygame

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
big_loaf_pattern = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
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
big_board_pattern = [
    [0] * 30 for _ in range(30)
]
# Set some cells to be alive in the larger pattern
# For example, a glider pattern
big_board_pattern[1][1] = 1
big_board_pattern[2][2] = 1
big_board_pattern[2][3] = 1
big_board_pattern[3][1] = 1
big_board_pattern[3][2] = 1

class Board:

    def __init__(self, board):
        self.size = len(board)
        self.board = board
        self.alive_cell_coordinates = set()
        self.willDie = set()
        self.willLive = set()

    def print_board(self):
        for row in self.board:
            for num in row:
                if num == 0:
                    output = 'O'
                else: 
                    output = '*'
                print(output, end=' ')
            print()
        print('-' * self.size * 3, end=None)

    def display_board(self):
        pygame.init()

        # constants
        CELL_SIZE = 20
        PANEL_HEIGHT = 50
        WIDTH, HEIGHT = self.size * CELL_SIZE, self.size * CELL_SIZE + PANEL_HEIGHT
        SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
        CLOCK = pygame.time.Clock()

        button_rect = pygame.Rect(10, self.size * CELL_SIZE + 10, 80, 30)
        clear_button_rect = pygame.Rect(100, self.size * CELL_SIZE + 10, 100, 30)
       
        is_playing = False

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        if button_rect.collidepoint(event.pos):
                            is_playing = not is_playing  # Toggle play/pause on button click
                        elif clear_button_rect.collidepoint(event.pos):
                            # Clear the boarda (set all alive cells to dead)
                            for y in range(self.size):
                                for x in range(self.size):
                                    if self.board[y][x] == 1:
                                        self.make_dead((x, y))
                    if event.button == 1 and not is_playing:  # Left mouse button click while paused
                        mouse_x, mouse_y = event.pos
                        # Check if the click is within the grid area
                        if mouse_y < self.size * CELL_SIZE:
                            # Calculate cell coordinates based on mouse position
                            cell_x = mouse_x // CELL_SIZE
                            cell_y = mouse_y // CELL_SIZE
                            # Toggle the state of the clicked cell
                            if self.board[cell_y][cell_x] == 0:
                                self.make_alive((cell_x, cell_y))
                            else:
                                self.make_dead((cell_x, cell_y))

            
            # clear the screen
            SCREEN.fill((0, 0, 0))

            # draw the cells
            for y in range(self.size):
                for x in range(self.size):
                    cell_rect = pygame.Rect(x * CELL_SIZE, y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    if self.board[y][x] == 1:
                        # Draw alive cells in green color
                        pygame.draw.rect(SCREEN, (0, 255, 0), cell_rect)
                    # Outline each cell in green
                    pygame.draw.rect(SCREEN, (0, 255, 0), cell_rect, 1)

            # draw the control panel 
            pygame.draw.rect(SCREEN, (50, 50, 50), (0, self.size * CELL_SIZE, WIDTH, PANEL_HEIGHT))

            # draw the pause/play button
            button_text = "Pause" if is_playing else "Play"
            pygame.draw.rect(SCREEN, (100, 100, 100), button_rect)
            font = pygame.font.SysFont(None, 24)
            text = font.render(button_text, True, (255, 255, 255))
            text_rect = text.get_rect(center=button_rect.center)
            SCREEN.blit(text, text_rect)

            # Draw the Clear Board button
            pygame.draw.rect(SCREEN, (100, 100, 100), clear_button_rect)
            clear_text = "Clear Board"
            font = pygame.font.SysFont(None, 24)
            clear_text_render = font.render(clear_text, True, (255, 255, 255))
            clear_text_rect = clear_text_render.get_rect(center=clear_button_rect.center)
            SCREEN.blit(clear_text_render, clear_text_rect)

            # update the board
            pygame.display.flip()
            CLOCK.tick(10) # adjust the speed here (frames per second)

            if is_playing:
                # update the board if playing
                self.update_board()
                pygame.display.set_caption("Conway's Game of Life")

                # process cell updates
                for coordinates in self.willDie:
                    self.make_dead(coordinates)
                for coordinates in self.willLive:
                    self.make_alive(coordinates)

                self.willDie = set()
                self.willLive = set()

    def find_initial_alive(self):
        for rowIndex, row in enumerate(self.board):
            for columnIndex, cell in enumerate(row):
                if cell == 1:
                    self.alive_cell_coordinates.add((columnIndex, rowIndex))

    def make_dead(self, coordinates):
            self.board[coordinates[1]][coordinates[0]] = 0
            if(coordinates in self.alive_cell_coordinates):
                self.alive_cell_coordinates.remove(coordinates)

    def make_alive(self, coordinates):
        self.board[coordinates[1]][coordinates[0]] = 1 # 1 == true, 0 == false, self.board[y][x]
        self.alive_cell_coordinates.add(coordinates)

    def update_board(self):
        for coordinates in self.alive_cell_coordinates:
            # check all 9 cells in block around live cell (including live cell)
            for x in range(coordinates[0]-1, coordinates[0]+2):
                for y in range(coordinates[1]-1, coordinates[1]+2):
                    if x < 0 or x >= self.size or y < 0 or y >= self.size:
                        continue
                    self.check_cell([x, y])
    
    def check_cell(self, coordinates):
        # find alive_count around cell (don't include the cell itself)
        alive_count = 0
        for x in range(coordinates[0]-1, coordinates[0]+2):
            for y in range(coordinates[1]-1, coordinates[1]+2):
                if x == coordinates[0] and y == coordinates[1]:
                    continue  # Skip the current cell itself
                if x < 0 or x >= self.size or y < 0 or y >= self.size:
                    continue
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
            self.make_dead(coordinates)
        for coordinates in self.willLive:
            self.make_alive(coordinates)
        time.sleep(1)
        self.willDie = set()
        self.willLive = set()
        self.game_loop()

    def start_game(self):
        self.find_initial_alive()
        # self.game_loop()
        self.display_board()


myBoard = Board(big_board_pattern)
myBoard.start_game()