# WRITE YOUR SOLUTION HERE:

import pygame
import random

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")
rock = pygame.image.load("rock.png")
clock = pygame.time.Clock()

number = 5
speed = 5
rock_speed = 2
info = {}

robot_x = width // 2 + robot.get_width()//2
robot_y = height - robot.get_height()

to_right = False
to_left = False

def new_position(i:int):
    x = random.randint(0, width - rock.get_width())
    y = -(random.randint(10,1000) + i*100 )
    info[i] = [x,y]

for i in range(number):
    new_position(i)
    
#default number of points to 0        
points = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
    #background
    window.fill((0,0,0))
    
    #handle falling objects
    for i in range(number):
        touch_x = info[i][0] + rock.get_width()//2 in range(robot_x, robot_x + robot.get_width())
        touch_y = info[i][1] + rock.get_height() in range(robot_y, robot_y + robot.get_height())
        
        if touch_x and touch_y:
            new_position(i)
            points += 1
            
        if info[i][1] >= height - rock.get_height():
            new_position(i)
            points = 0
        else:
            info[i][1] += rock_speed
    #print falling objects
    for i in range(number):
        window.blit(rock, (info[i][0], info[i][1]))
    
    #game texts
    game_font = pygame.font.SysFont("Arial", 24)
    text = game_font.render(f"Points: {points}", True, (202, 252, 190))
    window.blit(text, (width//2 - text.get_width()//2, text.get_height()//2))
    
    #handle robot movement
    if to_right:
        if robot_x <= width - robot.get_width():
            robot_x += speed
    if to_left:
        if robot_x >= 0:
            robot_x -= speed       
    window.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    clock.tick(60)
    
    
