import numpy
import random
import pygame
pygame.init()
pygame.display.init()

width=400
height=400
screen=pygame.display.set_mode((width,height))
white=pygame.Color(255,255,255)
resolution=40

#Array
def arrayCreate(cols,lignes):
    tab=numpy.zeros((lignes,cols))
    return tab

def comptageVoisins():
    for i in range(lignes):
        for j in range(cols):
            

#Initialisation
def setup():
    global grille
    global cols
    global lignes
    cols= int(width/resolution)
    lignes=int(height/resolution)
    grille=arrayCreate(cols,lignes)
    #Creation de la grille avec des cellules aléatoires (vives ou morts)
    for i in range(lignes):
        for j in range(cols):
            grille[i][j]=random.randint(0,1)
    draw()
    
#update

def draw():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run=False
                break
        for i in range(lignes):
            for j in range(cols):
                if grille[i][j]==1:
                    pygame.draw.rect(screen,white,(j*resolution,i*resolution,resolution-1,resolution-1))
        pygame.display.update()

setup()