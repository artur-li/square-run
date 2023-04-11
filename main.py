import pygame, sys, random
pygame.init()

# screen
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# score
score = 0
font = pygame.font.Font(None, 40)
def update_score():
    score_surf = font.render("SCORE: " + str(score), False, "grey", "black")
    score_rect = score_surf.get_rect(center=(400,60))
    screen.blit(score_surf,score_rect)
class Scorechecker(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.rect = self.image.get_rect(bottomleft=(800,100))
    def movement(self):
        self.rect.centerx -= 5
    def kill(self):
        if self.rect.centerx <= 0:
            pygame.sprite.Sprite.kill(self)
    def score_plus_1(self):
        global score
        if self.rect.centerx == 150:
            score += 1
    def update(self):
        self.score_plus_1()
        self.movement()
        self.kill()

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40,40))
        self.image.fill("white")
        self.rect = self.image.get_rect(midbottom=(200,300))
        self.start_jump_loop = False
        self.jump_speed = 10
    def jumping(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.midbottom == (200,300):
            self.start_jump_loop = True
        if self.start_jump_loop:
            self.rect.centery -= self.jump_speed
            self.jump_speed -= 0.375
            if self.rect.centery >= 280:
                self.start_jump_loop = False
                self.rect.midbottom = (200,300)
                self.jump_speed = 10
    def collision(self):
        global game_state, over_state
        collided = pygame.sprite.spritecollide(player, obstacle_group, False)
        for i in collided:
            if i != None:
                game_state = False
                over_state = True
    def update(self):
        self.jumping()
        self.collision()
player_group = pygame.sprite.Group()
player = Player()
player_group.add(player)

class Obstacle_a(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill("red")
        self.rect = self.image.get_rect(bottomleft=(800,300))
    def movement(self):
        self.rect.centerx -= 5
    def kill(self):
        if self.rect.centerx <= 0:
            pygame.sprite.Sprite.kill(self)
    def update(self):
        self.movement()
        self.kill()
class Obstacle_b(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((80,80))
        self.image.fill("red")
        self.rect = self.image.get_rect(bottomleft=(800,220))
    def movement(self):
        self.rect.centerx -= 5
    def kill(self):
        if self.rect.centerx <= 0:
            pygame.sprite.Sprite.kill(self)
    def update(self):
        self.movement()
        self.kill()
timer = 0
interval = 1
def spawn_obstacle():
    global timer
    global interval
    timer += interval
    if timer % 1440 == 0 and interval <= 2.5:
        interval += 0.5
    if timer % 180 == 0:
        if random.choice([1,2]) == 1:
            obstacle = Obstacle_a()
            score_check = Scorechecker()
            obstacle_group.add(obstacle, score_check)
        else:
            obstacle = Obstacle_b()
            score_check = Scorechecker()
            obstacle_group.add(obstacle, score_check)
obstacle_group = pygame.sprite.Group()

# start_game state
def start_game():
    global game_state
    global start_state
    play_surf = font.render("PLAY", False, "Blue", "black")
    play_rect = play_surf.get_rect(center=(400,200))
    screen.blit(play_surf,play_rect)
    mouse_pos = pygame.mouse.get_pos()
    if play_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() != (False, False, False):
        start_state = False
        game_state = True

# game_active state
def game():
    # background
    screen.fill("black")
    pygame.draw.line(screen,"white",(0,300),(800,300),1)
    # player
    player_group.draw(screen)
    player_group.update()
    # obstacles
    spawn_obstacle()
    obstacle_group.draw(screen)
    obstacle_group.update()
    # score 
    update_score()

# game_over state
def game_over():
    global game_state, timer, interval, score
    screen.fill("black")
    score_surf = font.render("FINAL SCORE: " + str(score), False, "grey", "black")
    score_rect = score_surf.get_rect(center=(400,170))
    screen.blit(score_surf,score_rect)
    play_surf = font.render("PLAY AGAIN", False, "Blue", "black")
    play_rect = play_surf.get_rect(center=(400,230))
    screen.blit(play_surf,play_rect)
    mouse_pos = pygame.mouse.get_pos()
    if play_rect.collidepoint(mouse_pos) and pygame.mouse.get_pressed() != (False, False, False):
        timer = 0
        interval = 1
        game_state = True
        score = 0
        obstacle_group.empty()

# state variables
start_state = True
game_state = False
over_state = False



# game loop
while True:

    # close window when 'x' presed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    if start_state:
        start_game()
    
    elif game_state:
        game()
    
    elif over_state:
        game_over()
    
    # update screen 60fps
    pygame.display.update()
    clock.tick(60)
