# WRITE YOUR SOLUTION HERE:
import pygame
import math
import random

pygame.init()

width, height = 640, 480

window = pygame.display.set_mode((width, height))
ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()

x = random.randint(0, width - ball.get_width()//2)
y = random.randint(0, height - ball.get_height()//2)
speed = 3
x_velocity = random.choice([speed,-speed])
y_velocity = random.choice([speed,-speed])


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    window.fill((40,201,120))
    
    x += x_velocity 
    y += y_velocity
    
    if x <= 0 or x >= width - ball.get_width():
        x_velocity = -x_velocity
        
    if y <= 0 or y >= height - ball.get_height():
        y_velocity = -y_velocity
        
    window.blit(ball, (x,y))
    pygame.display.flip()
    
    clock.tick(60)

