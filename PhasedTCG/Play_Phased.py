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