import pygame
import sys
from pygame.locals import *
from tkinter import Tk, filedialog, simpledialog

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)

# Fonts
FONT_SIZE = 20
FONT = pygame.font.Font(None, FONT_SIZE)

# Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Text Editor")

# Text buffer
text_lines = [""]
current_line = 0
clipboard = ""
undo_stack = []
redo_stack = []

# Function to save file
def save_file():
    global text_lines
    root = Tk()
    root.withdraw()
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "w") as file:
            for line in text_lines:
                file.write(line + "\n")
    root.destroy()

# Function to open file
def open_file():
    global text_lines, current_line
    root = Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")])
    if file_path:
        with open(file_path, "r") as file:
            text_lines = file.read().splitlines()
            current_line = len(text_lines) - 1
    root.destroy()

# Function to cut text
def cut_text():
    global clipboard, text_lines
    if text_lines[current_line]:
        clipboard = text_lines[current_line]
        text_lines[current_line] = ""

# Function to copy text
def copy_text():
    global clipboard, text_lines
    clipboard = text_lines[current_line]

# Function to paste text
def paste_text():
    global clipboard, text_lines
    if clipboard:
        text_lines[current_line] += clipboard

# Function to undo
def undo():
    global text_lines, undo_stack, redo_stack
    if undo_stack:
        redo_stack.append(text_lines.copy())
        text_lines = undo_stack.pop()

# Function to redo
def redo():
    global text_lines, undo_stack, redo_stack
    if redo_stack:
        undo_stack.append(text_lines.copy())
        text_lines = redo_stack.pop()

# Function to clear text area
def clear_text_area():
    global text_lines, current_line
    text_lines = [""]
    current_line = 0

# Main loop
running = True
while running:
    screen.fill(WHITE)

    # Event handling
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_RETURN:  # Enter key
                undo_stack.append(text_lines.copy())
                redo_stack.clear()
                text_lines.append("")
                current_line += 1
            elif event.key == K_BACKSPACE:  # Backspace key
                undo_stack.append(text_lines.copy())
                redo_stack.clear()
                if len(text_lines[current_line]) > 0:
                    text_lines[current_line] = text_lines[current_line][:-1]
                else:
                    if current_line > 0:
                        current_line -= 1
                        text_lines.pop()
            elif event.key == K_s and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+S to save
                save_file()
            elif event.key == K_o and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+O to open
                open_file()
            elif event.key == K_x and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+X to cut
                cut_text()
            elif event.key == K_c and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+C to copy
                copy_text()
            elif event.key == K_v and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+V to paste
                paste_text()
            elif event.key == K_z and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+Z to undo
                undo()
            elif event.key == K_y and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+Y to redo
                redo()
            elif event.key == K_n and pygame.key.get_mods() & KMOD_CTRL:  # Ctrl+N to clear
                clear_text_area()
            else:  # Regular text input
                undo_stack.append(text_lines.copy())
                redo_stack.clear()
                text_lines[current_line] += event.unicode

    # Render text
    y = 0
    for line in text_lines:
        text_surface = FONT.render(line, True, BLACK)
        screen.blit(text_surface, (5, y))
        y += FONT_SIZE + 5

    pygame.display.flip()

pygame.quit()
sys.exit()
