# tile_mapClass- to use, import this module in your code and use the Tilemap class to create an instance.
import pygame
import random
import math


class GenericEntity(object):
    def __init__(self, x, y, speed, angle, size):
        self.x = x
        self.y = y
        self.sp = speed
        self.size = size
        self.an = angle

    def move(self):
        dy = self.sp * -1 * math.sin(math.radians(self.an))
        dx = self.sp * math.cos(math.radians(self.an))
        self.y -= dy
        self.x -= dx

    def checkCollision(self, x, y, width, height):
        pass

    def render(self):
        pass
