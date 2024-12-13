# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
width, height = 640, 480
window = pygame.display.set_mode((width, height))
object = pygame.image.load("cat.png")
object = pygame.transform.scale(object, (object.get_width()//5, object.get_height()//5))
object_flipped = pygame.transform.flip(object, True, False)
clock = pygame.time.Clock()

object_x = width // 2 
object_y = height // 2
target_x = width // 2 
target_y = height // 2

speed = 1
direction = object

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            target_x = event.pos[0] - object.get_width()//2
            target_y = event.pos[1] - object.get_height()//2
    
    if object_x > target_x:
        object_x -= speed
        direction = object_flipped
    if object_x < target_x:
        object_x += speed
        direction = object
    if object_y > target_y:
        object_y -= speed
    if object_y < target_y:
        object_y += speed
    
    window.fill((200,250,220))
    window.blit(direction, (object_x, object_y))
    pygame.display.flip()
    clock.tick(60)