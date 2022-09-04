import pygame
import random

#Initialization
pygame.init()

#Create the screen
screen = pygame.display.set_mode((800, 600))

#Background
background = pygame.image.load('background.png')

#Caption and Icon
pygame.display.set_caption("space invaders")
icon = pygame.image.load('ufo (1).png')
pygame.display.set_icon(icon)

#Player
playerImg = pygame.image.load('spaceship (1).png')
playerX = 370
playerY = 480
playerX_change = 0

#Enemy
enemyImg = pygame.image.load('ghost.png')
enemyX = 370
enemyY = 50

enemyX = random.randint(0,736)
enemyY = random.randint(0,150)
enemyX_change = 0.3
enemyY_change = 40

#Bullet
#Ready - you cant see the bullet on the  screen
#Fire - the bullet is currently moving

bulletImg = pygame.image.load()
bulletX = 0
bulletY = 480
bulletX_change = 0
bulletY_change = 10
bullet_state = "ready"


def player():
    screen.blit(playerImg,(playerX,playerY))

def enemy():
    screen.blit(enemyImg,(enemyX,enemyY))

def fire_bullet():
    screen.blit(bulletImg,(bulletX,bulletY))



#Game loop
running = True
while running:
    #RGB = Red, Green, Blue
    screen.fill((0,0,0))

    #Background image
    screen.blit(background,(0,0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        #to check whether the keystroke pressed is left or right
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                playerX_change = -5
            if event.key == pygame.K_RIGHT:
                playerX_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0


    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736

    enemyX += enemyX_change
    if enemyX <= 0:
        enemyX_change = 0.3
        enemyY += enemyY_change

    if enemyX >= 736:
        enemyX_change = -0.3
        enemyY += enemyY_change



    player()
    enemy()
    pygame.display.update()