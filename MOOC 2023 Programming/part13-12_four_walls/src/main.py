# WRITE YOUR SOLUTION HERE:
import pygame


pygame.init()
width, height = 640, 480

window = pygame.display.set_mode((width, height))
object = pygame.image.load("chillguy.png")
object = pygame.transform.scale(object, (object.get_width()//10, object.get_height()//10))
flipped = pygame.transform.flip(object, True, False)
clock = pygame.time.Clock()

to_left = False
to_right = False
to_down = False
to_up = False

x = window.get_width()//2
y = window.get_height()//2
speed = 2

to_print = object
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False  
                
    if to_left:
        if x > 0:
            x -= speed
            to_print = object
    if to_right:
        if x < width-object.get_width():
            x += speed  
            to_print = flipped    
    if to_down:
        if y < height - object.get_width():
            y += speed
    if to_up:
        if y > 0:
            y -= speed     
    
    window.fill((0,0,0))
    window.blit(to_print, (x,y))
    pygame.display.flip()
    clock.tick(60)
            