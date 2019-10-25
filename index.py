'''
Memory Puzzle
Qitian Lin
'''
import random, pygame, sys
from pygame.locals import *

# Set the over all structure.
# Define the global variables that will be used.
FPS = 30 # frame per second
REAVEALSPEED = 8

# the width and height of the wondow being used
WINDOWWIDTH = 640
WINDOWHEIGHT = 480

BOXSIZE = 40
GAPSIZE = 10
BOARDWIDTH = 10
BOARDHEIGHT = 7
assert (BOARDWIDTH * BOARDWIDTH) % 2 == 0
XMARGIN = int((WINDOWWIDTH - (BOARDWIDTH * (BOXSIZE + GAPSIZE))) / 2)
YMARGIN = int((WINDOWHEIGHT - (BOARDHEIGHT * (BOXSIZE + GAPSIZE))) / 2)

GRAY = (100, 100, 100)
NAVYBLYE = (60, 60, 100)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 128, 0)
PURPLE = (255, 0, 255)
CYAN = (0, 255, 255)

BGCOLOR = NAVYBLYE
LIGHTBGCOLOR = GRAY
BOXCOLOR = WHITE
HIGHLIGHTCOLOR = BLUE

DONUT = 'donut'
SQUARE = 'square'
DIAMOND = 'diamond'
LINES = 'lines'
OVAL = 'oval'


# tuple of shapes and all kinds of color
ALLCOLORS = (RED, GREEN, BLUE, YELLOW, ORANGE, PURPLE, CYAN)
ALLSHAPES = (DONUT, SQUARE, DIAMOND, LINES, OVAL)

# Define the game board such as the width height of the game board.
# and the weight and height of each icons.

# Define the global variables colors that will be used.

# Define the shape of the icon object such as square, diamond.

# Draw icons method.
def draw_icon():
    
    pass

# Draw Board method.
def draw_board():
    pass


def get_random_board_strucutre():
    # make a list of all possible icons and shuffle 
    icons = []
    for color in ALLCOLORS:
        for shape in ALLSHAPES:
            icons.append((shape, color))
    random.shuffle(icons) 
    
    # Double the size of icons
    icons_used = int(BOARDHEIGHT * BOARDWIDTH / 2)
    icons = icons[:icons_used] * 2
    random.shuffle(icons)

    # create the board
    board = []
    for x in range(BOARDWIDTH):
        column = []
        for y in range(BOARDHEIGHT):
            # append the first icon to the column and 
            # delete this icon
            column.append(icons[0])
            del icons[0]
        board.append(column)

    return board
    

# get reveal boxes using val which is true or false
def get_reveal_boxes(val):
    revealed_boxes = []
    for in range(BOARDWIDTH):
        revealed_boxes.append([val] * BOARDHEIGHT)
    return revealed_boxes

# Show start game animation.
def start_game_anime(board):
    # Randomly reveal the boxes 8 at a time
    covered_boxes = get_reveal_boxes(False)

    boxes = []
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            boxes.append((x, y))  
    random.shuffle(boxes)

    box_groups = split_into_groups(8, boxes)
    # TO DO 


def split_into_groups(size, list):
    # Splits a list into a list of lists, where the inner lists have 
    # most size number of items
    result = []
    for i in range(0, len(list), size):
        result.append(list[i: i + size])
    
    return result    


# Show end game animation.
def end_game_anime():
    pass

# Show win the game animation.
def win_game_anime():
    pass

# Box reveal animation.
def box_reveal_animation():
    pass

# Get the mouse click event.
def get_event():
    pass

# Handle the event that happened
def handle_event():
    pass
    
# main game funciton.
def main():
    global FPSCLOCK, DISPLAYSURF
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    mouse_x = 0
    mouse_y = 0
    pygame.display.set_caption('Memory Game')

    main_board = get_random_board_strucutre()
    revealed_boxes = get_reveal_boxes()

    # stores the (x, y) of the position of the box clicked
    first_selection = None

    DISPLAYSURF.fill(BGCOLOR)
    start_game_anime(main_board)
    

main()