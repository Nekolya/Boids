import random
import pygame
import time
import math

class Boid:
    def __init__(self, W, H):
        self.x = random.randint(20, W - 20)
        self.y = random.randint(20, H - 20)
        self.dx = random.randint(15, 20)/50*random.choice([-1, 1])
        self.dy = random.randint(15, 20)/50*random.choice([-1, 1])

        self.avoid_dx = 0
        self.avoid_dy = 0
        self.aligm_dx = self.dx
        self.aligm_dy = self.dy
        self.cohes_dx = 0
        self.cohes_dy = 0
        self.lim = 0.1

        self.rect = pygame.Rect(self.x - 15, self.y + 15, 55, 55)
        self.avoid_rect = pygame.Rect(self.x - 7, self.y + 7, 39, 39)
        self.co_rect = pygame.Rect(self.x-30, self.y+30, 85, 85)

        self.neighbors = 1;
        self.cohesion_x = self.x;
        self.cohesion_y = self.y;
        self.angle = math.atan(self.dy/self.dx)*180/math.pi


#    def change_a
    def update(self):
        if self.dy ==0:
            self.angle = 0
        else:
            self.angle = math.atan(self.dy / self.dx)*180/math.pi
            if self.dy > 0 and self.dx < 0:
                self.angle += 180
            elif self.dy > 0 and self.dx > 0:
                self.angle += 180

        self.neighbors = 0
        self.cohesion_x = 0
        self.cohesion_y = 0
        self.avoid_dx = self.dx
        self.avoid_dy = self.dy
        self.aligm_dx = self.dx
        self.aligm_dy = self.dy
        self.cohes_dx = 0
        self.cohes_dy = 0


    def d_lim(self, speed):
        lim = 1
        while speed > lim or speed < -lim:
            speed /= 1.2
        return speed

    def speed_limit(self):
        const = 0.16
        while abs(self.dx) > self.lim or abs(self.dy) > self.lim:
            self.dx /= 1.2
            self.dy /= 1.2
            """

            if self.dx > lim:
                self.dx -= const

            elif self.dx < -lim:
                self.dx += const

            if self.dy > lim:
                self.dy -= const

            elif self.dy < -lim:
                self.dy += const"""

    def walls(self, w, h):
        mode = 2
        if mode == 2:
            if self.x > w:
                self.dx = -22

            elif self.y > h:
                self.y = -22

            elif self.x < -22:
                self.x = w

            elif self.y < -22:
                self.y = h
        elif mode:
            const = 0.03
            if self.x > w:
                self.dx = -22

            elif self.x < -22:
                self.x = w

            elif self.y > h - 100:
                self.dy -= const

            elif self.y < 100:
                self.dy += const
        else:
            const = 0.4
            if self.x > w - 30:
                self.dx -= const

            elif self.y > h - 30:
                self.dy -= const

            elif self.x < 30:
                self.dx += const

            elif self.y < 30:
                self.dy += const

    def avoid(self, boid):
        if self.avoid_rect.colliderect(boid.avoid_rect):
            #print(self.x_center, self.y_center, 'collide with', boid.x_center, boid.y_center)
            const = 0.2
            if self.x_center > boid.x_center:
                self.avoid_dx += const
            else:
                self.avoid_dx -= const

            if self.y_center > boid.y_center:
                self.avoid_dy += const
            else:
                self.avoid_dy -= const

            #self.avoid_dx = self.d_lim(self.avoid_dx)
            #self.avoid_dy = self.d_lim(self.avoid_dy)

    def alignment_accel(self, boid):
        if self.rect.colliderect(boid.rect):
            #res_dx = self.dx + boid.dx
            #res_dy = self.dy + boid.dy
            const = 1

            self.aligm_dx = self.d_lim(boid.aligm_dx/const + self.aligm_dx)
            self.aligm_dy = self.d_lim(boid.aligm_dy/const + self.aligm_dy)

            boid.aligm_dx = self.d_lim(self.aligm_dx/const + boid.aligm_dx)
            boid.aligm_dy = self.d_lim(self.aligm_dy/const + boid.aligm_dy)

    def center_of_gravity(self, boid):
            self.cohesion_x += boid.x
            self.cohesion_y += boid.y

            self.neighbors += 1

    def cohesion(self):
        if self.neighbors > 3:
            x = self.cohesion_x/self.neighbors
            y = self.cohesion_y/self.neighbors

            dx = x - self.x
            dy = y - self.y

            const = 2.2
            self.cohes_dx = self.d_lim(dx / const)
            self.cohes_dy = self.d_lim(dy / const)

        else:
            self.dx *= 0.18
            self.dy *= 0.18





