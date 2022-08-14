import pygame, random, os,time

from os import path

from pygame.math import Vector2

snd_dir=path.join(path.dirname(__file__), 'snd')#Creates a path that leads to the folder 'snd'

img_dir= path.join(path.dirname(__file__),'img') #Creates a path that leads to the folder 'img'

playersfile=open("player.txt","r")

lines=playersfile.readlines() #reads each line individually
questionscorrectfile=int(lines[2]) #takes the questions correct and questions answered specifically from a line in the file
questionsansweredfile=int(lines[3])
coinbalance=int(lines[1])
pygame.init() 

pygame.mixer.init()

WIDTH=1300

HEIGHT=650

FPS=30

questionsanswered=0
questionscorrect=0
questionswrong=0
lives=5
correct=False

DISPLAYSURF= pygame.display.set_mode((WIDTH,HEIGHT))

pygame.display.set_caption("Revision Game")

clock=pygame.time.Clock()#Implements time

startposition=-100

pixeboy=pygame.font.Font("Pixeboy.ttf", 14)

hitss=False

wrong=False


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

DARKBLUE=(0,18,110)

def questiongeneration():

    computer_science=open("Computer Science.txt","r")

    csRec=computer_science.readline()

    questionnumber=random.randint(1,5)

    questionnumber=str(questionnumber)

    print(questionnumber)

    lista=[]

    

    while csRec!="":

        field=csRec.split(",")

        

        if field[0][0]==questionnumber:

            answer1=field[1]

            answer2=field[2]

            answer3=field[3]

            answer4=field[4]

            for a in range(1,4):

                if field[a][0]=="!":

                    correctanswer=field[a][1:]

                    print(correctanswer)

                    lista.append(correctanswer)

                    question=field[0][1:]

                else:

                    lista.append(field[a])

        csRec=computer_science.readline()

        

    return lista,correctanswer,question

#draw_text function

lista,correctanswer,question=questiongeneration()

#draw_text function



print(question,correctanswer,lista)

#draw_text function

def draw_text(surf, text, size, x, y, font_name):

    font=pygame.font.Font(font_name,size) #Stores font and size

    text_surface= font.render(text,True, WHITE) #Creates the font with specified text

    text_rect=text_surface.get_rect()#Finds the rect

    text_rect.midtop=(x,y)#Finds midpoint of rect

    surf.blit(text_surface,text_rect)#Blits the text

