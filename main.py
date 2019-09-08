# здесь подключаются модули
import pygame
from Boid import Boid
 
# здесь определяются константы, классы и функции
FPS = 100
W = 1200
H = 640
boids = []
for b in range(100):
    boids.append(Boid())
 
# здесь происходит инициация, создание объектов и др.
pygame.init()
win = pygame.display.set_mode((W, H))
pygame.display.set_caption("Boids")

clock = pygame.time.Clock()
 
# если надо до цикла отобразить объекты на экране
pygame.display.update()
sprite = pygame.image.load("img.png")

# главный цикл
while True:
 
    # задержка
    clock.tick(FPS)

    # цикл обработки событий
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
    win.fill((0, 0, 0))
    # --------
    # изменение объектов и многое др.
    for boid in boids:
        win.blit(sprite, (boid.x, boid.y))
        boid.move()
        boid.teleport(W, H)
    # --------
 
    # обновление экрана
    pygame.display.update()
