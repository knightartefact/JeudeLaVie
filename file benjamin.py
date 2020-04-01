import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd



# Fonction pour créer un terrain (carré) de côté de longueur n

def terrain(n):
    global T
    T=np.zeros((n,n))


# Fonction pour placer les cases vivantes au départ

def cases_vivantes(L):
    for i in range(len(L)):
        T[L[i][0]][L[i][1]]=1








def affiche(M):
    plt.close()
    for i in range(len(M)):
        for j in range(len(M[0])):
            plt.fill([i,i+1,i+1,i,i],[j,j,j+1,j+1,j],color=C[M[i,j]])
    plt.xlim(0,n)
    plt.ylim(0,p)
    plt.axis('off')
    plt.show()