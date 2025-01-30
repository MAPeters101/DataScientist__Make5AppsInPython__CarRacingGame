import pygame, sys, time, random
from pygame.locals import *

pygame.init()

width = 800
height = 600
FPS = 40 #Frame Rate
white = (255,255,255)
l_red = (255,0,0)
red = (150,0,0)
l_green = (0,255,0)
green = (0,150,0)
yellow = (255,229,10)
l_yellow = (212,255,10)
black = (0,0,0)
roadcolor = (47,47,47)

Display = pygame.display.set_mode((width,height)) # Display surface object
pygame.display.set_caption("The Car Racing")
clock = pygame.time.Clock()

CarImg = pygame.image.load("images/car.png")
RoadImg1 = pygame.image.load("images/road1.png")
TreeImg1 = pygame.image.load("images/longtree1.png")
TreeImg2 = pygame.image.load("images/longtree2.png")
Bugatti = pygame.image.load("images/bugatti.png")
GameIcon = pygame.image.load("images/gameicon.png")
pygame.display.set_icon(GameIcon)

life = 2
Previous_Score = DodgeCars(Display)
Previous_Score.Previous_Score()

EndGame = False
GamePaused = False






