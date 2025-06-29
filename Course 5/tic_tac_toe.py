# Task 1: Implement the Basic Functions and Structure of the Game

# Understand the board structure

# Print the board

# Allow marking a cell

def create_board():
    return [[" " for _ in range(3)] for _ in range(3)]

def print_board(board):
    for row in board:
        print("|".join(row))
        print("-" * 5)

def mark_board(board, row, col, player):
    if board[row][col] == " ":
        board[row][col] = player
        return True
    return False


# Task 2: Take Input and Alternate Turns

# Accept user input

# Alternate turns between Player X and Player O

def play_game():
    board = create_board()
    current_player = "X"
    
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter col (0-2): "))
        
        if mark_board(board, row, col, current_player):
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    
    print_board(board)

# Task 3: Check for Winning Move and Announce Winner

# Check for a winning condition

# Announce the winner or if it’s a tie

def check_winner(board):
    for row in board:
        if row[0] == row[1] == row[2] != " ":
            return row[0]
    
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != " ":
            return board[0][col]
    
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]
    
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]
    
    return None

def play_game():
    board = create_board()
    current_player = "X"
    
    for _ in range(9):
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter col (0-2): "))
        
        if mark_board(board, row, col, current_player):
            winner = check_winner(board)
            if winner:
                print_board(board)
                print(f"Player {winner} wins!")
                return
            current_player = "O" if current_player == "X" else "X"
        else:
            print("Invalid move. Try again.")
    
    print_board(board)
    print("It's a tie!")


# Task 4: Build Background Graphics Using Pygame

# Set up a Pygame window

# Draw a grid background

import pygame
pygame.init()

WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 5
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic-Tac-Toe")

def draw_grid():
    SCREEN.fill((255, 255, 255))
    pygame.draw.line(SCREEN, (0, 0, 0), (100, 0), (100, 300), LINE_WIDTH)
    pygame.draw.line(SCREEN, (0, 0, 0), (200, 0), (200, 300), LINE_WIDTH)
    pygame.draw.line(SCREEN, (0, 0, 0), (0, 100), (300, 100), LINE_WIDTH)
    pygame.draw.line(SCREEN, (0, 0, 0), (0, 200), (300, 200), LINE_WIDTH)

def main():
    run = True
    while run:
        draw_grid()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        pygame.display.update()

main()
pygame.quit()

# Task 5: Use Pygame Events to Take Input

# Detect mouse clicks

# Convert them into board moves

def get_cell(pos):
    x, y = pos
    row = y // 100
    col = x // 100
    return row, col

if event.type == pygame.MOUSEBUTTONDOWN:
    row, col = get_cell(pygame.mouse.get_pos())
    # Update board and re-render based on turn


# Task 6: Animate the Game

# Show Xs and Os

# Animate them drawing into the grid

def draw_X(row, col):
    start_x = col * 100
    start_y = row * 100
    pygame.draw.line(SCREEN, (255, 0, 0), (start_x + 20, start_y + 20), (start_x + 80, start_y + 80), 5)
    pygame.draw.line(SCREEN, (255, 0, 0), (start_x + 80, start_y + 20), (start_x + 20, start_y + 80), 5)

def draw_O(row, col):
    center_x = col * 100 + 50
    center_y = row * 100 + 50
    pygame.draw.circle(SCREEN, (0, 0, 255), (center_x, center_y), 40, 5)

