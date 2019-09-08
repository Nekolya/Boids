import random
import time


class Boid:
    def __init__(self):
        self.x = random.randint(10, 1100)
        self.y = random.randint(10, 600)
        self.dx = random.randint(10, 20)/50*random.choice([-1, 1])
        self.dy = random.randint(10, 20)/50*random.choice([-1, 1])

    def move(self):
        self.x += self.dx
        self.y += self.dy
#    def change_

    def teleport(self, w, h):
        if self.x > w:
            self.x = -22

        elif self.y > h:
            self.y = -22

        elif self.x < -22:
            self.x = w

        elif self.y < -22:
            self.y = h

