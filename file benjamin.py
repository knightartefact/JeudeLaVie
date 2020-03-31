import numpy as np
import matplotlib as plt
import numpy.random as rd





def affiche(M):
    plt.close()
    for i in range(len(M)):
        for j in range(len(M[0])):
            plt.fill([i,i+1,i+1,i,i],[j,j,j+1,j+1,j],color=C[M[i,j]])
    plt.xlim(0,n)
    plt.ylim(0,p)
    plt.axis('off')
    plt.show()


