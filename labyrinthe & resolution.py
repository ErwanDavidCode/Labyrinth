# -*- coding: utf-8 -*-

#Import
import numpy as np
import random
import matplotlib.pyplot as plt
import time
import copy


#Class
class labyrinthe:
    def __init__(self, largeur=13, hauteur=13, ligne_entree=3, colonne_entree=3, ligne_sortie=12, colonne_sortie=12, pas=3, pad_width=0):
        self.largeur = largeur
        self.hauteur = hauteur
        self.carte = np.zeros((hauteur, largeur))
        self.pas = pas
        self.pad_width = pad_width
        
        #Sortie automatique la plus loin possible mais atteignable (multiple du pas)
        if ligne_entree and colonne_entree == "auto":
            self.ligne_entree = self.colonne_entree = 0
        else :
            self.ligne_entree = ligne_entree
            self.colonne_entree = colonne_entree
        
        if ligne_sortie and colonne_sortie == "auto":
            self.ligne_sortie = hauteur-1
            self.colonne_sortie = largeur-1
            while self.ligne_sortie % pas != 0 :
                self.ligne_sortie -=1
            while self.colonne_sortie % pas != 0 :
                self.colonne_sortie -=1
        else :       
            self.ligne_sortie = ligne_sortie
            self.colonne_sortie = colonne_sortie
    
        
    def marche(self):
        ligne_vivante = self.ligne_entree
        colonne_vivante = self.colonne_entree
        self.liste_positions = [(ligne_vivante, colonne_vivante)]
        n=0
        
        #on continue tant qu'on a pas atteint la sortie, liste pos = multiple du pas
        while len(self.liste_positions) != 0 :

            # on test chaque possibilité à chaque fois (donc pour chaque position)
            L = ["haut","droite","bas","gauche"]
            compteur = 0
            while len(L) != 0 : 
                deplacement = random.choice(L)
                n+=1
                

                if deplacement == "haut":
                    ligne_vivante = ligne_vivante-self.pas
                    
                    #si on peut faire l'action
                    if ((ligne_vivante >= 0 and ligne_vivante <= self.hauteur-1) and (colonne_vivante >= 0 and colonne_vivante <= self.largeur-1)) and not(self.carte[ligne_vivante,colonne_vivante] == 1) :
                        for i in range(self.pas):
                            #on remmplit les cases entre le point avant le saut et le saut (donc + car on a le saut = -pas ligne)
                            self.carte[ligne_vivante+i][colonne_vivante]=1
    
                            #on ajoute aux cases de futurs départs les cases multiples du pas
                            if i%self.pas==0:
                                "A OPTI ? si pas 3 on prend que 0"
                                self.liste_positions.append((ligne_vivante+i,colonne_vivante))
                        break
                    
                    else : 
                        L.remove("haut")
                        compteur += 1
                        ligne_vivante = ligne_vivante+self.pas
                    
                  
                elif deplacement == "droite":
                    colonne_vivante = colonne_vivante+self.pas
                    
                    if ((ligne_vivante >= 0 and ligne_vivante <= self.hauteur-1) and (colonne_vivante >= 0 and colonne_vivante <= self.largeur-1)) and not(self.carte[ligne_vivante,colonne_vivante] == 1) :
                        for i in range(self.pas):
                            self.carte[ligne_vivante][colonne_vivante-i]=1
                            if i%self.pas==0:
                                "A OPTI ? si pas 3 on prend que 0"
                                self.liste_positions.append((ligne_vivante,colonne_vivante-i))
                        break
                    
                    else : 
                        L.remove("droite")
                        compteur += 1 
                        colonne_vivante = colonne_vivante-self.pas


                elif deplacement == "bas":
                    ligne_vivante = ligne_vivante+self.pas
                    
                    if ((ligne_vivante >= 0 and ligne_vivante <= self.hauteur-1) and (colonne_vivante >= 0 and colonne_vivante <= self.largeur-1)) and not(self.carte[ligne_vivante,colonne_vivante] == 1) :
                        for i in range(self.pas):
                            self.carte[ligne_vivante-i][colonne_vivante]=1
                            if i%self.pas==0:
                                "A OPTI ? si pas 3 on prend que 0"
                                self.liste_positions.append((ligne_vivante-i,colonne_vivante))
                        break
                    
                    else : 
                        L.remove("bas")
                        compteur += 1 
                        ligne_vivante = ligne_vivante-self.pas


                elif deplacement == "gauche":
                    colonne_vivante = colonne_vivante-self.pas
                    
                    if ((ligne_vivante >= 0 and ligne_vivante <= self.hauteur-1) and (colonne_vivante >= 0 and colonne_vivante <= self.largeur-1)) and not(self.carte[ligne_vivante,colonne_vivante] == 1) :
                        for i in range(self.pas):
                            self.carte[ligne_vivante][colonne_vivante+i]=1
                            if i%self.pas==0:
                                "A OPTI ? si pas 3 on prend que 0"
                                self.liste_positions.append((ligne_vivante,colonne_vivante+i))
                        break
                    
                    else : 
                        L.remove("gauche")
                        compteur += 1
                        colonne_vivante = colonne_vivante+self.pas
                        
            #si on ne peut plus partir de cette case           
            if compteur == 4 :
                self.liste_positions.remove((ligne_vivante,colonne_vivante))
                if len(self.liste_positions) == 0:
                    break
                else :
                    choix = random.choice(self.liste_positions)
                    ligne_vivante = choix[0]
                    colonne_vivante = choix[1]

        self.carte = np.pad(self.carte, pad_width=self.pad_width, mode='constant',constant_values=0)
        
      
    def sortie(self):
        """Trouver la sortie dans le labyrinthe."""
        carte = self.carte

        # Coordonnées avec padding
        ligne_vivante, colonne_vivante = self.ligne_entree + self.pad_width, self.colonne_entree + self.pad_width
        ligne_sortie, colonne_sortie = self.ligne_sortie + self.pad_width, self.colonne_sortie + self.pad_width

        # Marquer l'entrée et la sortie
        carte[ligne_vivante][colonne_vivante] = 2
        carte[ligne_sortie][colonne_sortie] = 1
        avisiter = [(ligne_vivante, colonne_vivante)]

        # Compteur initial
        compteur = 1

        # Montée
        while carte[ligne_sortie][colonne_sortie] == 1:
            compteur += 1

            # Taille de la liste à chaque itération
            taille = len(avisiter)
            for _ in range(taille):
                ligne_vivante, colonne_vivante = avisiter[0]

                # Parcours des 4 directions
                for pos in [(ligne_vivante + 1, colonne_vivante), (ligne_vivante - 1, colonne_vivante),
                            (ligne_vivante, colonne_vivante + 1), (ligne_vivante, colonne_vivante - 1)]:

                    # Conditions de validité et exploration des chemins
                    if (0 <= pos[0] < len(carte)) and (0 <= pos[1] < len(carte[0])) and (carte[pos[0]][pos[1]] == 1):
                        carte[pos[0]][pos[1]] = compteur
                        avisiter.append(pos)

                # Retirer la position visitée
                avisiter.remove((ligne_vivante, colonne_vivante))

        # Descente
        ligne_vivante, colonne_vivante = ligne_sortie, colonne_sortie
        valeur = carte[ligne_sortie][colonne_sortie]

        while carte[self.ligne_entree + self.pad_width][self.colonne_entree + self.pad_width] == 2:
            for pos in [(ligne_vivante + 1, colonne_vivante), (ligne_vivante - 1, colonne_vivante),
                        (ligne_vivante, colonne_vivante + 1), (ligne_vivante, colonne_vivante - 1)]:

                if (0 <= pos[0] < len(carte)) and (0 <= pos[1] < len(carte[0])) and (
                        carte[pos[0]][pos[1]] == valeur - 1 or (pos == (self.ligne_entree + self.pad_width,
                                                                        self.colonne_entree + self.pad_width))):
                    valeur -= 1
                    ligne_vivante, colonne_vivante = pos
                    carte[ligne_vivante][colonne_vivante] = -1

                    
        #print(carte)
    
    def visualise(self):
        hauteur_pad = len(self.carte)
        largeur_pad = len(self.carte[0])
        map_jolie = np.zeros((hauteur_pad, largeur_pad,3))
        
        for ligne in range(hauteur_pad):
            for colonne in range(largeur_pad):
                if self.carte[ligne][colonne] >= 1:
                    map_jolie[ligne][colonne] = np.array([1,1,1])
                elif self.carte[ligne][colonne] == -1:
                    map_jolie[ligne][colonne] = np.array([0,1,1])
                    
                
        #Afficher entrée et sortie en couleur
        map_jolie[self.ligne_sortie+self.pad_width][self.colonne_sortie+self.pad_width] = np.array([1,0,0])
        map_jolie[self.ligne_entree+self.pad_width][self.colonne_entree+self.pad_width] = np.array([0,1,0])
        
        # Visualisation finale
        plt.clf()
        plt.axis("off")
        plt.imshow(map_jolie)
        # plt.savefig('path', format='png', dpi=300)
        plt.show() 
    


# =============================================================================
# #main
# =============================================================================
tic = time.time()

"""Il faut que x et y d'entrée (ou sortie) soient du même type : 'auto' ou saisie manuelle"""
carte = labyrinthe(101,101, "auto", "auto", "auto", "auto", 2, 1)
# Paramètres : 
# labyrinthe(largeur, hauteur, y_entrée, x_entrée, y_sortie, x_sortie, pas de la marche aléatoire)

carte.marche()
tac = time.time()
print("Temps pour créer le labyrinthe :", tac-tic, "sec")

carte.sortie()
toc=time.time()
print("Temps pour trouver la sortie :", toc-tac, "sec")


carte.visualise()
tuc = time.time()
print("Temps pour afficher le labyrinthe :", tuc-toc, "sec")
print("Temps totale algo:", tuc-tic, "sec")