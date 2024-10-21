#Class: CSE 1321
#Group Project by: Michael Kirtland, insert name here, insert name here, insert name here
import pygame,sys
import random
import time
pygame.init()
#screen initialization
screenwidth = 800
screenheight = 800
screen = pygame.display.set_mode((screenwidth,screenheight))
clock = pygame.time.Clock()
pygame.display.set_caption('Whack-a-mole')
#initialization for sounds
pygame.mixer.init()
spawn = pygame.mixer.Sound("spawning.mp3")
crash = pygame.mixer.Sound("Slap.mp3")
#Font
font = pygame.font.Font(None, 36)
#time variables
starttime = 0
#method for meteors
def spawnmeteor():
    spawn.play()
    side = random.choice(['top', 'bottom', 'left', 'right'])

    if side == 'top':
        x = random.randint(0, screenwidth)
        y = 0
        dx = random.uniform(-2, 2)
        dy = random.uniform(1, 4)
    elif side == 'bottom':
        x = random.randint(0, screenwidth)
        y = screenheight
        dx = random.uniform(-2, 2)
        dy = random.uniform(-1, -4)
    elif side == 'left':
        x = 0
        y = random.randint(0, screenheight)
        dx = random.uniform(1, 4)
        dy = random.uniform(-2, 2)
    elif side == 'right':
        x = screenwidth
        y = random.randint(0, screenheight)
        dx = random.uniform(-1, -4)
        dy = random.uniform(-2, 2)

    size = random.randint(20, 60)
    meteor = pygame.Rect(x, y, size, size)
    return meteor, dx, dy
#resetting the game method
def resetgame():
    global meteors, starttime, timesurvived, meteorspawnrate
    meteors.clear()
    player.x, player.y = screenwidth//2 - 40//2,screenheight//2 - 40//2
    starttime = pygame.time.get_ticks()
    timesurvived = 0
    meteorspawnrate = 5000
#boolean variables
status = "Off"
busy = False
#button click detection method
def buttonclicked(pos, buttonrect):
    return buttonrect.collidepoint(pos)
#reset to start
resetgame()
while True:
    keys = pygame.key.get_pressed()
    clock.tick(60)
    #filling the screen
    screen.fill((0,0,0))
    #timer
    currenttime = pygame.time.get_ticks()
    timesurvived = font.render(f'Time: {timesurvived}s', False, (255,255,255))
    screen.blit(timesurvived, (0,0))
    #update screen
    pygame.display.flip()
    #events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
