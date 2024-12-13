# WRITE YOUR SOLUTION HERE:

import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

window.fill((0,0,0))
width = robot.get_width()
height = robot.get_height()

for i in range(10):
    for j in range(10):
        window.blit(robot, (20 + 10*i + width*j, 100 + 20*i))

pygame.display.flip()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()