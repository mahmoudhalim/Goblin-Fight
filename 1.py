import pygame
from pygame.constants import K_LEFT
pygame.init()

win = pygame.display.set_mode((500, 480))

pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

clock = pygame.time.Clock()

x = 50
y = 425
WIDTH = 64
HEIGHT = 64
run = True
vel = 10
isjump = False
jumpcount = 5
left = False
right = False
walkcount = 0

def redrawGameWindow():
    global walkcount
    win.blit(bg, (0,0))
    if walkcount +1 >27:
        walkcount=0
    if left:
        win.blit(walkLeft[walkcount//3], (x, y))
        walkcount += 1
    elif right:
        win.blit(walkRight[walkcount//3], (x, y))
        walkcount += 1
    else:
        win.blit(char, (x, y))
    pygame.display.update()
    

while run:
    clock.tick(27)

    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x > vel:
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < 500 - WIDTH - vel:
        x += vel
        left = False
        right = True
    else:
        left = False
        right = False
        walkcount = 0
    if not isjump:
        if keys[pygame.K_SPACE]:
            isjump = True
            left = False
            right = False
            walkcount = 0
    else:
        if jumpcount >= -5:
            if jumpcount >= 0:
                y -= (jumpcount ** 2)
            if jumpcount < 0:
                y += (jumpcount ** 2)
            jumpcount -= 1
        else:
            isjump = False
            jumpcount = 5
            
    redrawGameWindow()


pygame.quit()
