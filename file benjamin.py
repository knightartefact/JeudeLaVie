import numpy as np
import matplotlib.pyplot as plt
import numpy.random as rd



# Fonction pour créer un terrain (carré) de côté de longueur n

def terrain(n):
    global T
    T=np.zeros((n,n))


# Fonction pour placer les cellules vivantes au départ (le tableau L(1xn) est la liste des coordonnées des cellules vivantes que l'on veut placer)

def cases_vivantes(L):
    for i in range(len(L)):
        T[L[i][0]][L[i][1]]=1


# Fonction auxiliaire pour trouver les coordonnées des cellules vivantes (CV est donc le tableau(1xn) contenant les coordonnées de cellules vivantes)

def vivantes(T):
    global CV
    CV=[]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]==1:
                CV.append([i,j])

# Fonction pour trouver les coordonnées des cellules mortes

def mortes(T):
    global CM
    CM=[]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]==0:
                CM.append([i,j])


''' Fonction auxiliaire pour faire naître une cellule (selon les règles données):
        Il faut créer une liste auxiliaire qui contient les coordonnées des cellules qui vont naitre
        ensuite, on utilise l'algo mortCell pour avoir la liste des coordonnées des cellules qui vont
        mourir. Enfin, on change la liste T avec l'algo iterationT.

        Dans une première étape on regarde les cellules vivantes puis on décide si elle vit ou si elle meurt, 
        ensuite on fait la même chose pour les cellules mortes puis on décide si elle vit ou si elle meurt; 
        ces modifications sont impléentées dans des listes temporaires puis à la fin de l'algo ont les transfère
        dans CV et CM pour ne pas faire d'interférences pendant le fonctionnement de l'algo
'''


def naissanceCell(CV,CM):
    for i in range(len(CV)):
        s = T[CV[i-1][0]][CV[i+1][1]] +T[CV[i-1][0]][CV[i][1]] +T[CV[i-1][0]][CV[i-1][1]] +T[CV[i][0]][CV[i-1][1]] +T[CV[i+1][0]][CV[i-1][1]] +T[CV[i+1][0]][CV[i][1]] +T[CV[i+1][0]][CV[i+1][1]] +T[CV[i][0]][CV[i+1][1]]

        



def mortCell():
    global CM
    CM=[]
    for i in range(len(T)):
        for j in range(len(T[0])):
            if T[i][j]==0:
                CM.append([i,j])





def JeuDeLaVie(n,L):
    terrain(n)
    cases_vivantes(L)
    for i in range(len(T)):
        for j in range(len(T[0])):




def affiche(M):
    plt.close()
    for i in range(len(M)):
        for j in range(len(M[0])):
            plt.fill([i,i+1,i+1,i,i],[j,j,j+1,j+1,j],color=C[M[i,j]])
    plt.xlim(0,n)
    plt.ylim(0,p)
    plt.axis('off')
    plt.show()

^^