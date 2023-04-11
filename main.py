import pygame, sys
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

# game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill("black")
    pygame.draw.line(screen,"white",(0,300),(800,300),1)
    player_group.draw(screen)
    player_group.update()
        
    # 60fps
    pygame.display.update()
    clock.tick(60)
