#Important
VERSION_NUMBER = "v-0.0.1 Beta"

#Imports
import pygame,sys,os,math,time,pygame.gfxdraw,random
from pygame.locals import *


#Constants
PGNAME = "Phased Between Realms"
BGCOLOR = (255,255,255)
FPSCOLOR = (64,64,64)
FPS_MAX = 90
DATA_DIR = "Data"

#Inits
pygame.init()
clock = pygame.time.Clock()

#Screen
screen = pygame.display.set_mode((540,370))
pygame.display.set_caption(PGNAME)
pygame.display.set_icon(pygame.image.load("Data/Icon.jpg"))
screen.fill(BGCOLOR)

screen.blit(pygame.transform.scale(pygame.image.load("Data/FlamoLogo.jpg"),(540,370)),(0,0))

pygame.display.update()

time.sleep(2)

#Load Resources
#cd data
os.chdir(DATA_DIR)

font = pygame.font.Font("PressStart2P.ttf",20)
BGP = pygame.image.load("BGP.jpg")

#Cursor
CURSOR = (               #sized 24x24
  "               o        ",
  "              X         ",
  "            XX         o",
  "           XX        XXX",
  "         ......     XXX ",
  "       ..oooooo..  XXX  ",
  "      .oo  XX  oo.XXX   ",
  "     .o    XX XXXo.     ",
  "     .o   XXXXXXXo.     ",
  "    .o    XXXX    o.    ",
  "    .o    XXXX    o.    ",
  "   X.oXXXXXXXXXXXXo.X   ",
  "   X.oXXXXXXXXXXXXo.X   ",
  "    .o    XXXX    o.    ",
  "    .o    XXXX    o.    ",
  "     .oXXXXXXX   o.     ",
  "     .oXXX XX    o.     ",
  "   XXX.oo  XX  oo.      ",
  "  XXX  ..oooooo..       ",
  " XXX     ......         ",
  "XXX        XX           ",
  "o         XX            ",
  "         X              ",
  "        o               ",
)

cursor = pygame.cursors.compile(CURSOR)

pygame.mouse.set_cursor((24,24),(12,12),cursor[0],cursor[1])

#Screen
Screen = pygame.display.set_mode((1300,800))

#Add version Number
BGP.blit(font.render(str(VERSION_NUMBER),0,(200,200,200)),(300,200))

#Blit BG
screen.blit(BGP,(0,0))
pygame.display.update()

#Startup loop
flag = 0
while True:

    for event in pygame.event.get():

        #Did the user quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        #Did the user press space?
        if event.type == KEYDOWN:
            if event.unicode == " ":
                flag = 1

    if flag:
        break
        
# Main loop

while True:
    
    #Load game screen
    Bfield = pygame.image.load("BattleField.jpg")
    screen.blit(Bfield,(0,0))
    pygame.display.update()
    
    for event in pygame.event.get():

        #Did the user quit?
        if event.type == QUIT:
            pygame.quit()
            sys.exit()