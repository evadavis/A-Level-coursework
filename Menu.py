import pygame, sys,time,random
from pygame.locals import *
#colours
BLACK = (0, 0, 0)
AQUA = (0, 255, 255) 
BLUE = (15, 8, 79) 
FUCHSIA = (255, 0, 255) 
GREY = (128, 128, 128) 
GREEN = (0, 128, 0) 
LIME = (0, 255, 0) 
MAROON = (128, 0, 0) 
NAVY = (0, 0, 128) 
OLIVE = (128, 128, 0) 
PURPLE = (128, 0, 128) 
RED = (255, 0, 0) 
SILVER = (192, 192, 192) 
TEAL = (0, 128, 128)
WHITE = (255,  255, 255) 
YELLOW = (255, 255, 0)
BROWN = (102, 51, 0)
pygame.init()
clock=pygame.time.Clock
DISPLAYSURF= pygame.display.set_mode((1000,700)) #Creates window
pygame.display.set_caption('Hello World!')
#establishing the fonts
pixeboy=pygame.font.Font("Pixeboy.ttf", 144)
pixeboymed=pygame.font.Font("Pixeboy.ttf", 96)
pixeboysmall=pygame.font.Font("Pixeboy.ttf", 72)
#Rendering the text and setting its positions
title= pixeboy.render("Revision Game", True, BLACK)
titleRect=title.get_rect()
titleRect.center= (500,75)
playgame= pixeboysmall.render("Play Game", True, BLACK)
playgameRect=playgame.get_rect()
playgameRect.center= (500,225)
shop= pixeboysmall.render("Shop", True, BLACK)
shopRect=shop.get_rect()
shopRect.center= (500,325)
options= pixeboysmall.render("Options", True, BLACK)
optionsRect=options.get_rect()
optionsRect.center= (500,525)
statistics= pixeboysmall.render("Statistics", True, BLACK)
statisticsRect=statistics.get_rect()
statisticsRect.center= (500,425)
sum=pixeboymed.render("1+1=2",True, BLACK)
sumRect=sum.get_rect()
sumRect.center=(150,500)
#loads images 
franceimg=pygame.image.load("france.png")
worldimg=pygame.image.load("world.png")
bookimg=pygame.image.load("book.png")
running=True
while running:
    DISPLAYSURF.fill(BLUE)
    mousex=0
    mousey=0
    mouseClicked=False
    mouse = pygame.mouse.get_pos() #get position of mouse
    #drawing the boxes for the text
    pygame.draw.rect(DISPLAYSURF,WHITE,(40,25,900,100)) 
    pygame.draw.rect(DISPLAYSURF,BLACK,(40,25,900,100),5)
    pygame.draw.rect(DISPLAYSURF,WHITE,(300,185,400,75))
    pygame.draw.rect(DISPLAYSURF,BLACK,(300,185,400,75),5)
    pygame.draw.rect(DISPLAYSURF,WHITE,(300,285,400,75))
    pygame.draw.rect(DISPLAYSURF,BLACK,(300,285,400,75),5)
    pygame.draw.rect(DISPLAYSURF,WHITE,(300,385,400,75))
    pygame.draw.rect(DISPLAYSURF,BLACK,(300,385,400,75),5)
    pygame.draw.rect(DISPLAYSURF,WHITE,(300,485,400,75))
    pygame.draw.rect(DISPLAYSURF,BLACK,(300,485,400,75),5)
    #displaying the text
    DISPLAYSURF.blit(title,titleRect) #blits title text with coordinates 
    DISPLAYSURF.blit(playgame,playgameRect) #blits playgame with coordinates 
    DISPLAYSURF.blit(shop,shopRect)
    DISPLAYSURF.blit(options,optionsRect)
    DISPLAYSURF.blit(statistics,statisticsRect)
    #displaying the images
    DISPLAYSURF.blit(franceimg, (25,200))
    DISPLAYSURF.blit(sum,sumRect)
    DISPLAYSURF.blit(worldimg,(700,100))
    DISPLAYSURF.blit(bookimg, (650,400))
    if 295+410 > mouse[0] > 300 and 180+85 > mouse[1] > 185: #if coordinates of mousex and mousey are between these coordinates
            pygame.draw.rect(DISPLAYSURF,YELLOW,(300,185,400,75),5)#draw a yellow box with the same specifics as the black outline box
    if 295+410 > mouse[0] > 300 and 280+85 > mouse[1] > 285:
            pygame.draw.rect(DISPLAYSURF,YELLOW,(300,285,400,75),5)
    if 295+410 > mouse[0] > 300 and 380+85 > mouse[1] > 385:
            pygame.draw.rect(DISPLAYSURF,YELLOW,(300,385,400,75),5)
    if 295+410 > mouse[0] > 300 and 480+85 > mouse[1] > 485:
            pygame.draw.rect(DISPLAYSURF,YELLOW,(300,485,400,75),5)




    for event in pygame.event.get():
        if event.type == QUIT: #Quits game
            pygame.quit()
            sys.exit()
        elif event.type==MOUSEMOTION: #If mouse moves
            mousex,mousey=event.pos#take note of the mouse positions
        elif event.type==MOUSEBUTTONUP:#if the mouse button is clicked
            mousex,mousey=event.pos
            mouseClicked=True#change mouse clicked to true
    pygame.display.update()
    