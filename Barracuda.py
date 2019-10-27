from Boid import Boid
import random
import pygame

class Barracuda(Boid):
    def __init__(self, h, w):
        super().__init__(h, w)

        self.lim = 0.45

        self.x /= 2
        self.y /= 2

        self.hunt_dx = 0
        self.hunt_dy = 0

        self.x_center = self.x + 37
        self.y_center = self.y - 11

        self.rect = pygame.Rect(self.x-25, self.y+15, 125, 105)
        self.avoid_rect = pygame.Rect(self.x-17, self.y + 7, 110, 90)
        #self.co_rect = pygame.Rect(self.x-30, self.y+30, 85, 85)
        self.co_rect = pygame.Rect(self.x-25, self.y+25, 120, 120)

    def update(self):
        super().update()
        self.x_center = self.x + 37
        self.y_center = self.y - 11
        self.rect.x = self.x - 25
        self.rect.y = self.y + 15
        self.avoid_rect.x = self.x - 17
        self.avoid_rect.y = self.y + 7
        self.co_rect.x = self.x - 30
        self.co_rect.y = self.y + 30

        self.hunt_dx = 0
        self.hunt_dy = 0

    def walls(self, w, h):
        mode = 2
        if mode == 2:
            if self.x > w:
                self.dx = -77

            elif self.y > h:
                self.y = -77

            elif self.x < -77:
                self.x = w

            elif self.y < -77:
                self.y = h

    def move(self):

        self.cohesion()

        #print("%.3f" % self.dx, "%.3f" % self.avoid_dx, "%.3f" % self.aligm_dx, "%.3f" % self.cohes_dx, sep="\t")

        self.dx = (self.dx*5 + self.avoid_dx + self.aligm_dx/3 + self.cohes_dx/3 + self.hunt_dx)/2
        self.dy = (self.dy*5 + self.avoid_dy + self.aligm_dy/3 + self.cohes_dy/3 + self.hunt_dy)/2
        self.speed_limit()

        self.x += self.dx
        self.y += self.dy
        self.update()

    def hunt(self, clown):
        if self.avoid_rect.colliderect(clown.avoid_rect):
            x = clown.x - self.x
            y = clown.x - self.x
            cot = abs(x/y /8)
            tan = abs(y/x /8)
            if x > 0:
                self.hunt_dx += cot
            else:
                self.hunt_dx += -cot
            if y > 0:
                self.hunt_dy += tan
            else:
                self.hunt_dy += -tan