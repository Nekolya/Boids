# здесь подключаются модули
import pygame
from Boid import Boid
import time
 
# здесь определяются константы, классы и функции
FPS = 200
W = 1024
H = 600
lenght = 120
boids = []
for b in range(lenght):
    boids.append(Boid(W, H))
 
# здесь происходит инициация, создание объектов и др.
pygame.init()
win = pygame.display.set_mode((W, H))
pygame.display.set_icon(pygame.image.load("icon.png"))

pygame.display.set_caption("Coral fishes")

clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()
sprite = pygame.image.load("fish.png")
sprite2 = pygame.image.load("fish2.png")
sprite3 = pygame.image.load("fish3.png")
sprite4 = pygame.image.load("fish4.png")
sprite5 = pygame.image.load("fish5.png")
seaweed = pygame.transform.scale(pygame.image.load("seaweed.png"), (70, 310))
corals = pygame.transform.scale(pygame.image.load("coral_reef.png"), (W+20, 220))

#sprite = pygame.transform.scale(sprite, (13, 20))
#sprite = pygame.transform.scale(sprite, (15, 25))
#sprite = pygame.transform.scale(sprite, (13, 20))
#back = pygame.image.load("backwater.jpg")
#back = pygame.transform.scale(back, (W, H))
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
    win.fill((40, 170, 210))
    pygame.draw.rect(win, (35, 165, 205), (0, 500, 1200, 600))
    pygame.draw.rect(win, (30, 160, 200), (0, 530, 1200, 600))
    pygame.draw.rect(win, (40, 155, 190), (0, 560, 1200, 600))
    pygame.draw.rect(win, (30, 150, 180), (0, 580, 1200, 600))
    win.blit(corals, (-20, 410))
    pygame.draw.circle(win, (55, 175, 220), (-100, - 600), 1000)
    pygame.draw.circle(win, (60, 185, 230), (-100, - 600), 800)
    pygame.draw.circle(win, (80, 215, 230), (-100, - 600), 700)
    pygame.draw.circle(win, (180, 240, 250), (-100, - 600), 630)


    counter = 0
    for boid in boids:
        counter += 1
        if counter % 5 == 0:
            win.blit(pygame.transform.rotate(sprite2, boid.angle), (boid.x, boid.y))
        elif counter % 6 == 0:
            win.blit(pygame.transform.rotate(sprite3, boid.angle), (boid.x, boid.y))
        elif counter % 4 == 0:
            win.blit(pygame.transform.rotate(sprite4, boid.angle), (boid.x, boid.y))
        elif counter % 7 == 0:
            win.blit(pygame.transform.rotate(sprite5, boid.angle), (boid.x, boid.y))
        else:
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
    #win.blit(seaweed, (120, 300))
    pygame.display.update()
