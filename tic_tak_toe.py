import pygame
import sys

# Initialize pygame
pygame.init()

# Set up the game window
size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Tic-Tac-Toe")

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Define the board
board = [[None]*3, [None]*3, [None]*3]

# Define fonts
font = pygame.font.Font(None, 74)
font_small = pygame.font.Font(None, 24)

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    pygame.draw.line(screen, BLACK, (100, 0), (100, 300), 2)
    pygame.draw.line(screen, BLACK, (200, 0), (200, 300), 2)
    pygame.draw.line(screen, BLACK, (0, 100), (300, 100), 2)
    pygame.draw.line(screen, BLACK, (0, 200), (300, 200), 2)

    for row in range(3):
        for col in range(3):
            if board[row][col] == 'X':
                pygame.draw.line(screen, RED, (col*100+15, row*100+15), (col*100+85, row*100+85), 2)
                pygame.draw.line(screen, RED, (col*100+85, row*100+15), (col*100+15, row*100+85), 2)
            elif board[row][col] == 'O':
                pygame.draw.circle(screen, BLACK, (col*100+50, row*100+50), 40, 2)

# Function to check for a win or tie
def check_winner():
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] is not None:
            return board[row][0]
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] is not None:
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not None:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not None:
        return board[0][2]
    for row in board:
        if None in row:
            return None
    return 'Tie'

# Main game loop
player = 'X'
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = event.pos
            row, col = y // 100, x // 100
            if board[row][col] is None:
                board[row][col] = player
                winner = check_winner()
                if winner is not None:
                    print(f"Winner is {winner}")
                    pygame.time.wait(2000)
                    board = [[None]*3, [None]*3, [None]*3]
                player = 'O' if player == 'X' else 'X'

    draw_board()
    pygame.display.flip()

pygame.quit()
sys.exit()
