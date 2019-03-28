# Jack Ponder
# ETGG 1801
# own project
# if console say "hit", the code has entered the hit function
# if console say "ur ded", the code has entered the if statement for health == 0
# if console say "OOF", the code has entered the if statement for health != 0

import pygame


class Healthbar(object):
    def __init__(self, x, y, width, height, total_health):
        self.x = x
        self.y = y
        self.dmg = 0
        self.wid = width
        self.height = height
        self.total = total_health
        self.healthC = (0, 255, 0)
        self.hurtC = (255, 0, 0)
        self.healthLeft = self.x + self.wid

    def draw(self, surface):
        ds = surface
        pygame.draw.rect(ds, self.healthC, (self.x, self.y, self.wid, self.height), 0)

    def hit(self, ping, surface, strength=1):
        ds = surface
        print("hit")
        self.dmg += ping  # input dmg done
        # must change to be total dmg
        self.healthLeft = self.total - (self.dmg * strength * .01)  # add damage
        if self.healthLeft <= 0:
            print("ur ded")
            self.healthLeft = 0
            self.dmg = 100 * strength ** -1
            # print(pix, dmg, lvl, s)  # number limiter check
            pygame.draw.rect(ds, self.hurtC, (self.healthLeft, self.y, (self.wid / self.total), self.height), 0)
            pygame.display.update()
            # return ded
        else:
            print("OOF")
            # print(pix, dmg, lvl, s)  # number limiter check
            pygame.draw.rect(ds, self.hurtC, (self.healthLeft, self.y, (self.wid / self.total), self.height), 0)
            pygame.display.update()

# def heal(self, ping, s=1):
#     print("heal")
#     self.dmg = self.dmg - ping
#     self.healthLeft -= (self.dmg * s)
#     if self.healthLeft >= self.wid:
#         print("full")
#         self.healthLeft = self.wid
#         self.dmg = 0
#         # print(pix, dmg, lvl, s)  # number limiter check
#         pygame.draw.rect(ds, self.healthC, ((self.healthLeft - 5), self.y, (self.wid / self.total), self.height), 0)
#         pygame.display.update()
#     else:
#         print("yay")
#         # print(pix, dmg, lvl, s)  # number limiter check
#         pygame.draw.rect(ds, self.healthC, ((self.healthLeft - 5), self.y, (self.wid / self.total), self.height), 0)
#         pygame.display.update()

# ping is heal or hit, s is level
