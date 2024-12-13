# WRITE YOUR SOLUTION HERE:
import pygame
import random

pygame.init()

width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
window.fill((0,0,0))

max_width = width-robot.get_width()
max_height = height-robot.get_height()

for i in range(1000):
    window.blit(robot, (random.randint(0, max_width), random.randint(0, max_height)))

pygame.display.flip()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()