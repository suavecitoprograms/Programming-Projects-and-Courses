# # WRITE YOUR SOLUTION HERE:
import pygame
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

clock = pygame.time.Clock()

x = 0
y = 0
velocity = 7
direction = True # true is horizontal movement, false is vertical

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((0,0,0))
    window.blit(robot, (x,y))
    pygame.display.flip()
    
    if direction:
        x += velocity
        if velocity > 0 and x + robot.get_width() >= width:
            direction = False
        if velocity < 0 and x <= 0:
            direction = False
        
    else:
        y += velocity
        if velocity > 0 and y + robot.get_height() >= height:
            direction = True
            velocity = -velocity
        if velocity < 0 and y <= 0:
            direction = True
            velocity = -velocity
        
    clock.tick(60)