import pew

pew.init()

# constants
screen = pew.Pix()

off = 0
dim = 1
light = 2
bright = 3

start_x = 0  # character's start position x
start_y = 0  # character's start position y
start_brightness = dim

# global matrix of current pixel colors
matrix = []

# sets the whole matrix to off
def clear():
    global matrix
    matrix = []
    i = 0
    while i < 8:
        next_row = [off, off, off, off, off, off, off, off]
        matrix.append(next_row)
        i = i + 1

# updates the screen based on the current values in matrix
def update_screen():
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            screen.pixel(i, j, matrix[i][j])
            j = j + 1
        i = i + 1

# initialize
clear()
matrix[start_x][start_y] = start_brightness
update_screen()
pew.show(screen)

old_pixel_color = off  # always stores the brightness of the pixel I moved from
x = start_x  # always stores my current position x
y = start_y  # always stores my current position y

pressing = False

while True:
    keys = pew.keys()
    if not pressing:
        if keys & pew.K_UP and y > 0:
            matrix[x][y] = old_pixel_color
            old_pixel_color = matrix[x][y-1]
            y -= 1
            matrix[x][y] = 1
            update_screen()
        elif keys & pew.K_DOWN and y < 7:
            matrix[x][y] = old_pixel_color
            old_pixel_color = matrix[x][y+1]
            y += 1
            matrix[x][y] = 1
            update_screen()
        if keys & pew.K_LEFT and x > 0:
            matrix[x][y] = old_pixel_color
            old_pixel_color = matrix[x-1][y]
            x -= 1
            matrix[x][y] = 1
            update_screen()
        elif keys & pew.K_RIGHT and x < 7:
            matrix[x][y] = old_pixel_color
            old_pixel_color = matrix[x+1][y]
            x += 1
            matrix[x][y] = 1
            update_screen()
        if keys & pew.K_O:
            old_pixel_color = 1
            matrix[x][y] = 2
            update_screen()
        if keys & pew.K_X:
            clear()
            update_screen()
        if keys:
            pressing = True
    else:
        if not keys:
            pressing = False

    pew.show(screen)
    pew.tick(1/12)
