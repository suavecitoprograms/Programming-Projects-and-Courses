# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

width, height = 640, 480
window =  pygame.display.set_mode((width, height))
object_a = pygame.image.load("chillguy.png")
object_a = pygame.transform.scale(object_a, (object_a.get_width()//10, object_a.get_height()//10))
object_a_flipped = pygame.transform.flip(object_a, True, False)
object_b = pygame.image.load("blueguy.png")
object_b = pygame.transform.scale(object_b, (object_b.get_width()//6, object_b.get_height()//6))
object_b_flipped = pygame.transform.flip(object_b, True, False)
clock = pygame.time.Clock()

a_x = width - object_a.get_width() * 2
a_y = height // 2

b_x = object_b.get_width() * 2
b_y = height // 2

speed = 2
a_direction = object_a
b_direction = object_b_flipped

a_to_left = False
a_to_right = False
a_to_up = False
a_to_down = False

b_to_left = False
b_to_right = False
b_to_up = False
b_to_down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                a_to_left = True
            if event.key == pygame.K_RIGHT:
                a_to_right = True
            if event.key == pygame.K_UP:
                a_to_up = True
            if event.key == pygame.K_DOWN:
                a_to_down = True
            
            if event.key == pygame.K_a:
                b_to_left = True
            if event.key == pygame.K_d:
                b_to_right = True
            if event.key == pygame.K_w:
                b_to_up = True
            if event.key == pygame.K_s:
                b_to_down = True
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                a_to_left = False
            if event.key == pygame.K_RIGHT:
                a_to_right = False
            if event.key == pygame.K_UP:
                a_to_up = False
            if event.key == pygame.K_DOWN:
                a_to_down = False
            
            if event.key == pygame.K_a:
                b_to_left = False
            if event.key == pygame.K_d:
                b_to_right = False
            if event.key == pygame.K_w:
                b_to_up = False
            if event.key == pygame.K_s:
                b_to_down = False
    
    if a_to_left:
        if a_x > 0:
            a_x -= speed
            a_direction = object_a
    if a_to_right:
        if a_x + object_a.get_width() < width:
            a_x += speed
            a_direction = object_a_flipped
    if a_to_down:
        if a_y < height:
            a_y += speed
    if a_to_up:
        if a_y > 0:
            a_y -= speed
            
    if b_to_left:
        if b_x > 0:
            b_x -= speed
            b_direction = object_b
    if b_to_right:
        if b_x + object_b.get_width() < width:
            b_x += speed
            b_direction = object_b_flipped
    if b_to_down:
        if b_y < height:
            b_y += speed
    if b_to_up:
        if b_y > 0:
            b_y -= speed
            
    window.fill((0,0,0))
    window.blit(a_direction, (a_x,a_y))
    window.blit(b_direction, (b_x,b_y))
    pygame.display.flip()
    clock.tick(60)