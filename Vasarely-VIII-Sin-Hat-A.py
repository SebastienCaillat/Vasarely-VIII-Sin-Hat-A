#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Programme en Python 3 pour dessiner une œuvre de
Victor Vasarely
Titre : VIII Sin-Hat-A
Année : 1974

Accessoirement permet de compter le nombre de triangles rouges, 
comme l'exercice 86, page 73
Nathan Trans Math 6ème | Programme 2016

La figure est tracée dans un premier temps tournée de 90°
avec des triangles vers le haut ou vers le bas
puis tournée comme sur l'original

Created on Oct 14, 2018
@author: Sébastien C.
"""
import matplotlib.pyplot as plt
# définition des fonctions
def TraceTriH(X,Y,C) : # Trace triangle vers le haut (coordonnées x, y, couleur)
    global nbH
    nbH+=1
    x=[X-1,X  ,X-0.5,X-1]
    y=[Y,Y,Y+1 ,Y]
    ax.fill (x,y,c=C)
    if pointil : ax.plot (x,y,'k',linewidth=0.7)
    if coordonnees : ax.text(X-0.8,Y+0.1,'('+str(X)+','+str(Y)+')', size=4)
    global nbRouge
    if C is 'red': 
        nbRouge+=1
        if numero : ax.text(X-0.7,Y+0.2,str(nbRouge), size=4)

def TraceTriB(X,Y,C) :# Trace triangle vers le haut (coordonnées x, y, couleur)
    global nbB
    nbB+=1
    x=[X-0.5,X,X+0.5,X-0.5]
    y=[Y+1,Y,Y+1,Y+1]
    ax.fill (x,y,c=C)
    if pointil : ax.plot (x,y,'k',linewidth=0.7)
    if coordonnees : ax.text(X,Y+0.8,'('+str(X)+','+str(Y)+')', size=4)
    global nbRouge
    if C is 'red': 
        nbRouge+=1
        if numero : ax.text(X-0.3,Y+0.6,str(nbRouge), size=4)

#-------------------Choix des options --------------------------------------
coordonnees=False   # Affiches coordonnées sur les triangles (True/False)
pointil=False       # Sépare les triages par des trais (True/False)
numero=False        # Affiche numéro des rouges sur la figure
compte=True         # Affiche nombre de traingles & losanges rouges
tourne=True         # Tourne image comme dans exercice
                    # Mettre à False si Scipy non présent
    
NomFichier='Vasarely-VIII-Sin-Hat-A' # Nom du fichier à sauver
# ------------------Fin choix des options ----------------------------------

# Initalisation des  compteurs
nbH=0       # Nombre de triangles vers le haut
nbB=0       # Nombre de triangles vers le bas
nbRouge=0   # Nombre de triangles rouges

# Début traçage de la figure
# Les triangles sont regroupés par couleur et zones,
# du centre vers l’extérieur.
# La figure est tracée dans un premier temps tournée de 90°
# avec des triangles vers le haut ou vers le bas

fig,ax=plt.subplots()

bleuclairmoyen='royalblue'
TraceTriH (0,0,bleuclairmoyen)
TraceTriB (-0.5,-1,bleuclairmoyen)

TraceTriH (-2,0,bleuclairmoyen)
TraceTriB (-2.5,-1,bleuclairmoyen)
TraceTriH (-1.5,1,bleuclairmoyen)
TraceTriB (-2,0,bleuclairmoyen)
TraceTriH (-1,2,bleuclairmoyen)
TraceTriB (-1.5,1,bleuclairmoyen)

TraceTriB (2.5,-1,bleuclairmoyen)
TraceTriH (2.5,-1,bleuclairmoyen)
TraceTriB (2,-2,bleuclairmoyen)
TraceTriH (2,-2,bleuclairmoyen)

TraceTriB (-2,4,bleuclairmoyen)
TraceTriB (-1,4,bleuclairmoyen)
TraceTriH (-1,4,bleuclairmoyen)
TraceTriB (0,4,bleuclairmoyen)
TraceTriH (0,4,bleuclairmoyen)
TraceTriB (1,4,bleuclairmoyen)
TraceTriH (1,4,bleuclairmoyen)
TraceTriB (2,4,bleuclairmoyen)
TraceTriH (2,4,bleuclairmoyen)
TraceTriH (3,4,bleuclairmoyen)

TraceTriB (-2.5,-5,bleuclairmoyen)
TraceTriH (-2,-4,bleuclairmoyen)
TraceTriB (-3,-4,bleuclairmoyen)
TraceTriH (-2.5,-3,bleuclairmoyen)
TraceTriB (-3.5,-3,bleuclairmoyen)
TraceTriH (-3,-2,bleuclairmoyen)
TraceTriB (-4,-2,bleuclairmoyen)
TraceTriH (-3.5,-1,bleuclairmoyen)
TraceTriB (-4.5,-1,bleuclairmoyen)
TraceTriH (-4,0,bleuclairmoyen)

TraceTriB (5.5,-1,bleuclairmoyen)
TraceTriH (6,0,bleuclairmoyen)
TraceTriB (5,-2,bleuclairmoyen)
TraceTriH (5.5,-1,bleuclairmoyen)
TraceTriB (4.5,-3,bleuclairmoyen)
TraceTriH (5,-2,bleuclairmoyen)
TraceTriB (4,-4,bleuclairmoyen)
TraceTriH (4.5,-3,bleuclairmoyen)
TraceTriB (3.5,-5,bleuclairmoyen)
TraceTriH (4,-4,bleuclairmoyen)
TraceTriB (3,-6,bleuclairmoyen)
TraceTriH (3.5,-5,bleuclairmoyen)

bleufonce='blue'
TraceTriB (-1,2,bleufonce)
TraceTriB (0,2,bleufonce)
TraceTriB (1,2,bleufonce)
TraceTriH (0,2,bleufonce)
TraceTriH (1,2,bleufonce)
TraceTriH (2,2,bleufonce)

TraceTriB (2,-6,bleufonce)
TraceTriH (3,-6,bleufonce)
TraceTriB (1,-6,bleufonce)
TraceTriH (2,-6,bleufonce)
TraceTriB (0,-6,bleufonce)
TraceTriH (1,-6,bleufonce)
TraceTriB (-1,-6,bleufonce)
TraceTriH (0,-6,bleufonce)
TraceTriB (-2,-6,bleufonce)
TraceTriH (-1,-6,bleufonce)
TraceTriB (-3,-6,bleufonce)
TraceTriH (-2,-6,bleufonce)

bleuclair='deepskyblue'
TraceTriH (1,0,bleuclair)
TraceTriB (0,0,bleuclair)

TraceTriB (1,0,bleuclair)
TraceTriH (2,0,bleuclair)
TraceTriH (1.5,1,bleuclair)
TraceTriB (1.5,-1,bleuclair)
TraceTriH (1.5,-1,bleuclair)
TraceTriB (1,-2,bleuclair)

TraceTriB (-2,2,bleuclair)
TraceTriH (-2,2,bleuclair)
TraceTriB (-2.5,1,bleuclair)
TraceTriH (-2.5,1,bleuclair)
TraceTriB (-3,0,bleuclair)
TraceTriH (-3,0,bleuclair)

TraceTriB (2.5,3,bleuclair)
TraceTriH (3.5,3,bleuclair)
TraceTriB (3,2,bleuclair)
TraceTriH (4,2,bleuclair)
TraceTriB (3.5,1,bleuclair)
TraceTriH (4.5,1,bleuclair)
TraceTriB (4,0,bleuclair)
TraceTriH (5,0,bleuclair)

TraceTriB (-3.5,-5,bleuclair)
TraceTriH (-2.5,-5,bleuclair)
TraceTriB (-4,-4,bleuclair)
TraceTriH (-3,-4,bleuclair)
TraceTriB (-4.5,-3,bleuclair)
TraceTriH (-3.5,-3,bleuclair)
TraceTriB (-5,-2,bleuclair)
TraceTriH (-4,-2,bleuclair)
TraceTriB (-5.5,-1,bleuclair)
TraceTriH (-4.5,-1,bleuclair)

violet='darkviolet'
TraceTriB (1.5,1,violet)
TraceTriH (2.5,1,violet)
TraceTriB (2,0,violet)
TraceTriH (3,0,violet)

TraceTriB (-2,-4,violet)
TraceTriH (-1,-4,violet)
TraceTriB (-1,-4,violet)
TraceTriH (-0,-4,violet)
TraceTriB (0,-4,violet)
TraceTriH (1,-4,violet)
TraceTriB (1,-4,violet)
TraceTriH (2,-4,violet)

TraceTriB (-2.5,5,violet)
TraceTriH (-2.5,5,violet)
TraceTriB (-3,4,violet)
TraceTriH (-3,4,violet)
TraceTriB (-3.5,3,violet)
TraceTriH (-3.5,3,violet)
TraceTriB (-4,2,violet)
TraceTriH (-4,2,violet)
TraceTriB (-4.5,1,violet)
TraceTriH (-4.5,1,violet)
TraceTriB (-5,0,violet)
TraceTriH (-5,0,violet)

rouge='red'
TraceTriB (0.5,-1,rouge)
TraceTriH (0.5,-1,rouge)

TraceTriH (0.5,1,rouge)
TraceTriB (0.5,1,rouge)
TraceTriB (-0.5,1,rouge)
TraceTriH (-0.5,1,rouge)
TraceTriB (-1,0,rouge)
TraceTriH (-1,0,rouge)

TraceTriH (-1.5,-1,rouge)
TraceTriB (-2,-2,rouge)
TraceTriH (-1,-2,rouge)
TraceTriB (-1.5,-3,rouge)

TraceTriH (-1.5,3,rouge)
TraceTriB (-1.5,3,rouge)
TraceTriH (-0.5,3,rouge)
TraceTriB (-0.5,3,rouge)
TraceTriH (0.5,3,rouge)
TraceTriB (0.5,3,rouge)
TraceTriH (1.5,3,rouge)
TraceTriB (1.5,3,rouge)

TraceTriH (2.5,-3,rouge)
TraceTriB (2,-4,rouge)
TraceTriH (3,-2,rouge)
TraceTriB (2.5,-3,rouge)
TraceTriH (3.5,-1,rouge)
TraceTriB (3,-2,rouge)

TraceTriH (-1.5,-5,rouge)
TraceTriB (-1.5,-5,rouge)
TraceTriH (-0.5,-5,rouge)
TraceTriB (-0.5,-5,rouge)
TraceTriH (0.5,-5,rouge)
TraceTriB (0.5,-5,rouge)
TraceTriH (1.5,-5,rouge)
TraceTriB (1.5,-5,rouge)

TraceTriH (3.5,5,rouge)
TraceTriB (3,4,rouge)
TraceTriH (4,4,rouge)
TraceTriB (3.5,3,rouge)
TraceTriH (4.5,3,rouge)
TraceTriB (4,2,rouge)
TraceTriH (5,2,rouge)
TraceTriB (4.5,1,rouge)
TraceTriH (5.5,1,rouge)
TraceTriB (5,0,rouge)

vertclair='lime'
TraceTriH (1,-2,vertclair)
TraceTriB (0,-2,vertclair)
TraceTriH (0,-2,vertclair)
TraceTriB (-1,-2,vertclair)
TraceTriH (-0.5,-1,vertclair)
TraceTriB (-1.5,-1,vertclair)

TraceTriH (-2.5,-1,vertclair)
TraceTriB (-3.5,-1,vertclair)
TraceTriH (-2,-2,vertclair)
TraceTriB (-3,-2,vertclair)
TraceTriH (-1.5,-3,vertclair)
TraceTriB (-2.5,-3,vertclair)

TraceTriH (3.5,1,vertclair)
TraceTriB (3,0,vertclair)
TraceTriH (3,2,vertclair)
TraceTriB (2.5,1,vertclair)
TraceTriH (2.5,3,vertclair)
TraceTriB (2,2,vertclair)

TraceTriH (4.5,-1,vertclair)
TraceTriB (4.5,-1,vertclair)
TraceTriH (4,-2,vertclair)
TraceTriB (4,-2,vertclair)
TraceTriH (3.5,-3,vertclair)
TraceTriB (3.5,-3,vertclair)
TraceTriH (3,-4,vertclair)
TraceTriB (3,-4,vertclair)
TraceTriH (2.5,-5,vertclair)
TraceTriB (2.5,-5,vertclair)

TraceTriH (-3.5,1,vertclair)
TraceTriB (-4,0,vertclair)
TraceTriH (-3,2,vertclair)
TraceTriB (-3.5,1,vertclair)
TraceTriH (-2.5,3,vertclair)
TraceTriB (-3,2,vertclair)
TraceTriH (-2,4,vertclair)
TraceTriB (-2.5,3,vertclair)

vertfonce='mediumseagreen'
TraceTriB (1.5,-3,vertfonce)
TraceTriH (1.5,-3,vertfonce)
TraceTriB (0.5,-3,vertfonce)
TraceTriH (0.5,-3,vertfonce)
TraceTriB (-0.5,-3,vertfonce)
TraceTriH (-0.5,-3,vertfonce)

TraceTriB (3.5,-1,vertfonce)
TraceTriH (4,0,vertfonce)

TraceTriB (2.5,5,vertfonce)
TraceTriH (2.5,5,vertfonce)
TraceTriB (1.5,5,vertfonce)
TraceTriH (1.5,5,vertfonce)
TraceTriB (0.5,5,vertfonce)
TraceTriH (0.5,5,vertfonce)
TraceTriB (-0.5,5,vertfonce)
TraceTriH (-0.5,5,vertfonce)
TraceTriB (-1.5,5,vertfonce)
TraceTriH (-1.5,5,vertfonce)

ax.set_aspect('equal', 'box')   # Permet que les axes soient proportionnés
plt.axis('off')                 # Empeche affichage des axes

# Enregistre image tournée de 90°
NomFichier='Vasarely-VII-Sin-Hat-A' # Nom du fichier à sauver
plt.savefig(NomFichier+'-tourne.jpeg',dpi=300,bbox_inches='tight')
plt.show() # Affiche image

# Affiche nombre de triangles et losanges rouges
if compte :
    print ('Nombre de triangles rouges : ',nbRouge,'/',nbH+nbB)
    print ('Nombre de losanges rouges : ',nbRouge/2,'/',(nbH+nbB)/2)

# Tourne l'image comme l'exercice 86 page 73
if tourne :
    from scipy import ndimage  # Attention nécessite scipy 
    import matplotlib.image as mpimg
    figure=mpimg.imread(NomFichier+'-tourne.jpeg') # lecture de l'image 
    figureTourne = ndimage.interpolation.rotate(figure, -90,reshape=True) # rotation
    plt.imshow(figureTourne) 
    plt.axis('off')
    plt.savefig(NomFichier+'-Exercice-86.jpeg',dpi=300,bbox_inches='tight')
    plt.show() 
