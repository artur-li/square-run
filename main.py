import pygame, sys
pygame.init()

# screen
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()

# game loop
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        
    # 60fps
    pygame.display.update()
    clock.tick(60)