class Player(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image= pygame.transform.scale(avatar_img,(75,125))#

        self.image.set_colorkey(BLACK)

        #self.image.set_colorkey(WHITE)

        self.rect=self.image.get_rect()

        self.rect.centerx=WIDTH/2

        self.rect.bottom= HEIGHT-10

        self.speedx=0

        self.speedy=0

        self.shield=100

        self.shoot_delay=250

        self.last_shot=pygame.time.get_ticks()

    def update(self):

        self.speedx=0

        self.speedy=0

        keystate=pygame.key.get_pressed()#Gets all the possible key presses.

        if keystate[pygame.K_a]: #If left key is pressed.

            self.speedx=-3 #Change speed to go left.

        if keystate[pygame.K_d]:#If right key is pressed.

            self.speedx=3 #Change speed to go right

      

        #if keystate[pygame.K_SPACE]:

        

        self.rect.x+=self.speedx #Change x position

        self.rect.y+=self.speedy#Change y position

        if self.rect.right>WIDTH: #If the right side of the rect is past the width, stop it from moving

            self.rect.right=WIDTH

        if self.rect.left<0: #If the left side is goes outside the window, stop it from moving

            self.rect.left=0

        if self.rect.bottom>HEIGHT: #If reaches bottom of screen, stop it from moving more

            self.rect.bottom= HEIGHT

        if self.rect.top<0:#If reaches top, stop movement

            self.rect.top=0

    def shoot(self): #Adds a bullet sprite

        now=pygame.time.get_ticks()

        #if now-self.last_shot>self.shoot_delay:

            #self.last_shot=now

        bullet=Bullet(self.rect.centerx, self.rect.top)#Sets position of bullet to be top centre of player.

        all_sprites.add(bullet)#draws bullet

        bullets.add(bullet)

class spaceship(pygame.sprite.Sprite):

    def __init__(self):

        pygame.sprite.Sprite.__init__(self)

        self.image =pygame.transform.scale(spaceship_img,(200,150))#sets the image of the sprite to be this colour

        self.image.set_colorkey(DARKBLUE)#Removes black

        self.test=pixeboy.render(str(text),True,BLACK) #creates text to follow

        self.rect=self.image.get_rect()

        self.rect.x=startposition

        self.rect.y= startpositiony#

        self.pos=Vector2(startposition,startpositiony)#The vector command means that you can move sprites at a float speed.

        

        self.speedx=0#The spaceships will not be moving horizontally so the speed on the x axis will be 0.

        self.speedy=0.5

        self.answer=text

        self.velocity=Vector2(0,0.4)#The spaceship will be moving slowly vertically so the speed will be 0.2.

        self.testRect=self.test.get_rect()

        self.testRect.center=(self.speedx+100,self.speedy+75) #follows the image and changed the position to fit the size of the ship

        self.testing=self.image.blit(self.test,self.testRect)#puts the text onto the image

    def update(self):

         self.pos+=self.velocity#The position updates with the velocity.

         self.rect.center=self.pos#The position becomes the rect centre.

         if self.rect.bottom==525: #If reaches bottom of screen, stop it from moving more

            self.kill()

         if correct==True:

            self.kill()

         if wrong==True:

            self.kill()

        

class Bullet(pygame.sprite.Sprite):

    def __init__(self,x ,y):

        pygame.sprite.Sprite.__init__(self)

        self.image=pygame.Surface((10,20))#sets the bullet to be an aqua rectangle

        self.image.fill(AQUA)

        self.rect=self.image.get_rect()

        self.rect.bottom=y

        self.rect.centerx=x

        self.speedy=-1 #sets the speed to go up

    def update(self):

        self.rect.y+=self.speedy

        if self.rect.bottom<0:

            self.kill()
        if correct==True:
            self.kill()
        if wrong==True:
            self.kill()

def newmob(all_sprites,mobs,lista):

    

    global startposition

    #global startpositony

    startposition=100

    startpositiony=0

    for s in range(2):

        startpositiony=startpositiony+50

        for i in range(5):

            global text

            text=random.choice(lista)#

            

            m=spaceship()

            

            startposition=startposition+275

            all_sprites.add(m)

            mobs.add(m)

            all_sprites.update()

        

    

startpositiony=0

all_sprites= pygame.sprite.Group()        

spaceship_img= pygame.image.load(path.join(img_dir, "spaceship.png")).convert()

avatar_img= pygame.image.load(path.join(img_dir, 'man.png')).convert()

bullets=pygame.sprite.Group()

mobs=pygame.sprite.Group()

player=Player()

all_sprites.add(player)



startposition=100

startpositiony=0

for s in range(50): #for each row in spaceships
            for a in range(2):
                
                for i in range(15): #Adds 5 spaceships

                    text=random.choice(lista)

                    m=spaceship()

                    startposition=startposition+275 #Increases the start position by 175

                    

                    all_sprites.add(m) 

                    mobs.add(m)
                   
                startpositiony-=175
                startposition=40
                startposition=startposition+140
            startpositiony-=25
            startposition=40
#newmob(all_sprites,mobs,lista)



#newmob2(all_sprites,mobs,lista)

test=False

running=True



while running:

    

                 

    

    DISPLAYSURF.fill(DARKBLUE)

    all_sprites.update()

    all_sprites.draw(DISPLAYSURF)
    pygame.draw.rect(DISPLAYSURF, DARKBLUE, (0,0,1750,65))
    livesdrawn=draw_text(DISPLAYSURF, "Lives:"+str(lives), 34, 75, 600, "Pixeboy.ttf")
    newquestion=draw_text(DISPLAYSURF, question, 34, 650, 25, "Pixeboy.ttf")

    for event in pygame.event.get():

        if event.type== pygame.QUIT:
            
            playersfile=open('player.txt','w')
            lines[2]=(str(questionscorrectfile+questionscorrect)+"\n")
            lines[3]=(str(questionsansweredfile+questionsanswered)+"\n")
            lines[1]=(str(coinbalance)+"\n")
            playersfile.writelines(lines)
            playersfile.close()

            running=False

        elif event.type==pygame.KEYDOWN:#If the player presses space then shoot the bullet/]

            if event.key==pygame.K_SPACE:

                player.shoot()

    hits=pygame.sprite.groupcollide(mobs,bullets,True,True)

    time_passed=time.time()

    

    for hit in hits:
        questionsanswered+=1
        if hit.answer==correctanswer:

            
            questionscorrect+=1
            print("correct")

            startposition=40

            startpositiony=0

            coinbalance+=10 #Increase coinbalance

            correct=True

            all_sprites.update()

            correct=False
            
        if hit.answer!=correctanswer:
            questionswrong+=1
            startposition=40

            startpositiony=0

            lives-=1 #Decrease the lives by 1

            wrong=True

            print("Wrong")

            all_sprites.update()

            wrong=False
        lista,correctanswer,question=questiongeneration()
        
        for s in range(50): #for each row in spaceships
            for a in range(2): #Change the startposition every two ships.
                
                for i in range(15): #Adds 5 spaceships

                    text=random.choice(lista)

                    m=spaceship()

                    startposition=startposition+275 #Increases the start position by 175

                    

                    all_sprites.add(m) 

                    mobs.add(m)
                   
                startpositiony-=175
                startposition=40
                startposition=startposition+140
            startpositiony-=25
            startposition=40
           # startposition=startposition+150
                
        print("Coin balance:"+str(coinbalance))
            
            
        livesdrawn=draw_text(DISPLAYSURF, str(lives), 34, 150, 800, "Pixeboy.ttf")#update the lives amount
        newquestion=draw_text(DISPLAYSURF, question, 34, 650, 25, "Pixeboy.ttf")  #draw the new question   
    if lives==0: #if lives run out end the game
        lines[2]=(str(questionscorrectfile+questionscorrect)+"\n") #adds the two values together
        lines[3]=(str(questionsansweredfile+questionsanswered)+"\n")#adds the two values together
        lines[1]=(str(coinbalance)+"\n")
        playersfile=open('player.txt','w')#opens the file in write mode
        playersfile.writelines(lines)#writes the lines
        playersfile.close()
        pygame.quit()

    pygame.display.update()

    all_sprites.update()

    pygame.display.flip()

pygame.quit()