# Complete your game here
import pygame
import random
## game is a coin collector game
## there will be falling monster if it touches you, game will reset
## there will doors if you touch it, you will be teleported to a random location

class Collector():
    def __init__(self) -> None:
        pygame.init()
        
        self.width = 720
        self.height = 720   
        
        self.game_font = pygame.font.SysFont("Avenir", 20)
        self.window = pygame.display.set_mode((self.width, self.height + 100))
        self.clock = pygame.time.Clock()
        self.tries = 1
        self.high_score = (0,0)

        self.load_images()
        self.new_game()
        self.main_loop()
    
    def load_images(self):
        self.images = {}
        for image in ["coin", "door", "monster", "robot"]:
            self.images[image] = pygame.image.load(image + ".png")
            
    def interactive_items(self, amount:int, classification:str):
        for i in range(amount):
            x = random.randint(0, self.width - self.images[classification].get_width())
            if classification == "monster":
                y = -random.randint(10,1000)
            else:
                y = random.randint(0, self.height - self.images[classification].get_height())
            self.interactive[classification][i] = x,y
    
    def new_game(self):
        #caption
        pygame.display.set_caption("Coin Collector")
        
        #interactive item container
        self.interactive = {"coin" : {}, "door" : {}, "monster" : {}}

        #score and level
        self.score = 0
        self.level = 1
        self.game_over = False
        
        #coin generator 
        self.interactive_items(5, "coin")
        #teleport-ing door generator
        self.interactive_items(2, "door")
        #falling monsters generator
        self.interactive_items(4, "monster")
        
        #robot movement
        self.robot_x = self.width/2 - self.images["robot"].get_width()/2
        self.robot_y = self.height/2 - self.images["robot"].get_height()/2
        self.speed = 3
        
        #movement info
        self.to_right = False
        self.to_left = False
        self.to_up = False
        self.to_down = False
    
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
    
    def move(self):
        if self.to_left:
            if self.robot_x > 0:
                self.robot_x -= self.speed
        if self.to_right:
            if self.robot_x + self.images["robot"].get_width() < self.width:
                self.robot_x += self.speed
        if self.to_up:
            if self.robot_y > 0:
                self.robot_y -= self.speed
        if self.to_down:
            if self.robot_y + self.images["robot"].get_height() < self.height:
                self.robot_y += self.speed
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a: # move left
                    self.to_left = True
                if event.key == pygame.K_d: # move right
                    self.to_right = True
                if event.key == pygame.K_w: # move up
                    self.to_up = True
                if event.key == pygame.K_s: # move down
                    self.to_down = True
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_n:
                    self.new_game()
                    
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a: # move left
                    self.to_left = False
                if event.key == pygame.K_d: # move right
                    self.to_right = False
                if event.key == pygame.K_w: # move up
                    self.to_up = False
                if event.key == pygame.K_s: # move right
                    self.to_down = False
        self.move()
    
    def collected(self, coordinate: tuple, object:str):
        object_x = coordinate[0]
        object_y = coordinate[1]
        #range only works with integers
        touch_x = coordinate[0] + self.images[object].get_width()//2 in range(round(self.robot_x), round(self.robot_x + self.images["robot"].get_width()))
        touch_y = coordinate[1] + self.images[object].get_height()//2 in range(round(self.robot_y), round(self.robot_y + self.images["robot"].get_height()))
        if touch_x and touch_y:
            return True
        return False
        
    def draw_window(self):
        #coin generator
        self.window.fill("#555555")
        
        for coin, coordinate in self.interactive["coin"].items():
            if self.collected(coordinate, "coin"):
                x = random.randint(0, self.width - self.images["coin"].get_width())
                y = random.randint(0, self.height - self.images["coin"].get_height())
                self.interactive["coin"][coin] = x,y
                self.window.blit(self.images["coin"], (x,y))
                self.score += 1
            else:
                self.window.blit(self.images["coin"], (coordinate[0], coordinate[1]))
                
        #increasing difficulty every 15 coins collected
        #adding an additional monster
        if self.score > self.level * 15:
            #add more monster
            monster_x = random.randint(0, self.width - self.images["monster"].get_width())
            monster_y = -random.randint(10,1000)
            self.interactive["monster"][len(self.interactive["monster"])+1] = monster_x, monster_y
            #add more doors for randomness
            door_x = random.randint(0, self.width - self.images["monster"].get_width())
            door_y = random.randint(0, self.height - self.images["door"].get_height())
            self.interactive["door"][len(self.interactive["door"])+1] = door_x, door_y
            self.level += 1
                
        for door, coordinate in self.interactive["door"].items():
            if self.collected(coordinate, "door"):
                x = random.randint(0, self.width - self.images["door"].get_width())
                y = random.randint(0, self.height - self.images["door"].get_height())
                self.interactive["door"][door] = x,y
                self.window.blit(self.images["door"], (x,y))
                #teleport robot
                self.robot_x = random.randint(0, self.width - self.images["robot"].get_width())
                self.robot_y = random.randint(0, self.height - self.images["robot"].get_height())
            else:
                self.window.blit(self.images["door"], (coordinate[0], coordinate[1]))
                
        for monster, coordinate in self.interactive["monster"].items():
            if self.collected(coordinate, "monster"):
                self.game_over = True
                if (self.score, self.level) > self.high_score:
                    self.high_score = (self.score, self.level)
            if self.interactive["monster"][monster][1] + self.images["monster"].get_height() >= self.height:
                x = random.randint(0, self.width - self.images["monster"].get_width())
                y = -random.randint(100,3000)
                self.interactive["monster"][monster] = x,y
            else:
                self.interactive["monster"][monster] = coordinate[0], coordinate[1] + self.speed
                self.window.blit(self.images["monster"], (coordinate[0], coordinate[1]))
            
        #moving robot
        image = self.images["robot"]
        self.window.blit(image, (self.robot_x, self.robot_y))
        
        #time
        self.clock.tick(60)
        
        #bottom screen info
        pygame.draw.rect(self.window, "#eeeee4", (0, self.height, self.width, 100))
        pygame.draw.rect(self.window, "#555da1", (5, self.height+5, self.width-10, 90))
        
        #instructions
        game_text = self.game_font.render("WASD: movement", True, "#eeeee4")
        self.window.blit(game_text, (20, self.height - game_text.get_height()/2 + 28))
        game_text = self.game_font.render("Esc: exit", True, "#eeeee4")
        self.window.blit(game_text, (20, self.height - game_text.get_height()/2 + 53))
        game_text = self.game_font.render("N: new game", True, "#eeeee4")
        self.window.blit(game_text, (20, self.height - game_text.get_height()/2 + 78))
        
        
        #score info
        game_text = self.game_font.render(f"Score: {self.score}", True, "#eeeee4")
        self.window.blit(game_text, (self.width - game_text.get_width() - 20, self.height + 50 - game_text.get_height()/2))
        
        #level info
        game_text = self.game_font.render(f"Level: {self.level}", True, "#eeeee4")
        self.window.blit(game_text, (self.width//2 - game_text.get_width()//2, self.height + 50 - game_text.get_height()/2))
        
        #game status
        if self.game_over:
            pygame.draw.rect(self.window, (0,0,0), (0,0,self.width,self.height))
            game_text = self.game_font.render("thanks for playing", True, (255,0,0))
            self.window.blit(game_text,(self.width//2 - game_text.get_width()//2, self.height//2 - game_text.get_height()//2))
            game_text = self.game_font.render(f"score achieved: level {self.level} ({self.score} coins)", True, (255,255,255))
            self.window.blit(game_text,  (self.width//2 - game_text.get_width()//2, self.height//2 - game_text.get_height()//2 + 50))
            game_text = self.game_font.render(f"high score: level {self.high_score[1]} ({self.high_score[0]} coins)", True, (255,255,255))
            self.window.blit(game_text,  (self.width//2 - game_text.get_width()//2, self.height//2 - game_text.get_height()//2 + 100))
            
        #update window
        pygame.display.flip()
        
Collector()