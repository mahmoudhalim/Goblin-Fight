import pygame
from pygame.constants import K_DOWN
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
x = 250
y= 250
run = True
vel = 5
while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= vel
    if keys[pygame.K_UP]:
        y -= vel
    if keys[pygame.K_RIGHT]:
        x += vel
    if keys[pygame.K_DOWN]:
        y += vel
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()
pygame.quit()
