import pygame
import math
import random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
object = pygame.image.load("chillguy.png")
object = pygame.transform.scale(object, (object.get_width()//10, object.get_height()//10))
flipped = pygame.transform.flip(object, True, False)
clock = pygame.time.Clock()

number = 100 #number of objects to be reused
objects = {}
for i in range(number):
    objects[i] = [-3000, height, random.choice([-1,1])] # x = -1000 and y = height so it will reset during the while True loop
    
speed = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))       
    
    for i in range(number):
        if objects[i][1] + object.get_height() < height:
            objects[i][1] += speed
        else:
            if objects[i][0] < -width or objects[i][0] > width:
                x = random.randint(0, width - object.get_width()) # generate a new x position within the domain 0 and width (minus the width of the object)
                y = -random.randint(100, 3000) # generate a new position above the screen (-negative because above the screen goes negative)
                objects[i] = [x,y, random.choice([-1,1])]
            else:
                if objects[i][2] == -1:
                    objects[i][0] -= speed
                else:
                    objects[i][0] += speed
    for i in range(number):
        if objects[i][2] == 1:
            window.blit(flipped if not objects[i][1] + object.get_height() < height else object, (objects[i][0], objects[i][1]))
        else:
            window.blit(object, (objects[i][0], objects[i][1]))
    pygame.display.flip()
    clock.tick(60)