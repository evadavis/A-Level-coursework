import pygame, sys
from pygame.locals import *
#colours
BLACK = (0, 0, 0)
AQUA = (0, 255, 255) 
BLUE = (0, 0, 255) 
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
DARKBLUE=(0,18,110)
pygame.init()
playersfile=open("player.txt","r") #opens the file in read mode
lines=playersfile.readlines() #reads each line individually
questionscorrect=int(lines[2]) #takes the questions correct and questions answered specifically from a line in the file
questionsanswered=int(lines[3])
accuracyrating=(questionscorrect/questionsanswered) #finds an accuracy rating by finding the ratio of questions correct to questions answered
accuracypercentage=accuracyrating*100
DISPLAYSURF= pygame.display.set_mode((1300,650)) #Creates window
pygame.display.set_caption('Hello World!')#Creates caption
pixeboy=pygame.font.Font("Pixeboy.ttf", 14)
def draw_text(surf, text, size, x, y, font_name):

    font=pygame.font.Font(font_name,size) #Stores font and size

    text_surface= font.render(text,True, WHITE) #Creates the font with specified text

    text_rect=text_surface.get_rect()#Finds the rect

    text_rect.midtop=(x,y)#Finds midpoint of rect

    surf.blit(text_surface,text_rect)#Blits the text

while True:
    DISPLAYSURF.fill(DARKBLUE)
    #text
    draw_text(DISPLAYSURF, "Computer Science", 128, 650,50, "pixeboy.ttf")
    draw_text(DISPLAYSURF, "Number of correct answers: "+str(questionscorrect), 64, 400,275, "pixeboy.ttf")
    draw_text(DISPLAYSURF, "Number of questions answered: "+str(questionsanswered), 64, 445,325, "pixeboy.ttf")
    draw_text(DISPLAYSURF, "Computer Science", 128, 650,50, "pixeboy.ttf")
    pygame.draw.rect(DISPLAYSURF,BLACK,(100,150,1100,75),10) #draws 
    pygame.draw.rect(DISPLAYSURF,GREEN,(105,155,(1095*accuracyrating),65)) #uses the accuracy rating to determine the length of the bar
    for event in pygame.event.get():
        if event.type == QUIT: #Quits game
            pygame.quit()
            sys.exit()
    pygame.display.update()
