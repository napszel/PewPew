import pew

pew.init()
screen = pew.Pix()

matrix = []

def clear():
    i = 0
    while i < 8:
        next_row = [0, 0, 0, 0, 0, 0, 0, 0]
        matrix.append(next_row)
        i = i + 1

def update_screen():
    i = 0
    while i < 8:
        j = 0
        while j < 8:
            screen.pixel(i, j, matrix[i][j])
            j = j + 1
        i = i + 1

clear()

x = 3
y = 3
matrix[x][y] = 1

update_screen()
pew.show(screen)

old_pixel_color = 0
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
        if keys:
            pressing = True
    else:
        if not keys:
            pressing = False

    pew.show(screen)
    pew.tick(1/6)
 


pew.show(screen)

while True:
    keys = pew.keys()
    if not pressing:
        if keys & pew.K_UP and y > 0:
            matrix[x][y] = old_pixel_color
            old_pixel_color = screen.pixel(x, y-1)
            y -= 1
            matrix[x][y] = 3
            update_screen()
        elif keys & pew.K_DOWN and y < 7:
            matrix[x][y] = old_pixel_color
            old_pixel_color = screen.pixel(x, y+1)
            y += 1
            matrix[x][y] = 3
            update_screen()
        if keys & pew.K_LEFT and x > 0:
            matrix[x][y] = old_pixel_color
            old_pixel_color = screen.pixel(x-1, y)
            x -= 1
            matrix[x][y] = 3
            update_screen()
        elif keys & pew.K_RIGHT and x < 7:
            matrix[x][y] = old_pixel_color
            old_pixel_color = screen.pixel(x+1, y)
            x += 1
            matrix[x][y] = 3
            update_screen()
        if keys & pew.K_O:
            screen.pixel(x, y, screen.pixel(x, y)+1)
        if keys:
            pressing = True
    else:
        if not keys:
            pressing = False

    pew.show(screen)
    pew.tick(1/6)
