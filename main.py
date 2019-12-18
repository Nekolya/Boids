# здесь подключаются модули
import pygame
from Clownfish import Clownfish
from Barracuda import Barracuda
from Boid import Boid
import time

# здесь определяются константы, классы и функции
FPS = 120
W = 1024
H = 600
lenght_clown = 180

lenght_barracuda = 5
clownfishes = []
barracudas = []
 
# здесь происходит инициация, создание объектов и др.
pygame.init()
win = pygame.display.set_mode((W, H))
pygame.display.set_icon(pygame.image.load("images/icon.png"))

pygame.display.set_caption("Coral fishes")

clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

mode = 0

if mode:
    FPS = 120
    lenght_clown = 180
    sprite = pygame.transform.scale(pygame.image.load("images/fish.png"), (8, 17))
    sprite2 = pygame.transform.scale(pygame.image.load("images/fish2.png"), (8, 17))
    sprite3 = pygame.transform.scale(pygame.image.load("images/fish3.png"), (8, 17))
    sprite4 = pygame.transform.scale(pygame.image.load("images/fish4.png"), (8, 17))
    sprite5 = pygame.transform.scale(pygame.image.load("images/fish5.png"), (8, 17))
    barracuda_sprite = pygame.transform.scale(pygame.image.load("images/barracuda2.png"), (9, 30))
else:
    lenght_clown = 150
    sprite = pygame.transform.scale(pygame.image.load("images/fish.png"), (10, 20))
    sprite2 = pygame.transform.scale(pygame.image.load("images/fish2.png"), (10, 20))
    sprite3 = pygame.transform.scale(pygame.image.load("images/fish3.png"), (10, 20))
    sprite4 = pygame.transform.scale(pygame.image.load("images/fish4.png"), (10, 20))
    sprite5 = pygame.transform.scale(pygame.image.load("images/fish5.png"), (10, 20))
    barracuda_sprite = pygame.transform.scale(pygame.image.load("images/barracuda2.png"), (12, 40))


for b in range(lenght_clown):
    clownfishes.append(Clownfish(W, H))

for b in range(lenght_barracuda):
    barracudas.append(Barracuda(W, H))
    
seaweed = pygame.transform.scale(pygame.image.load("images/seaweed.png"), (70, 310))
corals = pygame.transform.scale(pygame.image.load("images/coral_reef.png"), (W+20, 220))

#sprite = pygame.transform.scale(sprite, (13, 20))
#sprite = pygame.transform.scale(sprite, (15, 25))
#sprite = pygame.transform.scale(sprite, (13, 20))
#back = pygame.image.load("backwater.jpg")
#back = pygame.transform.scale(back, (W, H))
checker = 0

#time.sleep(20)

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

    for i in range(len(clownfishes)):
            counter += 1
            neighbours_counter = 0
            if counter % 5 == 0:
                win.blit(pygame.transform.rotate(sprite2, clownfishes[i].angle), (clownfishes[i].x, clownfishes[i].y))
            elif counter % 6 == 0:
                win.blit(pygame.transform.rotate(sprite3, clownfishes[i].angle), (clownfishes[i].x, clownfishes[i].y))
            elif counter % 4 == 0:
                win.blit(pygame.transform.rotate(sprite4, clownfishes[i].angle), (clownfishes[i].x, clownfishes[i].y))
            elif counter % 7 == 0:
                win.blit(pygame.transform.rotate(sprite5, clownfishes[i].angle), (clownfishes[i].x, clownfishes[i].y))
            else:
                win.blit(pygame.transform.rotate(sprite, clownfishes[i].angle), (clownfishes[i].x, clownfishes[i].y))
            if checker % 10 == 0:
                for b in barracudas:
                    clownfishes[i].run_away(b)
                    if (counter == 100):
                        b.hunt(clownfishes[i])
                if neighbours_counter < 7:
                    neighbours_counter += 1
                    for j in range(i+1, len(clownfishes)):
                            if clownfishes[j].co_rect.colliderect(clownfishes[i].co_rect):
                                clownfishes[j].alignment_accel(clownfishes[i])
                                clownfishes[j].avoid(clownfishes[i])
                                clownfishes[j].center_of_gravity(clownfishes[i])
                                clownfishes[j].do_panic(clownfishes[i])
            clownfishes[i].move()
            clownfishes[i].walls(W, H)

    for barracuda in barracudas:
            win.blit(pygame.transform.rotate(barracuda_sprite, barracuda.angle), (barracuda.x, barracuda.y))
            if checker % 10 == 0:
                for b in barracudas:
                    if b != barracuda:
                        #b.alignment_accel(barracuda)
                        b.avoid(barracuda)
                        #b.center_of_gravity(barracuda)

            barracuda.move()
            barracuda.walls(W, H)



    # --------
    # обновление экрана
    #win.blit(seaweed, (120, 300))
    pygame.display.update()
