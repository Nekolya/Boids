# здесь подключаются модули
import random
import pygame
from Clownfish import Clownfish
from Barracuda import Barracuda
from Boid import Boid
import time

#random.seed(4)
# здесь определяются константы, классы и функции
FPS = 120
W = 1024
H = 600
lenght_clown = 120

lenght_barracuda = 0
clownfishes = []
barracudas = []

# здесь происходит инициация, создание объектов и др.
pygame.init()
win = pygame.display.set_mode((W+240, H))
pygame.display.set_icon(pygame.image.load("images/icon.png"))

font = pygame.font.Font('images/14235.otf', 24)

pygame.display.set_caption("Coral fishes")

clock = pygame.time.Clock()

# если надо до цикла отобразить объекты на экране
pygame.display.update()

mode = 1
add_sprite = pygame.image.load("images/add.png")
add_barac = pygame.image.load("images/barracudaButt.png")
add_coral = pygame.transform.scale(pygame.image.load("images/f.png"), (40, 30))
kill = pygame.image.load("images/kill.png")
quit_sprite = pygame.image.load("images/quit.png")

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
many_flag = 0
#time.sleep(20)
seed_counter = 0
# главный цикл
while True:
    """
    seed_counter += 1
    if seed_counter == 150:
        seed_counter = 0
        print( 'x = ','%.2f' % clownfishes[0].x, 'y = ', '%.2f' % clownfishes[0].y)"""
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
    pygame.draw.rect(win, (255, 255, 255), (1024, 0, 1300, 600))
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
                    if counter == 100:
                        b.hunt(clownfishes[i])

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
                        b.avoid(barracuda)

            barracuda.move()
            barracuda.walls(W, H)

    pygame.draw.rect(win, (255, 255, 255), (1024, 0, 100, 1024))
    pygame.draw.rect(win, (230, 100, 100), (1024, 0, 5, 600))

    win.blit(add_sprite, (1045, 100))
    win.blit(add_coral, (1170, 103))

    win.blit(add_sprite, (1045, 170))
    win.blit(add_barac, (1170, 179))

    win.blit(kill, (1045, 270))
    win.blit(add_coral, (1170, 273))

    win.blit(kill, (1045, 340))
    win.blit(add_barac, (1170, 349))

    win.blit(quit_sprite, (1125, 15))

    ev = pygame.event.get()

    many = font.render("Too many fishes!", 1, (30, 0, 0))
    if many_flag:
        many_flag -= 1
        win.blit(many, (1040, 530))

    # proceed events
    for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            add1 = pygame.Rect(1045, 100, 117, 34)
            add2 = pygame.Rect(1045, 170, 117, 34)
            quit_b = pygame.Rect(1125, 15, 117, 34)

            kill1 = pygame.Rect(1045, 270, 117, 34)
            kill2 = pygame.Rect(1045, 340, 117, 34)

            if add1.collidepoint(pos):
                if len(clownfishes) > 219:
                    many_flag = 150
                else:
                    clownfishes.append(Clownfish(W, H))

            if add2.collidepoint(pos):
                if len(barracudas) > 9:
                    many_flag = 150
                else:
                    barracudas.append(Barracuda(W, H))

            if quit_b.collidepoint(pos):
                quit()

            if kill1.collidepoint(pos):
                if len(clownfishes) > 0:
                    clownfishes.pop()

            if kill2.collidepoint(pos):
                if len(barracudas) > 0:
                    barracudas.pop()

    clown_counter = font.render("Clownfishes: " + str(len(clownfishes)), 1, (180, 0, 0))
    barracuda_counter = font.render("Barracudas: " + str(len(barracudas)), 1, (180, 0, 0))
    win.blit(clown_counter, (1045, 440))
    win.blit(barracuda_counter, (1045, 480))

    pygame.display.update()
