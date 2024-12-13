import pygame

pygame.init()
width, height = 750, 500
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
scale_x = 108 / 2.7
scale_y = 173 / 2.7
ratio = scale_x, scale_y
##fire
    #normal
fire_normal_left = pygame.image.load("fire_normal.png")
fire_normal_left = pygame.transform.scale(fire_normal_left, ratio)
fire_normal_right = pygame.transform.flip(fire_normal_left, True, False)

fire_normal_up = pygame.image.load("fire_normal_top.png")
fire_normal_up = pygame.transform.scale(fire_normal_up, ratio)
fire_normal_down = pygame.transform.flip(fire_normal_up, False, True)
    #blackflash
fire_blackflash_left = pygame.image.load("fire_blackflash.png")
fire_blackflash_left = pygame.transform.scale(fire_blackflash_left, ratio)
fire_blackflash_right = pygame.transform.flip(fire_blackflash_left, True, False)

fire_blackflash_up = pygame.image.load("fire_blackflash_top.png")
fire_blackflash_up = pygame.transform.scale(fire_blackflash_up, ratio)
fire_blackflash_down = pygame.transform.flip(fire_blackflash_up, False, True)

    #blue
fire_blue_left = pygame.image.load("fire_blue.png")
fire_blue_left = pygame.transform.scale(fire_blue_left, ratio)
fire_blue_right = pygame.transform.flip(fire_blue_left, True, False)

fire_blue_up = pygame.image.load("fire_blue_top.png")
fire_blue_up = pygame.transform.scale(fire_blue_up, ratio)
fire_blue_down = pygame.transform.flip(fire_blue_up, False, True)
    #green
fire_green_left = pygame.image.load("fire_green.png")
fire_green_left = pygame.transform.scale(fire_green_left, ratio)
fire_green_right = pygame.transform.flip(fire_green_left, True, False)

fire_green_up = pygame.image.load("fire_green_top.png")
fire_green_up = pygame.transform.scale(fire_green_up, ratio)
fire_green_down = pygame.transform.flip(fire_green_up, False, True)

#game background
game_background = pygame.image.load("game_background.png")
game_background = pygame.transform.scale(game_background, (750,500))
game_background_green = pygame.image.load("game_background_green.png")
game_background_green = pygame.transform.scale(game_background_green, (750,500))

#character
character_front = pygame.image.load("sprite_front.png")
character_front = pygame.transform.scale(character_front, (ratio))
    
character_back = pygame.image.load("sprite_back.png")
character_back = pygame.transform.scale(character_back, (ratio))

character_left = pygame.image.load("sprite_left.png")
character_left = pygame.transform.scale(character_left, (ratio))

character_right = pygame.image.load("sprite_right.png")
character_right = pygame.transform.scale(character_right, (ratio))


character_x = width / 2
character_y = height / 2

direction = character_front

speed = 2

to_right = False
to_left = False
to_up = False
to_down = False

fire_normal = False
fire_blackflash = False
fire_blue = False
fire_green = False

effect = fire_normal_down

