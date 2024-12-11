import random

# Sample word list
word_list = ["apple", "banana", "grape", "orange", "kiwi", "lemon"]

# Define the grid size
GRID_SIZE = 10

# Initialize the grid
grid = [['.' for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

# Function to print the grid
def print_grid(grid):
    for row in grid:
        print(' '.join(row))

# Function to place a word in the grid
def place_word(word):
    direction = random.choice(['horizontal', 'vertical'])
    length = len(word)

    if direction == 'horizontal':
        row = random.randint(0, GRID_SIZE - 1)
        col = random.randint(0, GRID_SIZE - length)
        for i in range(length):
            grid[row][col + i] = word[i]
    elif direction == 'vertical':
        row = random.randint(0, GRID_SIZE - length)
        col = random.randint(0, GRID_SIZE - 1)
        for i in range(length):
            grid[row + i][col] = word[i]

# Main function
if __name__ == "__main__":
    print("Crossword Puzzle Game")

    # Place words in the grid
    for word in word_list:
        place_word(word)

    # Print the final grid
    print("\nGenerated Crossword Grid:")
    print_grid(grid)

    print("\nFind the words in the grid!")
    for word in word_list:
        print(f" - {word}")

    # Simple interaction to find words
    while True:
        input_word = input("\nEnter a word to find (or type 'exit' to quit): ").lower()
        if input_word == 'exit':
            break
        elif input_word in word_list:
            print(f"Yes, '{input_word}' is in the crossword!")
        else:
            print(f"Sorry, '{input_word}' is not in the crossword.")
