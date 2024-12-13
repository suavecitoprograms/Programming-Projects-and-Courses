# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width,height))
object = pygame.image.load("red.png")
object = pygame.transform.scale(object, (object.get_width()//10, object.get_height()//10))
clock = pygame.time.Clock()

object_x = random.randint(0, width - object.get_width())
object_y = random.randint(0, height - object.get_height())

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = event.pos[0]
            mouse_y = event.pos[1]
            
            hit_x = mouse_x in range(object_x, object_x + object.get_width())
            hit_y = mouse_y in range(object_y, object_y + object.get_height())
            
            if hit_x and hit_y:
                object_x = random.randint(0, width - object.get_width())
                object_y = random.randint(0, height - object.get_height())
        
    
    window.fill((0,0,0))
    window.blit(object, (object_x, object_y))
    pygame.display.flip()
    clock.tick(60)