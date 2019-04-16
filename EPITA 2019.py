# -*- coding: utf-8 -*-
"""
Created on Mon Apr 15 21:51:46 2019

@author: El Zorro
"""

"""
Ecrire une focnction searchMatrix(M,x) qui retournere la position (i,j) de la 
première valeur x trouvée dans la matrice M (que l'on supposera non vide).
Si x n'est pas présent, la foncion retourne (-1,-1)
"""
def searchMatrix(M,x):
    for i in range(len(M)):
        k=0
        for j in M[i]:
            if j==x:
                return (i,k)
            else:
                k+=1
    return (-1,-1) #Si on arrive ici, c'est parce qu'on a rien trouvé
