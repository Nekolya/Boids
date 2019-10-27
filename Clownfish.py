from Boid import Boid
import random
import pygame

class Clownfish(Boid):
    def __init__(self, h, w):
        super().__init__(h, w)

        self.lim = 0.1

        self.see_predator = 0
        self.panic = 0

        self.x_center = self.x + 13
        self.y_center = self.y - 13

        self.rect = pygame.Rect(self.x-15, self.y+15, 55, 55)
        self.avoid_rect = pygame.Rect(self.x-7, self.y + 7, 39, 39)
        #self.co_rect = pygame.Rect(self.x-30, self.y+30, 85, 85)
        self.co_rect = pygame.Rect(self.x-25, self.y+25, 75, 75)

        self.run_dx = 0
        self.run_dy = 0

        self.run_away_rect = pygame.Rect(self.x - 30, self.y + 30, 85, 85)

    def run_away(self, barracuda):
        if self.run_away_rect.colliderect(barracuda.avoid_rect):
            self.see_predator = 1
            self.panic = 1
            # print(self.x_center, self.y_center, 'collide with', boid.x_center, boid.y_center)
            mode = 1
            if mode:
                const = 0.9
                if self.x_center > barracuda.x_center:
                    self.run_dx += const
                else:
                    self.run_dx -= const

                if self.y_center > barracuda.y_center:
                    self.run_dy += const
                else:
                    self.run_dy -= const


    def update(self):
        super().update()
        self.x_center = self.x + 13
        self.y_center = self.y - 13
        self.rect.x = self.x - 15
        self.rect.y = self.y + 15
        self.avoid_rect.x = self.x - 7
        self.avoid_rect.y = self.y + 7
        self.co_rect.x = self.x - 25
        self.co_rect.y = self.y + 25
        self.run_away_rect.x = self.x + 30
        self.run_away_rect.y = self.y + 30

        self.see_predator = 0

        self.run_dx = 0
        self.run_dy = 0

        self.panic = 0

    def do_panic(self, clown):
        if self.rect.colliderect(clown.rect) and self.see_predator == 0 and clown.panic == 1:
            self.panic = 1
            self.dx = clown.dx
            self.dy = clown.dy
            """
            self.dx = clown.dx*4/5 + self.dx*1/5
            self.dy = clown.dy * 4/5 + self.dy * 1 / 5"""

    def move(self):
        if self.panic == 1:
            self.lim = 1.8
        else:
            self.lim = 0.6
        self.cohesion()
        #print("%.3f" % self.dx, "%.3f" % self.avoid_dx, "%.3f" % self.aligm_dx, "%.3f" % self.cohes_dx, sep="\t")
        """
        if self.panic:
            self.aligm_dx += self.run_dx/2
            self.aligm_dy += self.run_dy/2"""

        if self.panic:
            self.aligm_dx = self.dx
            self.aligm_dy = self.dy

        if self.see_predator:
            self.cohes_dx = self.dx
            self.cohes_dy = self.dy

        self.dx = (self.dx*5 + self.avoid_dx + self.aligm_dx/3 + self.cohes_dx/3 + self.run_dx)
        self.dy = (self.dy*5 + self.avoid_dy + self.aligm_dy/3 + self.cohes_dy/3 + self.run_dy)

        self.dx += self.run_dx
        self.dy += self.run_dy

        self.speed_limit()

        self.x += self.dx
        self.y += self.dy
        self.update()