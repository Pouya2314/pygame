#1-import library
import pygame
import sys

#2-Initialize pygame
pygame.init()

#3-Constants
width , height = 300,300
line_color = (164,172,75)
backgrand_color = (0,240,120)
line_width = 8
grid_size = 3
cell_size = width//grid_size
current_player = 'x'
Winner = None
Game_over = False
 
#4-Initialize the screen
screen = pygame.display.set_mode((width , height))
pygame.display.set_caption("tic_toc_toe")

#5-Initialize the game boardrange
board = [[' 'for _ in range(grid_size) for _ in range(grid_size)]]      #

#6-Function to draw the game board
def draw_board():
    for row in range(1,grid_size):
        pygame.draw.line(screen , line_color , line_width , (0 , row*cell_size) , (width , row*cell_size))
        pygame.draw.line(screen , line_color , line_width , (row*cell_size , 0) , (row*cell_size , height))

#7-Function to handle player clicls
def handle_click(row, col):
    global current_player, game_over

    if board[row][col] == '' and not game_over:
        board[row][col] = current_player
        if current_player == 'X':
            current_player = 'O'
        else:
            current_player = 'X'

# Function to check for a win
def check_win():
    global winner, game_over

    for row in range(GRID_SIZE):
        if board[row][0] == board[row][1] == board[row][2] != '':
            winner = board[row][0]
            game_over = True
            return

    for col in range(GRID_SIZE):
        if board[0][col] == board[1][col] == board[2][col] != '':
            winner = board[0][col]
            game_over = True
            return

    if board[0][0] == board[1][1] == board[2][2] != '':
        winner = board[0][0]
        game_over = True
        return

    if board[0][2] == board[1][1] == board[2][0] != '':
        winner = board[0][2]
        game_over = True
        return

# Game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x, y = pygame.mouse.get_pos()
            row, col = y // CELL_SIZE, x // CELL_SIZE
            handle_click(row, col)
            check_win()

    screen.fill(BG_COLOR)
    draw_board()

    # Draw X and O
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):
            if board[row][col] == 'X':
                x_center, y_center = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 3
                pygame.draw.line(screen, LINE_COLOR, (x_center - radius, y_center - radius),
                                 (x_center + radius, y_center + radius), LINE_WIDTH)
                pygame.draw.line(screen, LINE_COLOR, (x_center + radius, y_center - radius),
                                 (x_center - radius, y_center + radius), LINE_WIDTH)
            elif board[row][col] == 'O':
                x_center, y_center = col * CELL_SIZE + CELL_SIZE // 2, row * CELL_SIZE + CELL_SIZE // 2
                radius = CELL_SIZE // 3
                pygame.draw.circle(screen, LINE_COLOR, (x_center, y_center), radius, LINE_WIDTH)

    # Display the winner
    if winner:
        font = pygame.font.Font(None, 36)
        text = font.render(f"Player {winner} wins!", True, LINE_COLOR)
        text_rect = text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(text, text_rect)

    pygame.display.update()