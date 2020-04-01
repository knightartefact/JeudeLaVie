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
cols= int(width/resolution)
lignes=int(height/resolution)

grille=[]

#Array
def arrayCreate(cols,lignes):
    grille=numpy.zeros((lignes,cols))
    return grille

def enVie():
    
    print(grille)
    return grille

#Initialisation
def setup():
#Creation de la grille avec des cellules aléatoires (vives ou morts)

    grille=arrayCreate(cols,lignes)
    for i in range(lignes):
        for j in range(cols):
            grille[i][j]=random.randint(0,1)
            if grille[i][j]==1:
                pygame.draw.rect(screen,white,(j*resolution,i*resolution,resolution-1,resolution-1))
    pygame.display.update()



#update

def draw():
    run=True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:   
                run=False
                break

        screen.fill((0,0,0))
        pygame.display.update()
          

setup()