import pygame
import time

pygame.init()

win = pygame.display.set_mode((500, 480))
pygame.display.set_caption("First Game")

walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load(
    'R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')]
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load(
    'L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')]
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')
FONT = pygame.font.SysFont("comicsans", 30, True)
bulletSound = pygame.mixer.Sound("data/bullet.wav")
bulletSound.set_volume(0.2)
hitSound = pygame.mixer.Sound("data/hit.wav")
hitSound.set_volume(0.1)

music = pygame.mixer.music.load("data/music.wav")
pygame.mixer.music.set_volume(0.5)
pygame.mixer.music.play(-1)
clock = pygame.time.Clock()
score = 0


class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.standing = True
        self.walkCount = 0
        self.jumpCount = 10
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0
        if not self.standing:
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x, self.y))
                self.walkCount += 1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            elif self.left:
                win.blit(walkLeft[0], (self.x, self.y))
            else:
                win.blit(char, (self.x, self.y))
        self.hitbox = (self.x + 17, self.y + 11, 29, 52)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def hit(self):
        self.x = 60
        self.y = 410
        self.walkCount = 0
        font = pygame.font.SysFont("comicsans", 100)
        text = font.render("-10", 1, (255, 0, 0))
        win.blit(text, (250 - (text.get_width()/2), 200))
        pygame.display.update()
        time.sleep(0.5)


class enemy(object):
    walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png'), pygame.image.load('R3E.png'), pygame.image.load('R4E.png'), pygame.image.load('R5E.png'), pygame.image.load(
        'R6E.png'), pygame.image.load('R7E.png'), pygame.image.load('R8E.png'), pygame.image.load('R9E.png'), pygame.image.load('R10E.png'), pygame.image.load('R11E.png')]
    walkLeft = [pygame.image.load('L1E.png'), pygame.image.load('L2E.png'), pygame.image.load('L3E.png'), pygame.image.load('L4E.png'), pygame.image.load('L5E.png'), pygame.image.load(
        'L6E.png'), pygame.image.load('L7E.png'), pygame.image.load('L8E.png'), pygame.image.load('L9E.png'), pygame.image.load('L10E.png'), pygame.image.load('L11E.png')]

    def __init__(self, x, y, width, height, end):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.end = end
        self.path = [self.x, self.end]
        self.walkcount = 0
        self.vel = 3
        self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        self.health = 10
        self.visible = True

    def draw(self, win):
        self.move()
        if self.visible:
            if self.walkcount + 1 >= 33:
                self.walkcount = 0
            if self.vel > 0:
                win.blit(self.walkRight[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
            else:
                win.blit(self.walkLeft[self.walkcount//3], (self.x, self.y))
                self.walkcount += 1
            pygame.draw.rect(win, (255, 255, 255),
                             (self.hitbox[0] - 5, self.hitbox[1] - 10, 40, 5))
            pygame.draw.rect(
                win, (255, 0, 0), (self.hitbox[0] - 5, self.hitbox[1] - 10, self.health*4, 5))

            self.hitbox = (self.x + 17, self.y + 2, 31, 57)
        # pygame.draw.rect(win, (255, 0, 0), self.hitbox, 2)

    def move(self):
        if self.vel > 0:
            if self.x + self.vel < self.path[1]:
                self.x += self.vel
            else:
                self.vel = -1 * self.vel
                self.walkcount = 0
                self.x += self.vel
        else:
            if self.x - self.vel > self.path[0]:
                self.x += self.vel
            else:
                self.vel = -1 * self.vel
                self.walkcount = 0
                self.x += self.vel

    def hit(self):
        hitSound.play()
        if self.health > 0:
            self.health -= 1
        else:
            self.visible = False


class projectile(object):
    def __init__(self, x, y, color, radius, dir):
        self.x = x
        self.y = y
        self.color = color
        self.radius = radius
        self.dir = dir
        self.vel = 7*self.dir

    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


def redrawGameWindow():
    win.blit(bg, (0, 0))
    text = FONT.render("0" * (6 - len(str(score))) + str(score), 1, (0, 0, 0))
    win.blit(text, (390, 10))

    man.draw(win)
    goblin.draw(win)
    for bullet in bullets:
        bullet.draw(win)
    pygame.display.update()


# mainloop
man = player(200, 410, 64, 64)
goblin = enemy(100, 416, 64, 64, 450)
shootLoop = 0
bullets = []
run = True


def is_hit(bullet: projectile) -> bool:
    if bullet.y - bullet.radius < goblin.hitbox[1] + goblin.hitbox[3] and bullet.y + bullet.radius > goblin.hitbox[1]:
        if bullet.x + bullet.radius > goblin.hitbox[0] and bullet.x - bullet.radius < goblin.hitbox[0] + goblin.hitbox[2]:
            return True
    return False


def is_collide(man: player) -> bool:
    if man.hitbox[1] < goblin.hitbox[1] + goblin.hitbox[3] and man.hitbox[1] + man.hitbox[3] > goblin.hitbox[1]:
        if man.hitbox[0] + man.hitbox[2] > goblin.hitbox[0] and man.hitbox[0] < goblin.hitbox[0] + goblin.hitbox[2]:
            return True
    return False


while run:
    clock.tick(27)
    if shootLoop > 0:
        shootLoop += 1
    if shootLoop > 3:
        shootLoop = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    if is_collide(man):
        man.hit()
        score -= 5

    for bullet in bullets:
        if is_hit(bullet):
            goblin.hit()
            score += 10
            bullets.remove(bullet)
        if bullet.x < 500 and bullet.x > 0:
            bullet.x += bullet.vel
        else:
            bullets.remove(bullet)

    keys = pygame.key.get_pressed()

    if keys[pygame.K_SPACE] and shootLoop == 0:
        if len(bullets) < 7:
            bulletSound.play()
            bullets.append(projectile((round(man.x + man.width//2)),
                                      (round(man.y + man.height//2)),
                                      (0, 0, 0),
                                      5,
                                      1 if man.right else -1))
        shootLoop = 1
    if keys[pygame.K_LEFT] and man.x > man.vel:
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < 500 - man.width - man.vel:
        man.x += man.vel
        man.right = True
        man.left = False
        man.standing = False
    else:
        man.standing = True
        man.walkCount = 0

    if not(man.isJump):
        if keys[pygame.K_UP]:
            man.isJump = True
            man.right = False
            man.left = False
            man.walkCount = 0
    else:
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            man.y -= (man.jumpCount ** 2) * 0.5 * neg
            man.jumpCount -= 1
        else:
            man.isJump = False
            man.jumpCount = 10

    redrawGameWindow()

pygame.quit()
