import numpy
import pygame
pygame.init()
pygame.display.init()
screen=pygame.display.set_mode((400,400))

cols=10
lignes=10
#Array
def arrayCreate(cols,lignes):
    a=numpy.zeros((lignes,cols))
    #print(a)
    return a


#Initialisation
def setup():
    arrayCreate(cols,lignes)