game_font = pygame.font.SysFont("comicsansms'", 25)
background_color = 255,255,255
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                to_left = True
            if event.key == pygame.K_d:
                to_right = True  
            if event.key == pygame.K_w:
                to_up = True 
            if event.key == pygame.K_s:
                to_down= True 
            
            if event.key == pygame.K_LEFT:
                fire_normal = True
            if event.key == pygame.K_RIGHT:
                fire_blackflash = True
            if event.key == pygame.K_UP:
                fire_blue = True
            if event.key == pygame.K_DOWN:
                fire_green = True
                
                
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                to_left = False
            if event.key == pygame.K_d:
                to_right = False  
            if event.key == pygame.K_w:
                to_up = False 
            if event.key == pygame.K_s:
                to_down= False
                
            if event.key == pygame.K_LEFT:
                fire_normal = False
            if event.key == pygame.K_RIGHT:
                fire_blackflash = False
            if event.key == pygame.K_UP:
                fire_blue = False
            if event.key == pygame.K_DOWN:
                fire_green = False
                
    if to_right:
        if character_x + character_front.get_width() <= width:
            character_x += speed
            direction = character_right
    
    if to_left:
        if character_x >= 0:
            character_x -= speed
            direction = character_left
    
    if to_down:
        if character_y + character_front.get_height() <= height:
            character_y += speed
            direction = character_front
    
    if to_up:
        if character_y >= 0:
            character_y -= speed
            direction = character_back
    if fire_normal:
        if direction == character_right:
            effect = fire_normal_right
            fire_x = character_front.get_width()
            fire_y = 0
        if direction == character_left:
            effect = fire_normal_left
            fire_x = -character_front.get_width()
            fire_y = 0
        if direction == character_back:
            effect = fire_normal_up
            fire_x = 0
            fire_y = -character_front.get_height()
        if direction == character_front:
            effect = fire_normal_down
            fire_x = 0
            fire_y = character_front.get_height()

    if fire_blackflash:
        if direction == character_right:
            effect = fire_blackflash_right
            fire_x = character_front.get_width()
            fire_y = 0
        if direction == character_left:
            effect = fire_blackflash_left
            fire_x = -character_front.get_width()
            fire_y = 0
        if direction == character_back:
            effect = fire_blackflash_up
            fire_x = 0
            fire_y = -character_front.get_height()
        if direction == character_front:
            effect = fire_blackflash_down
            fire_x = 0
            fire_y = character_front.get_height()


    if fire_blue:
        if direction == character_right:
            effect = fire_blue_right
            fire_x = character_front.get_width()
            fire_y = 0
        if direction == character_left:
            effect = fire_blue_left
            fire_x = -character_front.get_width()
            fire_y = 0
        if direction == character_back:
            effect = fire_blue_up
            fire_x = 0
            fire_y = -character_front.get_height()
        if direction == character_front:
            effect = fire_blue_down
            fire_x = 0
            fire_y = character_front.get_height()

    if fire_green:
        if direction == character_right:
            effect = fire_green_right
            fire_x = character_front.get_width()
            fire_y = 0
        if direction == character_left:
            effect = fire_green_left
            fire_x = -character_front.get_width()
            fire_y = 0
        if direction == character_back:
            effect = fire_green_up
            fire_x = 0
            fire_y = -character_front.get_height()
        if direction == character_front:
            effect = fire_green_down
            fire_x = 0
            fire_y = character_front.get_height()
            
    window.blit(game_background, (0,0))
    window.blit(direction, (character_x, character_y))
    if fire_normal:
        window.blit(effect, (character_x + fire_x, character_y + fire_y))
        text = game_font.render("normal fire!", True, (200,0,0))
        window.blit(text, (character_x + fire_x, character_y + fire_y))

    if fire_blackflash:
        window.fill((0,0,0))
        window.blit(direction, (character_x, character_y))
        window.blit(effect, (character_x + fire_x, character_y + fire_y))
        text = game_font.render("blackflash!", True, (255,255,255))
        window.blit(text, (character_x + fire_x, character_y + fire_y))
        
    if fire_blue:
        pygame.draw.circle(window,(255,255,255), (character_x + character_back.get_width()/2,character_y + character_back.get_height()/2), 100) 
        pygame.draw.circle(window,(0,0,255), (character_x + character_back.get_width()/2,character_y + character_back.get_height()/2), 97) 
        window.blit(direction, (character_x, character_y))
        window.blit(effect, (character_x + fire_x, character_y + fire_y))
        text = game_font.render("blues clues!", True, (255,255,255))
        window.blit(text, (character_x + fire_x, character_y + fire_y))
        
    if fire_green:
        window.blit(game_background_green, (0,0))
        window.blit(direction, (character_x, character_y))
        window.blit(effect, (character_x + fire_x, character_y + fire_y))
        text = game_font.render("escape my light!", True, (0,255,0))
        window.blit(text, (character_x + fire_x, character_y + fire_y))

        
    pygame.display.flip()
    clock.tick(60)
                
    
    