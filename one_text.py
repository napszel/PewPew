import pew

text = "Hello"

pew.init()
while True:
    screen = pew.Pix()

    text = pew.Pix.from_text(text)
    for dx in range(-8, text.width):
        screen.blit(text, -dx, 1)
        pew.show(screen)
        pew.tick(1/12)

