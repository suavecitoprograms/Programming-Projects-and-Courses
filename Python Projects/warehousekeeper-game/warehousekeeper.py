import pygame

class WarehouseKeeper:
    def __init__(self) -> None:
        pygame.init()
        self.load_images()
        self.new_game()
        
        self.height = len(self.map)
        self.width = len(self.map[0])
        self.scale = self.images[0].get_width()
        
        self.game_font = pygame.font.SysFont("comicsansms", 24)
        
        window_width = self.width * self.scale
        window_height = self.height * self.scale
        self.window = pygame.display.set_mode((window_width, window_height + self.scale))
        
        pygame.display.set_caption("Warehouse Keeper")
        
        self.main_loop()
    
    
    def load_images(self):
        self.images = []
        for name in ["floor", "wall", "target", "box", "robot", "done", "target_robot"]:
            self.images.append(pygame.image.load(name+".png"))
    
    def new_game(self):
        self.moves = 0
        self.map = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
                    [1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 2, 3, 0, 0, 0, 1, 0, 0, 1, 2, 3, 0, 0, 0, 0, 1],
                    [1, 0, 0, 1, 2, 3, 0, 2, 3, 0, 0, 0, 1, 0, 0, 0, 1],
                    [1, 0, 4, 1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 1],
                    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
    
    def main_loop(self):
        while True:
            self.check_events()
            self.draw_window()
    
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    self.move(0, -1)
                if event.key == pygame.K_RIGHT:
                    self.move(0, 1)
                if event.key == pygame.K_UP:
                    self.move(-1, 0)
                if event.key == pygame.K_DOWN:
                    self.move(1, 0)
                #other functionality (exit or newgame)
                if event.key == pygame.K_ESCAPE:
                    exit()
                if event.key == pygame.K_n:
                    self.new_game()
                    
    def find_robot(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [4, 6]:
                    return y,x

    def move(self, move_y:int, move_x:int):
        if self.game_solved():
            return
        robot_old_y, robot_old_x = self.find_robot()
        robot_new_y = robot_old_y + move_y 
        robot_new_x = robot_old_x + move_x
        
        if self.map[robot_new_y][robot_new_x] == 1:
            return
        
        if self.map[robot_new_y][robot_new_x] in [3, 5]:
            box_new_y = robot_new_y + move_y 
            box_new_x = robot_new_x + move_x
            
            if self.map[box_new_y][box_new_x] in [1,3,5]:
                return
            
            #update position of robot assuming it hits a box
            self.map[robot_new_y][robot_new_x] -= 3 #if initial box[3] it becomes floor[0] if done[5] it becomes target[2]
            self.map[box_new_y][box_new_x] += 3 #if floor[0] it becomes box[3] if target[2] it becomes done[5]
        #new position of robot
        self.map[robot_old_y][robot_old_x] -= 4 #if floor[0] it becomes robot[4] if target[2] it becomes target_robot[6]
        self.map[robot_new_y][robot_new_x] += 4 #if robot[4] it becomes floor[0] if target_robot[6] it becomes target[2]
        #register a move if the robot did move
        self.moves += 1
    
    def game_solved(self):
        for y in range(self.height):
            for x in range(self.width):
                if self.map[y][x] in [2,6]: #2 is empty target #6 is robot on target
                    return False
        return True
        
    def draw_window(self):
        self.window.fill((0,0,0))
        
        for y in range(self.height):
            for x in range(self.width):
                square = self.map[y][x]
                self.window.blit(self.images[square], (self.scale*x, self.scale*y))
                
        #move counter
        game_text = self.game_font.render(f"Moves: {self.moves}", True, (255,255,255))
        self.window.blit(game_text, (self.scale*self.width - game_text.get_width() - 20, self.scale*self.height + 7))
        #settings
            #press N for new game
        game_text = self.game_font.render("N = new game", True, (255,255,255))
        self.window.blit(game_text, (30, self.scale*self.height + 7))
            #press Esc to escape and exit
        game_text = self.game_font.render("Esc = exit game", True, (255,255,255))
        self.window.blit(game_text, (30 + game_text.get_width(), self.scale*self.height + 7))
        
        if self.game_solved():
            game_text = self.game_font.render("Congratulations, took you long enough!", True, (250,248,246))
            game_text_y = self.scale * self.height // 2 - game_text.get_height() // 2
            game_text_x = self.scale * self.width // 2 - game_text.get_width() // 2
            pygame.draw.rect(self.window, (193,66,63), (game_text_x - game_text.get_width()//6.5, game_text_y - game_text.get_height()//3, game_text.get_width() + game_text.get_width()//3,game_text.get_height() + game_text.get_height()//1.5))
            self.window.blit(game_text, (game_text_x, game_text_y))
            
        
        pygame.display.flip()
    
if __name__ == "__main__":
    WarehouseKeeper()