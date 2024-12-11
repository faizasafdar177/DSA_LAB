import pygame
import sys
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 600, 600
GRID_SIZE = 10
CELL_SIZE = WIDTH // GRID_SIZE

# Colors
BACKGROUND_COLOR = (255, 228, 196)
SNAKE_COLOR = (0, 255, 0)
LADDER_COLOR = (255, 0, 0)
PLAYER1_COLOR = (0, 0, 255)
PLAYER2_COLOR = (255, 165, 0)
TEXT_COLOR = (0, 0, 0)
LINE_COLOR = (0, 0, 0)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake and Ladder")

# Game variables
player_positions = [0, 0]
current_player = 0
snakes = {97: 78, 93: 68, 64: 60, 62: 19, 17: 7}
ladders = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 36: 44, 51: 67, 71: 91, 80: 99}
font = pygame.font.Font(None, 36)

# Functions
def draw_grid():
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            rect = pygame.Rect(col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, LINE_COLOR, rect, 1)
            number = GRID_SIZE * (GRID_SIZE - row - 1) + (col + 1) if row % 2 == 0 else GRID_SIZE * (GRID_SIZE - row) - col
            text = font.render(str(number), True, TEXT_COLOR)
            screen.blit(text, (col * CELL_SIZE + 5, row * CELL_SIZE + 5))

def draw_snakes_and_ladders():
    for start, end in snakes.items():
        start_pos = get_pos(start)
        end_pos = get_pos(end)
        pygame.draw.line(screen, SNAKE_COLOR, start_pos, end_pos, 5)

    for start, end in ladders.items():
        start_pos = get_pos(start)
        end_pos = get_pos(end)
        pygame.draw.line(screen, LADDER_COLOR, start_pos, end_pos, 5)

def get_pos(square):
    row, col = divmod(square, GRID_SIZE)
    col = col if row % 2 == 0 else GRID_SIZE - 1 - col
    x = col * CELL_SIZE + CELL_SIZE // 2
    y = (GRID_SIZE - 1 - row) * CELL_SIZE + CELL_SIZE // 2
    return (x, y)

def draw_players():
    for i, pos in enumerate(player_positions):
        x, y = get_pos(pos)
        color = PLAYER1_COLOR if i == 0 else PLAYER2_COLOR
        pygame.draw.circle(screen, color, (x, y), CELL_SIZE // 4)

def roll_dice():
    return random.randint(1, 6)

def move_player():
    global current_player
    roll = roll_dice()
    player_positions[current_player] += roll
    if player_positions[current_player] > 99:
        player_positions[current_player] = 99
    if player_positions[current_player] in snakes:
        player_positions[current_player] = snakes[player_positions[current_player]]
    if player_positions[current_player] in ladders:
        player_positions[current_player] = ladders[player_positions[current_player]]
    current_player = 1 - current_player

def draw_text(text, x, y):
    text_surface = font.render(text, True, TEXT_COLOR)
    screen.blit(text_surface, (x, y))

# Main game loop
running = True
while running:
    screen.fill(BACKGROUND_COLOR)
    draw_grid()
    draw_snakes_and_ladders()
    draw_players()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            move_player()

    winner = None
    if 99 in player_positions:
        winner = "Player 1" if player_positions[0] == 99 else "Player 2"
    
    if winner:
        draw_text(f"{winner} Wins!", WIDTH // 2 - 50, HEIGHT // 2 - 20)

    pygame.display.flip()

pygame.quit()
sys.exit()
