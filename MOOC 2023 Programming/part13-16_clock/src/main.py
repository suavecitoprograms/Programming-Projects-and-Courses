# WRITE YOUR SOLUTION HERE:
import pygame
from datetime import *
import math

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))

def circle(color:tuple, radius:int):
    pygame.draw.circle(window, color, (width//2, height//2),radius)
    
def hand(proportion:float, radius:int, thickness:int): # radius is hypotenus
    x = width // 2 + math.cos(proportion * 2 * math.pi - math.pi/2) * radius - thickness / 2
    y = height // 2 + math.sin(proportion * 2 * math.pi - math.pi/2) * radius - thickness / 2
    pygame.draw.line(window, (0,0,255), (width//2 - thickness//2, height//2), (x,y), thickness)


game_font = pygame.font.SysFont("Arial", 24)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
    now = datetime.now()
    time = now.strftime("%H:%M:%S")
    time_info = time.split(":")
    
    now_seconds = int(time_info[2])
    now_minutes = int(time_info[1])
    now_hours = int(time_info[0])%12 #if under 12 if its divided the remainder is itself, if over the remainder is itself-12

    text = game_font.render(time, True, (255,255,255))
    
    window.fill((0,0,0))
    window.blit(text, (width//2 - text.get_width()//2, 0))
    
    #clock background
    circle((255,0,0), 180)
    circle((0,0,0), 177)
    circle((255,0,0), 5)
    
    #seconds line
    hand(now_seconds/60, 175, 1)
    #minutes line
    hand(now_minutes/60, 130, 3)
    #hours line
    hand(now_hours/12, 90, 5)
    
    #window name
    pygame.display.set_caption(time)
    pygame.display.flip()
    