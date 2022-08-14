import pygame, random, os,time
from pygame.locals import *

from os import path #searches specific directories

from pygame.math import Vector2

snd_dir=path.join(path.dirname(__file__), 'snd')#Creates a path that leads to the folder 'snd'

img_dir= path.join(path.dirname(__file__),'img') #Creates a path that leads to the folder 'img'

pygame.init() 

pygame.mixer.init()

WIDTH=1300
HEIGHT=650
playersfile=open("player.txt","r") #opens the file in read mode
lines=playersfile.readlines() #reads each line individually
coinbalance=int(lines[1])#sets the value of the coin balance in the text file to a variable

selected_avatar=0 #The first avatar to appear on the screen will always be 'man'.
FPS=30

DISPLAYSURF= pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Revision Game")
pixeboy=pygame.font.Font("Pixeboy.ttf", 14)
#colours

BLACK   = (0, 0, 0)

AQUA    = (0, 255, 255) 

BLUE    = (0, 0, 255) 

FUCHSIA = (255, 0, 255) 

GREY    = (128, 128, 128) 

GREEN   = (0, 128, 0) 

LIME    = (0, 255, 0) 

MAROON  = (128, 0, 0) 

NAVY    = (0, 0, 128) 

OLIVE   = (128, 128, 0) 

PURPLE  = (128, 0, 128) 

RED     = (255, 0, 0) 

SILVER  = (191, 191, 191) 

TEAL    = (0, 128, 128)

WHITE   = (255,  255, 255) 

YELLOW  = (255, 255, 0)

BROWN   = (102, 51, 0)

DARKBLUE= (0,18,110)
#positions of the first avatar
avatarx=525
avatary=200
confirm=False
running=True


def draw_text(surf, text, size, x, y, font_name):

    font=pygame.font.Font(font_name,size) #Stores font and size

    text_surface= font.render(text,True, WHITE) #Creates the font with specified text

    text_rect=text_surface.get_rect()#Finds the rect

    text_rect.midtop=(x,y)#Finds midpoint of rect

    surf.blit(text_surface,text_rect)#Blits the text

#loading the images
man=pygame.image.load(path.join(img_dir,"man.png")).convert()
woman=pygame.image.load(path.join(img_dir,"woman.png")).convert()
man2=pygame.image.load(path.join(img_dir,"man2.png")).convert()
woman2=pygame.image.load(path.join(img_dir,"woman2.png")).convert()
coin= pygame.image.load(path.join(img_dir,"coin.png")).convert()
#2D array
avatarselector=[[man,0,150,True],[woman,1,300,False],[man2,2,500,False],[woman2,3,700,False]]
while running:
    DISPLAYSURF.fill(DARKBLUE)
    man.set_colorkey(BLACK)
    man2.set_colorkey(BLACK)
    woman.set_colorkey(BLACK)
    woman2.set_colorkey(BLACK)
    coin.set_colorkey(WHITE)
    #text so the user can buy this
    buyingtext1=("This avatar costs "+str(avatarselector[selected_avatar][2])+" coins.")
    buyingtext2=("Press z to buy it.")
    alreadybought1=("You have selected this avatar.")
    alreadybought2=("Press z to go back to the shop page.")
    #blitting the images for them to appear on screen
    DISPLAYSURF.blit(man,(avatarx+60,avatary))
    DISPLAYSURF.blit(woman,(avatarx+200,avatary-60))
    DISPLAYSURF.blit(man2,(avatarx+550,avatary))
    DISPLAYSURF.blit(woman2,(avatarx+850,avatary))
    DISPLAYSURF.blit(coin,(50,50))
    draw_text(DISPLAYSURF, str(coinbalance), 64, 225, 75, "pixeboy.ttf")
    draw_text(DISPLAYSURF, "SHOP", 128, 650, 50, "pixeboy.ttf")
    if confirm==True:
        pygame.draw.rect(DISPLAYSURF, DARKBLUE, (0,0,1300,1000))
        DISPLAYSURF.blit(coin,(50,50))
        draw_text(DISPLAYSURF, str(coinbalance), 64, 225, 75, "pixeboy.ttf")#text for coin balance
        #DISPLAYSURF.blit(avatarselector[selected_avatar][0],(750,200))
        if avatarselector[selected_avatar][3]==False: #if the user hasn't bought the avatar
            draw_text(DISPLAYSURF, buyingtext1, 64, 650, 200, "pixeboy.ttf")
            draw_text(DISPLAYSURF, buyingtext2, 64, 650, 300, "pixeboy.ttf")
        if avatarselector[selected_avatar][3]==True:#if the user has bought it
            draw_text(DISPLAYSURF, alreadybought1, 64, 650, 200, "pixeboy.ttf")
            draw_text(DISPLAYSURF, alreadybought2, 64, 650, 300, "pixeboy.ttf")
    for event in pygame.event.get():

        if event.type== pygame.QUIT:
            #updates the text file when the game quits
            playersfile=open('player.txt','w')
            lines[1]=str(coinbalance)+"\n"
            playersfile.writelines(lines)
            playersfile.close()
            running=False
        elif event.type== KEYDOWN:
            if event.key== K_a: #if user presses a
                if avatarx+900>=0:#and the next movement won't make all of the images go off the screen
                    if selected_avatar<3:
                        avatarx-=300#move the avatar left
                        selected_avatar+=1#change the selected avatar
            if event.key==K_d:#if user presses d
                if avatarx+300<=1300:#and the next movement won't make all the images go off the screen
                    if selected_avatar>0:
                        avatarx+=300#move avatar right
                        selected_avatar-=1#change the selected avatar
            if event.key==K_SPACE: #if the user presses space bar
                confirm=True
            if event.key==K_z:#if the user presses 'z' key
                if avatarselector[selected_avatar][3]==True: #make this avatar the one the user plays as
                    playingavatar=selected_avatar
                if coinbalance>=avatarselector[selected_avatar][2]: #if the user hasn't got it and has enough coins, purchase the avatar.
                    if avatarselector[selected_avatar][3]==False:
                        avatarselector[selected_avatar][3]=True
                        coinbalance= coinbalance-avatarselector[selected_avatar][2] #has a new coin balance for when the user has bought it.
                        print("Yes")
                
                confirm=False
                print(selected_avatar)
                   
                
                
    pygame.display.update()
    pygame.display.flip()
pygame.quit()

