# WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

x = 0
y = 0
velocity = 1

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    y += velocity
    if velocity > 0 and y + robot.get_height() >= height:
        velocity = -velocity
    if velocity < 0 and y <= 0:
        velocity = - velocity
    clock.tick(60)
    