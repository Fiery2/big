# title

# imports
import pygame
import random
import math
import time

# setup
pygame.init()
# variables
ds = pygame.display.set_mode((800, 600))


# classes

# functions
def clear():
    """sets screen to background"""
    ds.fill((0, 0, 0))


def distance(x1, y1, x2, y2):
    """compute the distance"""
    dx = x1 - x2
    dy = y1 - y2
    dist = (dx ** 2 + dy ** 2) ** 0.5
    return dist


def update():
    """update the display"""
    pygame.display.update()


# main code
while True:
    pygame.event.pump()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_ESCAPE]:
        break

    clear()

    update()
pygame.display.quit()
