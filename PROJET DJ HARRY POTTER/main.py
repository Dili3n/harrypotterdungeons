# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 18:54:13 2020

@author: xarfy
"""
from fltk import *
from textes import *

from time import sleep
from random import randint
import winsound
import pygame

file = 'assets/musique/song.mp3'
filefight = 'assets/musique/battle.mp3'

pygame.init()
pygame.mixer.init()

def stats():
    
    texte(40, 60,(gallions))
    texte(1178,60,(endurance))
    texte(638,60,(nbhorcrux))

def combat(x):
    
    if x == 1:
            
        image(640,360,'assets/ombragecombat.png', ancrage = "center")
        
    elif x == 2:
        
        image(640,360,'assets/detraqueurcombat.png', ancrage = "center")
        
    elif x == 3:

        image(640,360,'assets/dragomcombat.png', ancrage = "center")
        
    elif x == 4:
        
        image(640,360,'assets/basiliccombat.png', ancrage = "center")
        
    stats()
    texte(500,230,(endurance_monstre))
    texte(750,570,(endurance))
    mise_a_jour()
    attend_clic_gauche()
    

largeur_plateau = 1280  # en nombre de cases
hauteur_plateau = 720  # en nombre de cases

cree_fenetre(largeur_plateau, hauteur_plateau)

gallions = 1000
endurance = 100
nbhorcrux = 0
nbballais = 0

i = 1
salle = 0

boucle = True

accueil = True
menu = False
entrainement = False
boutique = False
jeu = False
coffre = False

while boucle:
  
    print(aide)

    while accueil:
    
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
    
        image(640,360,'assets/bg.png', ancrage = "center")
        
        image(285, 387.5, 'assets/button1.png')
        image(985, 387.5, 'assets/button2.png')
            
        mise_a_jour()
        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            boucle = False
            pygame.mixer.music.stop()
            break
        if ty == 'ClicGauche':
            if 235 <= abscisse(ev) <= 335 and 287.5 <= ordonnee(ev) <= 487.5:
                accueil = False
                menu = True
            elif 935 <= abscisse(ev) <= 1035 and 287.5 <= ordonnee(ev) <= 487.5:
                boucle = False
                pygame.mixer.music.stop()
                break
            
    while menu:
        
        image(640,360,'assets/bgdebut.png', ancrage = "center")
        
        stats()
        
        image(645,370,'assets/button1.png', ancrage = "center")
        image(295,375,'assets/button3.png', ancrage = "center")
        image(995,375,'assets/button4.png', ancrage = "center")
        
        image(22.5,695,'assets/ballais.png', ancrage = "center")
        
        mise_a_jour()
        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            boucle = False
            pygame.mixer.music.stop()
            break
        
        if ty == 'ClicGauche':
            if 569 <= abscisse(ev) <= 724 and 250 <= ordonnee(ev) <= 479:
                menu = False
                jeu = True
            elif 217 <= abscisse(ev) <= 372 and 180 <= ordonnee(ev) <= 400:
                menu = False
                boutique = True
            elif 917 <= abscisse(ev) <= 1072 and 180 <= ordonnee(ev) <= 400:
                menu = False
                entrainement = True
            elif 10 <= abscisse(ev) <= 35 and 670 <= ordonnee(ev) <= 720:
                image(640,360,'assets/ballaisuse.png', ancrage = "center")
                attend_clic_gauche()
                salle += 1
                menu = False
                coffre = True
    
    while entrainement:
        
        gallions -= 100
        
        image(640,360,'assets/bgtextdebut.png', ancrage = "center")
        
        stats()
        
        mise_a_jour()
    
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            boucle = False
            pygame.mixer.music.stop()
            break
        
        chance_entraineur = randint(1,2)
        
        if chance_entraineur == 1:
            image(81,500,('assets/hermione.png'))
            texte(337,584,(hg1),taille = '16')
            texte(337,609,(hg1_2),taille = '16')
            mise_a_jour()
            attend_clic_gauche()
            image(640,360,'assets/bgtextdebut.png', ancrage = "center")
            stats()
            image(81,500,('assets/hermione.png'))
            texte(337,584,(hg2),taille = '16')
            mise_a_jour()
            pygame.mixer.music.pause()
            
            winsound.PlaySound('assets/musique/hermionegranger.wav',
                                   winsound.SND_FILENAME)
            pygame.mixer.music.unpause()
            endurance += 15
            attend_clic_gauche()
            entrainement = False
            menu = True
            
        elif chance_entraineur == 2:
            image(81,500,('assets/harry.png'))
            texte(337,584,(hp1),taille = '16')
            texte(337,609,(hp1_2),taille = '16')
            mise_a_jour()
            attend_clic_gauche()
            image(640,360,'assets/bgtextdebut.png', ancrage = "center")
            stats()
            image(81,500,('assets/harry.png'))
            texte(337,584,(hp2),taille = '16')
            mise_a_jour()
            endurance += 5
            attend_clic_gauche()
            entrainement = False
            menu = True
            
    
    while boutique:
        
        image(640,360,'assets/bgdebut.png', ancrage = "center")
        
        stats()
        
        image(240,360,'assets/boutique1.png', ancrage = "center")
        image(970,360,'assets/boutique2.png', ancrage = "center")
        image(1230,670,'assets/croix.png', ancrage = "center")
        
        mise_a_jour()
    
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            boucle = False
            pygame.mixer.music.stop()
            break
        
        if ty == 'ClicGauche':
            if 140 <= abscisse(ev) <= 340 and 300 <= ordonnee(ev) <= 460:
                if gallions >= 200:
                    gallions -= 200
                    endurance += 20
                    image(240,360,'assets/achataccept.png', ancrage = "center")
                else:
                    image(240,360,'assets/achatrefus.png', ancrage = "center")
                mise_a_jour()
                sleep(0.5)
            elif 870 <= abscisse(ev) <= 1070 and 300 <= ordonnee(ev) <= 460:
                if gallions >= 800:
                    gallions -= 800
                    nbballais += 1
                    image(970,360,'assets/achataccept.png', ancrage = "center")
                else:
                    image(970,360,'assets/achatrefus.png', ancrage = "center")
                mise_a_jour()
                sleep(0.5)  
            elif 1180 <= abscisse(ev) <= 1280 and 620 <= ordonnee(ev) <= 720:
                boutique = False
                menu = True
        
    
    while jeu:
        
        pygame.mixer.music.stop
        pygame.mixer.music.load(filefight)
        pygame.mixer.music.play(-1)
        
        salle += 1
        endurance_monstre = (randint(30, 50))*salle
        combatrandom = randint(1,4)
        
        combat(combatrandom)       
            
        while endurance_monstre > 0 and endurance > 0:
            chancetape = randint(1,2)
            if chancetape == 1:         
                    
                degat2 = randint(5,20)
                endurance -= degat2
                    
                if combatrandom == 1:
                    image(640,360,'assets/ombragedegat.png'
                              , ancrage = "center")
                        
                elif combatrandom == 2:
                    image(640,360,'assets/detraqueurdegat.png'
                              , ancrage = "center")
                        
                elif combatrandom == 3:
                    image(640,360,'assets/dragomdegat.png'
                              , ancrage = "center")
                        
                elif combatrandom == 4:
                    image(640,360,'assets/basilicdegat.png'
                              , ancrage = "center")
                        
                stats()
                    
                texte(720,380,(degat2))
                    
                texte(500,230,(endurance_monstre))
                texte(750,570,(endurance))
                mise_a_jour()
                attend_clic_gauche()
                    
            elif chancetape == 2:
        
                degat1 = randint(5,20)
                endurance_monstre -= degat1
            
                if combatrandom == 1:
                    image(640,360,'assets/ombragedegat2.png'
                              , ancrage = "center")
                        
                elif combatrandom == 2:
                    image(640,360,'assets/detraqueurdegat2.png'
                              , ancrage = "center")
                        
                elif combatrandom == 3:
                    image(640,360,'assets/dragomdegat2.png'
                              , ancrage = "center")
                        
                elif combatrandom == 4:
                    image(640,360,'assets/basilicdegat2.png'
                              , ancrage = "center")
                        
                stats()
                    
                texte(720,380,(degat1))
                    
                texte(500,230,(endurance_monstre))
                texte(750,570,(endurance))
                mise_a_jour()
                attend_clic_gauche()
                    
        if endurance_monstre <= 0:
                
                image(640,360,'assets/gagne.png', ancrage = "center")
                stats()
                texte(750,570,(endurance))
                mise_a_jour()
                attend_clic_gauche()
                jeu = False
                coffre = True
                continue
            
        elif endurance <= 0:
                if combatrandom == 1:
                        image(640,360,'assets/perduombrage.png'
                              , ancrage = "center")
                        
                elif combatrandom == 2:
                        image(640,360,'assets/perdudetraqueur.png'
                              , ancrage = "center")
                        
                elif combatrandom == 3:
                        image(640,360,'assets/perdudragom.png'
                              , ancrage = "center")
                        
                elif combatrandom == 4:
                        image(640,360,'assets/perdubasilic.png'
                              , ancrage = "center")
                stats()
                texte(750,570,(endurance))
                mise_a_jour()
                attend_clic_gauche()
                boucle = False
                pygame.mixer.music.stop()
                break
            
            
    while coffre:
        
        # gestion des événements
        ev = donne_ev()
        ty = type_ev(ev)
        
        if ty == 'Quitte':
            boucle = False
            pygame.mixer.music.stop()
            break

        image(640,360,'assets/butin.png', ancrage = "center")
        stats()
        
        horcruxchance = randint(0,1)
        texte(400, 575,(horcruxchance))
        nbhorcrux += horcruxchance
            
        gallionsplus = randint(1,50)*salle
        texte(200, 290,(gallionsplus))
        gallions += gallionsplus
            
        enduranceplus = randint(1,50)
        texte (850,260,(enduranceplus))
        endurance += enduranceplus
        
        mise_a_jour()
        
        sleep(0.5)
        
        attend_clic_gauche()
        
        pygame.mixer.music.stop()
        pygame.mixer.music.load(file)
        pygame.mixer.music.play(-1)
        coffre = False
        menu = True  
        
        efface_tout()
    
        
ferme_fenetre()
