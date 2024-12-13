# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
clock = pygame.time.Clock()

x1 = 0
x2 = 0
y = 20
velocity1 = 1
velocity2 = 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((0,0,0))
    window.blit(robot, (x1, y))
    window.blit(robot, (x2, y+robot.get_height()))
    pygame.display.flip()
    
    x1 += velocity1
    x2 += velocity2
    
    if x1 == 0 or x1 + robot.get_width() >= width:
        velocity1 = -velocity1
        
    if x2 == 0 or x2 + robot.get_width() >= width:
        velocity2 = -velocity2

        
    clock.tick(60)