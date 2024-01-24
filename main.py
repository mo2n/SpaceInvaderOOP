import pygame, sys
from spaceship import Spaceship



pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 750, 700
FPS = 60
GREY = (29, 29, 27)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


clock = pygame.time.Clock()

spaceship = Spaceship(SCREEN_WIDTH, SCREEN_HEIGHT)
spaceship_group = pygame.sprite.GroupSingle()
spaceship_group.add(spaceship)


#Loop piu fps
while True:
    fps = clock.get_fps()#
    pygame.display.set_caption(f"PySpaceInvadersOOP - fps: {fps:.2f}")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
 
    #Update
    spaceship_group.update()#movimento spaceship
    

    
    #Drawing
    screen.fill(GREY)
    spaceship_group.draw(screen)
    spaceship_group.sprite.lasers_group.draw(screen)


    pygame.display.update()
    clock.tick(FPS)


