import pygame, sys, random
pygame.init()

# screen
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

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
    def update(self):
        self.jumping()
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
            obstacle_group.add(obstacle)
        else:
            obstacle = Obstacle_b()
            obstacle_group.add(obstacle)
obstacle_group = pygame.sprite.Group()

# game loop
while True:

    # close window when 'x' presed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # draw to screen
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
        
    # update screen 60fps
    pygame.display.update()
    clock.tick(60)
