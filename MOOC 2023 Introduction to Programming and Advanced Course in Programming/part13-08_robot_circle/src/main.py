# WRITE YOUR SOLUTION HERE:

import pygame
import math

pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()
angle = 0
radius = 120

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    window.fill((0,0,0))
    
    for i in range(10):
        x = width/2 + math.cos(angle + i *(2*math.pi/10)) * radius - robot.get_width()/2
        y = height/2 + math.sin(angle + i *(2*math.pi/10)) * radius - robot.get_height()/2
        window.blit(robot, (x,y))
    
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    angle += 0.01
    clock.tick(60)