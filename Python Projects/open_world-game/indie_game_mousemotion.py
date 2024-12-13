import pygame

pygame.init()
width, height = 750, 500
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

game_background = pygame.image.load("game_background.png")
game_background = pygame.transform.scale(game_background, (750,500))

character_front = pygame.image.load("sprite_front.png")
character_front = pygame.transform.scale(character_front, (31,49))
    
character_back = pygame.image.load("sprite_back.png")
character_back = pygame.transform.scale(character_back, (31,49))

character_left = pygame.image.load("sprite_left.png")
character_left = pygame.transform.scale(character_left, (31,49))

character_right = pygame.image.load("sprite_right.png")
character_right = pygame.transform.scale(character_right, (31,49))


character_x = width / 2
character_y = height / 2

direction = character_front

mouse_speed = 1

mouse_x = width / 2
mouse_y = height / 2

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            mouse_x = event.pos[0] - character_front.get_width() // 2
            mouse_y = event.pos[1] - character_front.get_height() // 2
            
    if character_x > mouse_x: # move left
        character_x -= mouse_speed
        direction = character_left
    if character_x < mouse_x: # move right
        character_x += mouse_speed
        direction = character_right
    if character_y > mouse_y: # move top
        character_y -= mouse_speed
        direction = character_back
    if character_y < mouse_y: # move bottom
        character_y += mouse_speed
        direction = character_front
    
    #window.blit(game_background, (0,0))
    window.fill((255,255,255))
    window.blit(direction, (character_x, character_y))
    pygame.display.flip()
    clock.tick(60)
                
    
    