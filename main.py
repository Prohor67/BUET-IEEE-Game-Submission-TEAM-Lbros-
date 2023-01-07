import pygame, sys
from Menu import Button
from pygame.locals import *
from pygame import mixer


pygame.init()


SCREEN = pygame.display.set_mode((300, 300))
pygame.display.set_caption("Menu")

BG = pygame.image.load("F:\WORK\PYTHON\Project Game\Project/Background.png")


screen_height = 300
screen_width = 300
line_width = 6
screen = pygame.display.set_mode((screen_width, screen_height))
# define colours
red = (237, 179, 19)
green = (0, 255, 0)
blue = (255, 255, 255)
black = (0, 0, 0)
# define font
font = pygame.font.SysFont(None, 40)

# define variables
clicked = False
player = 1
pos = (0, 0)
markers = []
game_over = False
winner = 0

# setup a rectangle for "Play Again" Option
again_rect = Rect(screen_width // 2 - 80, screen_height // 2, 160, 50)

# create empty 3 x 3 list to represent the grid
for x in range(3):
    row = [0] * 3
    markers.append(row)


def draw_board():
    bg = (6, 0, 74)
    grid = (250, 250, 250)
    screen.fill(bg)
    for x in range(1, 3):
        pygame.draw.line(screen, grid, (0, 100 * x), (screen_width, 100 * x), line_width)
        pygame.draw.line(screen, grid, (100 * x, 0), (100 * x, screen_height), line_width)


def draw_markers():
    x_pos = 0
    for x in markers:
        y_pos = 0
        for y in x:
            if y == 1:
                pygame.draw.line(screen, red, (x_pos * 100 + 15, y_pos * 100 + 15),
                                 (x_pos * 100 + 85, y_pos * 100 + 85), line_width)
                pygame.draw.line(screen, red, (x_pos * 100 + 85, y_pos * 100 + 15),
                                 (x_pos * 100 + 15, y_pos * 100 + 85), line_width)
            if y == -1:
                pygame.draw.circle(screen, green, (x_pos * 100 + 50, y_pos * 100 + 50), 38, line_width)
            y_pos += 1
        x_pos += 1


def check_game_over():
    global game_over

    global winner

    x_pos = 0
    for x in markers:
        # check columns
        if sum(x) == 3:
            winner = 1
            game_over = True
        if sum(x) == -3:
            winner = 2
            game_over = True
        # check rows
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == 3:
            winner = 1
            game_over = True
        if markers[0][x_pos] + markers[1][x_pos] + markers[2][x_pos] == -3:
            winner = 2
            game_over = True
        x_pos += 1

    # check cross
    if markers[0][0] + markers[1][1] + markers[2][2] == 3 or markers[2][0] + markers[1][1] + markers[0][2] == 3:
        winner = 1
        game_over = True
    if markers[0][0] + markers[1][1] + markers[2][2] == -3 or markers[2][0] + markers[1][1] + markers[0][2] == -3:
        winner = 2
        game_over = True

    # check for tie
    if game_over == False:
        tie = True
        for row in markers:
            for i in row:
                if i == 0:
                    tie = False
        # if it is a tie, then call game over and set winner to 0 (no one)
        if tie == True:
            game_over = True
            winner = 0



def draw_game_over(winner):
    if winner != 0:
        end_text = "Player " + str(winner) + " lose!"
    elif winner == 0:
        end_text = "You have tied!"

    end_img = font.render(end_text, True, blue)
    pygame.draw.rect(screen, black, (screen_width // 2 - 100, screen_height // 2 - 60, 200, 50))
    screen.blit(end_img, (screen_width // 2 - 100, screen_height // 2 - 50))

    again_text = 'Play Again?'
    again_img = font.render(again_text, True, blue)
    pygame.draw.rect(screen, black, again_rect)
    screen.blit(again_img, (screen_width // 2 - 80, screen_height // 2 + 10))


def get_font(size):  # Returns Press-Start-2P in the desired size
    return pygame.font.Font("F:\WORK\PYTHON\Project Game\Project/font.ttf", size)



def play():


    pygame.init()

    screen_height = 300
    screen_width = 300
    line_width = 6
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption('Tic Tac Toe')
    global game_over
    global clicked
    global markers
    global player
    global winner

    run = True
    while run:

        # draw board and markers first
        draw_board()
        draw_markers()

        # handle events
        for event in pygame.event.get():
            # handle game exit
            if event.type == pygame.QUIT:
                run = False
            # run new game
            if game_over == False:
                # check for mouseclick
                if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                    clicked = True
                    click = mixer.Sound('Sound1.mp3')
                    click.play()
                if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                    clicked = False
                    pos = pygame.mouse.get_pos()
                    cell_x = pos[0] // 100
                    cell_y = pos[1] // 100
                    if markers[cell_x][cell_y] == 0:
                        markers[cell_x][cell_y] = player
                        player *= -1
                        check_game_over()

        # check if game has been won
        if game_over == True:
            draw_game_over(winner)
            # check for mouseclick to see if we clicked on Play Again
            if event.type == pygame.MOUSEBUTTONDOWN and clicked == False:
                clicked = True
            if event.type == pygame.MOUSEBUTTONUP and clicked == True:
                clicked = False
                pos = pygame.mouse.get_pos()
                if again_rect.collidepoint(pos):
                    # reset variables
                    game_over = False
                    player = 1
                    pos = (0, 0)
                    markers = []
                    winner = 0
                    # create empty 3 x 3 list to represent the grid
                    for x in range(3):
                        row = [0] * 3
                        markers.append(row)

        # update display
        pygame.display.update()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(20).render("MAIN MENU", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(150, 50))

        PLAY_BUTTON = Button(image=None,pos=(150, 150),text_input="PLAY", font=get_font(15), base_color="#d7fcd4", hovering_color="White")

        QUIT_BUTTON = Button(image=None,pos=(150, 250),text_input="QUIT", font=get_font(15), base_color="#d7fcd4", hovering_color="White")

        SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON,QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(SCREEN)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    play()

                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()