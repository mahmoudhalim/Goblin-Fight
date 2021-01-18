import pygame
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("First Game")
x = 250
y= 250
WIDTH = 500
HEIGHT = 500
run = True
vel = 10
isjump = False
jcount  = 10
while run:
    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and x >= vel:
        x -= vel
    if keys[pygame.K_RIGHT] and x < WIDTH - 50:
        x += vel
    if not isjump     :  
        if keys[pygame.K_UP] and y >= vel:
            y -= vel
        if keys[pygame.K_DOWN] and y < HEIGHT - 50 :
            y += vel
        if keys[pygame.K_SPACE]:
            isjump = True
    else:
        if jcount >= -10:
            if jcount >= 0:
                y -=  (jcount **2) *0.5
            if jcount < 0:
                y +=  (jcount **2) *0.5
            jcount -= 1
        else:
            isjump = False
            jcount = 10
        
        
    win.fill((0, 0, 0))
    pygame.draw.rect(win, (255, 0, 0), (x, y, 50, 50))
    pygame.display.update()
pygame.quit()
