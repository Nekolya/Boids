# здесь подключаются модули
import pygame
from Boid import Boid
import time
 
# здесь определяются константы, классы и функции
FPS = 120
W = 1300
H = 680
lenght = 120
boids = []
for b in range(lenght):
    boids.append(Boid())
 
# здесь происходит инициация, создание объектов и др.
pygame.init()
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Boids")

clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()
sprite = pygame.image.load("fish.png")
#sprite = pygame.transform.scale(sprite, (13, 20))
sprite = pygame.transform.scale(sprite, (15, 25))
back = pygame.image.load("backwater.jpg")
back = pygame.transform.scale(back, (W, H))
checker = 0


# главный цикл
while True:
 
    # задержка
    clock.tick(FPS)
    checker += 1
    if checker > 100:
        checker = 0
    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    win.fill((0, 140, 160))
    #win.blit(back, (0, 0))

    for boid in boids:
        win.blit(pygame.transform.rotate(sprite, boid.angle), (boid.x, boid.y))
        if checker % 10 == 0:
            for b in boids:
                if b != boid:
                    b.alignment_accel(boid)
                    b.avoid(boid)
                    b.center_of_gravity(boid)
        boid.move()
        boid.walls(W, H)
    # --------
    # обновление экрана
    pygame.display.update()
