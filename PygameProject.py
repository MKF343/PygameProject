#Class: CSE 1321
#Group Project by: Michael K, Julian H., Damon B., Kaliayh
import pygame, sys, random, time

pygame.init()

#screen initialization
screenwidth = 1500
screenheight = 700
screen = pygame.display.set_mode((screenwidth, screenheight))
clock = pygame.time.Clock()
pygame.display.set_caption('Whack-a-Mole')

#sound initialization
pygame.mixer.init()

youwin = pygame.mixer.Sound("youwin.mp3")
crash = pygame.mixer.Sound("Slap.mp3")
gameover = pygame.mixer.Sound("gameover.mp3")
wrongmole = pygame.mixer.Sound("wrongmole.mp3")
loading = pygame.mixer.Sound("loading.mp3")
bossmusic = pygame.mixer.Sound("bossmusic.mp3")

#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

#game variables
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
timelimit = 10
targetscore = 10
score = 0
gameactive = False

#mole settings
moleradius = 30
realmolecolor = green
fakemolecolor = red
numfakemoles = 40

#mole positions
molepositions = [(random.randint(moleradius, screenwidth - moleradius), random.randint(moleradius, screenheight - moleradius)) for s in range(numfakemoles + 1)]
molespeeds = [(random.choice([-3, 3]), random.choice([-3, 3])) for i in range(numfakemoles + 1)]
realmoleindex = random.randint(0, numfakemoles)

#button settings
buttonwidth, buttonheight = 200, 80
buttonx = screenwidth // 2 - buttonwidth // 2
buttony = screenheight // 2 - buttonheight // 2
buttonrect = pygame.Rect(buttonx, buttony, buttonwidth, buttonheight)

#timer
starttime = 0


#game functions
def drawmenu():
    screen.fill(white)
    titletext = font.render("Whack-a-Mole", True, black)
    screen.blit(titletext, (screenwidth // 2 - titletext.get_width() // 2, screenheight // 6))
    pygame.draw.rect(screen, green, buttonrect)
    buttontext = font.render("Start", True, white)
    screen.blit(buttontext, (buttonx + buttonwidth // 2 - buttontext.get_width() // 2, buttony + buttonheight // 2 - buttontext.get_height() // 2))
    descriptiontext = font.render(f"Click the green mole {targetscore} times before time runs out!", True, black)
    screen.blit(descriptiontext, (screenwidth //2 - 300, screenheight // 3.5))
    descriptiontext = font.render("Make sure not to click the red balls", True, black)
    screen.blit(descriptiontext, (screenwidth //2 - 200, screenheight // 1.5))

def startgame():
    global gameactive, score, starttime
    gameactive = True
    bossmusic.play()
    score = 0
    starttime = pygame.time.get_ticks()


def drawgame():
    screen.fill(white)

    #draw timer
    elapsedtime = (pygame.time.get_ticks() - starttime) / 1000
    timeleft = timelimit - elapsedtime
    timertext = font.render(f"Time: {int(timeleft)}s", True, black)
    screen.blit(timertext, (10, 10))
    targettext = font.render(f"Target Score: {targetscore}", True, black)
    screen.blit(targettext, (10, 40))

    #draw score
    scoretext = font.render(f"Score: {score}", True, black)
    screen.blit(scoretext, (screenwidth - 110, 10))

    #draw moles
    for i, (x, y) in enumerate(molepositions):
        molecolor = realmolecolor if i == realmoleindex else fakemolecolor
        pygame.draw.circle(screen, molecolor, (x, y), moleradius)

    #check win or lose conditions
    if score >= targetscore:
        if pygame.mixer.get_busy():
            bossmusic.stop()
        youwin.play()
        endgame("You Win!")
    elif timeleft <= 0:
        gameover.play()
        endgame("Time's Up! You Lose!")


def endgame(message):
    global gameactive
    gameactive = False
    screen.fill(white)
    endtext = font.render(message, True, black)
    screen.blit(endtext, (screenwidth // 2 - endtext.get_width() // 2, screenheight // 2 - endtext.get_height() // 2))
    pygame.display.flip()
    pygame.time.delay(3000)
    resetgame()


def resetgame():
    global molepositions, molespeeds, realmoleindex, moleradius
    molepositions = [(random.randint(moleradius, screenwidth - moleradius), random.randint(moleradius, screenheight - moleradius)) for i in range(numfakemoles + 1)]
    molespeeds = [(random.choice([-3, 3]), random.choice([-3, 3])) for i in range(numfakemoles + 1)]
    realmoleindex = random.randint(0, numfakemoles)


def updatemoles():
    for i in range(numfakemoles + 1):
        x, y = molepositions[i]
        dx, dy = molespeeds[i]
        #move mole
        x += dx
        y += dy
        #bounce off walls
        if x - moleradius < 0 or x + moleradius > screenwidth:
            dx = -dx
        if y - moleradius < 0 or y + moleradius > screenheight:
            dy = -dy
        molepositions[i] = (x, y)
        molespeeds[i] = (dx, dy)


def checkmoleclick(pos):
    global score, realmoleindex
    for i, (x, y) in enumerate(molepositions):
        #creating a rect around the moles
        molerect = pygame.Rect(x - moleradius, y - moleradius, moleradius * 2, moleradius * 2)
        if molerect.collidepoint(pos): #checks if you have clicked within the boundaries of the circle
            if i == realmoleindex:
                crash.play()
                score += 1
                #select a new random target mole
                new_index = random.randint(0, numfakemoles)
                #makes sure the new target is actually new
                while new_index == realmoleindex:
                    new_index = random.randint(0, numfakemoles)
                realmoleindex = new_index
            else:
                wrongmole.play()
                score = max(0, score - 1)
            return #makes sure it only checks the one mole


#main loop
while True:
    keys = pygame.key.get_pressed()
    screen.fill(white)

    if not gameactive:
        drawmenu()
    else:
        drawgame()
        updatemoles()

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if keys[pygame.K_ESCAPE]:
            sys.exit()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if not gameactive and buttonrect.collidepoint(event.pos):
                loading.play()
                pygame.time.wait(3000)
                startgame()
            elif gameactive:
                checkmoleclick(event.pos)

    clock.tick(60)
