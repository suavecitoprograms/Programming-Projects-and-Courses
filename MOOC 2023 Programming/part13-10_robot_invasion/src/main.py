import pygame
import math
import random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
object = pygame.image.load("robot.png")
clock = pygame.time.Clock()

number = 20
speed = 2
info = {}

for i in range(number):
    info[i] = [-object.get_width(), -height + object.get_height(), random.choice([-1,1])]

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))
    for i in range(number):
        if info[i][1] + object.get_height() < height and info[i][0] in range(0, width - object.get_width()):
            info[i][1] += speed
        else:
            if info[i][0] < 0 or info[i][0] + object.get_width() > width:
                x = random.randint(0, width - object.get_width())
                y = -random.randint(100, 2000)
                info[i] = [x, y, random.choice([-1,1])]
            else:
                if info[i][2] == -1:
                    info[i][0] -= speed
                else:
                    info[i][0] += speed
    
    for i in range(number):
        window.blit(object, (info[i][0], info[i][1]))
    
    pygame.display.flip()
    clock.tick(60)