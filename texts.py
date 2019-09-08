import sys
import os
import time
import pew


def scroll(pix, dx=1):
    x = 0
    while True:
        for x in range(x, pix.width, dx):
            screen.box(0)
            screen.blit(pix, -x, 1)
            yield x
        x = -8


def change(pix, next_pix, x, dy):
    for y in range(1, 1 + 8 * dy, dy):
        screen.box(0)
        screen.blit(pix, -x, y)
        screen.blit(next_pix, 0, y - 7 * dy)
        yield


def hold_keys():
    global hold

    try:
        keys = pew.keys()
    except pew.GameOver:
        keys = 0
    if keys:
        hold = 0
    while pew.keys() and time.monotonic() - hold < 0.25:
        return 0
    hold = time.monotonic()
    return keys


def animate(entries):
    global user_exit
    selected = 0
    pix = pew.Pix.from_text(entries[selected])
    x = 0
    animation = scroll(pix)
    while True:
        keys = hold_keys()
        if keys & pew.K_X:
            user_exit = True
            return
        if keys & pew.K_UP:
            selected = (selected - 1) % len(entries)
            next_pix = pew.Pix.from_text(entries[selected])
            yield from change(pix, next_pix, x, 1)
            hold_keys()
            pix = next_pix
            animation = scroll(pix)
            keys = 0
        if keys & pew.K_DOWN:
            selected = (selected + 1) % len(entries)
            next_pix = pew.Pix.from_text(entries[selected])
            yield from change(pix, next_pix, x, -1)
            hold_keys()
            pix = next_pix
            animation = scroll(pix)
            keys = 0
        x = next(animation)
        yield selected
        yield selected


pew.init()
user_exit = False
while True:
    hold = 0
    screen = pew.Pix()
    texts = (
        "Hello",
        "COOOOL",
        "Are we there yet?",
        "CRAZY EX")

    m = animate(texts)
    
    while True:
        try:
            next(m)
        except StopIteration:
            break

        if user_exit:
            break

        pew.show(screen)
        pew.tick(1/24)

    if user_exit:
        break




