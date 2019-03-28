# Jack Ponder
# ETGG 1801
# Section 51
# Lab 8

# imports
import pygame
import random
import math
import time

# setup
pygame.init()
# variables
ds = pygame.display.set_mode((800, 600))
num_stars = 500
tank_x = 400
meteor = pygame.image.load("meteor1.png")  #
meteor2 = pygame.image.load("meteor2.png")  #
meteor3 = pygame.image.load("meteor3.png")  #
game_end = pygame.image.load("boom.png")
font = pygame.font.SysFont("Gill Sans", 25)
font2 = pygame.font.SysFont("arial", 50)
font3 = pygame.font.SysFont("arial", 30)
bullet_list = []
metero_list = []
star_list = []
cooldown = 0
bullet_num = 10
boom = 10000
explosion = pygame.mixer.Sound("Explosion+3.wav")
pew = pygame.mixer.Sound("pew.wav")
sad = pygame.mixer.Sound("Sad_Trombone.wav")
pygame.mixer.music.load("Megalovania.ogg")
pygame.mixer.music.set_volume(.1)
pygame.mixer.music.play()


# classes
class Bullet(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.angle = 90
        self.speed = 0.2
        self.rad = 4

    def move(self):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = -1 * self.speed * math.sin(math.radians(self.angle))
        self.x += dx
        self.y += dy

    def draw(self):
        pygame.draw.circle(ds, (255, 0, 0), (int(self.x), int(self.y)), self.rad, 0)

    def coll(self, ob):
        D = distance(self.x, self.y, ob.x, ob.y)
        return D <= ob.rad + self.rad


class Asteroid(object):
    def __init__(self):
        self.x = random.randint(0, 710)
        self.y = 0
        self.angle = 270
        self.speed = 0.1
        self.pix = random.randint(1, 3)
        self.rad = 80

    def move(self):
        dx = self.speed * math.cos(math.radians(self.angle))
        dy = -1 * self.speed * math.sin(math.radians(self.angle))
        self.x += dx
        self.y += dy

    def draw1(self):

        if self.pix == 1:
            ds.blit(meteor, (self.x, self.y))
        elif self.pix == 2:
            ds.blit(meteor2, (self.x, self.y))
        else:
            ds.blit(meteor3, (self.x, self.y))


# functions
def star(x, y):
    pygame.draw.circle(ds, (240, 240, 240), (x, y), random.randint(1, 3), 0)


def clear():
    """sets screen to background"""
    ds.fill((0, 0, 0))
    for i in range(0, num_stars):
        point = star_list[i]
        x = point[0]
        y = point[1]
        star(x, y)
    # ground
    pygame.draw.rect(ds, (0, 120, 0), (0, 500, 800, 100), 0)


def update():
    """update the display"""
    pygame.display.update()


def tank(x):
    pygame.draw.polygon(ds, (255, 128, 0), ((x, 490), (x + 5, 500), (x - 5, 500)), 0)


def distance(x1, y1, x2, y2):
    """compute the distance"""
    dx = x1 - x2
    dy = y1 - y2
    dist = (dx ** 2 + dy ** 2) ** 0.5
    return dist


def HealtH(thing, eat):
    textSurf = font.render(thing, True, (255, 0, 255), (0, 120, 0))
    ds.blit(textSurf, (0, 575))
    textSurf2 = font.render(str(eat), True, (255, 0, 255), (0, 120, 0))
    ds.blit(textSurf2, (125, 575))


def current_items():
    textSurf = font.render("Bullets:" + str(len(bullet_list)), True, (255, 0, 255))
    ds.blit(textSurf, (0, 0))
    textSurf2 = font.render("Asteroids:" + str(len(metero_list)), True, (255, 0, 255))
    ds.blit(textSurf2, (100, 0))


def tim():
    textSurf = font.render("Time Survived:", True, (255, 0, 255), (0, 120, 0))
    ds.blit(textSurf, (530, 575))
    textSurf2 = font.render(str(times) + " seconds", True, (255, 0, 255), (0, 120, 0))
    ds.blit(textSurf2, (695, 575))


def game_over():
    ds.fill((0, 0, 0))
    ds.blit(game_end, (0, 0))
    ds.blit(meteor3, (0, 0))
    ds.blit(meteor2, (710, 0))
    ds.blit(meteor, (355, 160))
    textSurf = font2.render("Game Over", False, (255, 0, 0), (0, 0, 0))
    ds.blit(textSurf, (300, 250))
    textSurf2 = font3.render("Score: ", False, (255, 0, 0), (0, 0, 0))
    ds.blit(textSurf2, (340, 300))
    textSurf3 = font3.render(str(times), False, (255, 0, 0), (0, 0, 0))
    ds.blit(textSurf3, (450, 300))
    sad.play(1, 4000)
    update()
    pygame.time.wait(5000)


# list creations
for i in range(0, num_stars):
    star_list.append((random.randint(0, 799), random.randint(0, 599)))
# main code
while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    times = int(pygame.time.get_ticks() / 1000)
    if boom <= 0:
        break
    if keys[pygame.K_ESCAPE]:
        pygame.display.quit()
    if keys[pygame.K_LEFT]:
        # move left
        tank_x -= 1
        if tank_x <= 0:
            tank_x = 0
    if keys[pygame.K_RIGHT]:
        # move right
        tank_x += 1
        if tank_x >= 799:
            tank_x = 799

    # Fire
    if keys[pygame.K_SPACE]:

        if cooldown == 0:
            pew.play()
            bullet_list.append(Bullet(tank_x, 490))
            cooldown = 250
    if cooldown != 0:
        cooldown -= 1
    # draw
    # background
    clear()
    # tank
    tank(tank_x)



    # use this for collision
    # bullet Print
    for bullet in bullet_list:
        bullet.move()
        bullet.draw()
    bulllets_remove = []
    for bullet in bullet_list:
        if bullet.y < 0:
            bulllets_remove.append(bullet)
    for bullet in bulllets_remove:
        bullet_list.remove(bullet)
    # asteroids

    aster = random.randint(1, 500)

    if aster == 1:
        metero_list.append(Asteroid())

    for metero in metero_list:
        metero.move()
        metero.draw1()

    metero_remove = []
    for metero in metero_list:
        if metero.y > 445:
            explosion.play(1, 1717)
            metero_remove.append(metero)
            boom -= random.randint(23, 45)
    for metero in metero_remove:
        metero_list.remove(metero)
    for bullet in bullet_list:
        for metero in metero_list:
            if bullet.coll(metero):
                explosion.play(1, 1717)
                bullet_list.remove(bullet)
                metero_list.remove(metero)
    HealtH("Population", boom)
    current_items()
    tim()
    update()
times = int(pygame.time.get_ticks() / 1000)
pygame.mixer.music.stop()
game_over()
pygame.display.quit()
