# -*- coding: utf-8 -*-
### FAIT DE A a W par Dilien Oeuvrard.
### Seul les dessins ne viennent pas de moi !

from liste import *
from time import sleep
from os import system
from random import randint
import keyboard
import winsound


endurance = 100
chance = 0 # CHANCE DE FUITE AMELIORES || ACHETABLE EN BOUTIQUE et ENTRAINEMENT
force = 0 # DEGATS AMELIORES || ACHETABLE EN BOUTIQUE et ENTRAINEMENT
portefeuille = 0
force1 = 0
MIN = 20
MAX = 33
enduraide = 0

############################################################################## 
##############################################################################   
##############################################################################
# FONCTIONS SECONDAIRES

def clear(): #systeme de clear
    sleep(1)
    _ = system('cls')
    
def dormir(): #sert Ã  rien
    sleep(1)
    
def Suppr(lst, elm): # supprimer un horcrux d'une liste
    for i in range(len(lst)):
        if lst[i] == elm:
            lst.pop(i)
            return lst
    return None

def ajouter(lst, i): # pour ajouter un horcrux dans une liste
    lst.append(i)

############################################################################## 
##############################################################################   
##############################################################################
# SALLES

def visitez_salle(salle): #pour ouvrir une porte.
    if salle == 10: 
        print("Vous avez gagne !")
        return
    else: 
        print("Vous avez ouvert la porte de la salle numero", salle,"\n")
        sleep(2)
        return salle
    
def fouillez_salle(salle): # fouiller la salle (coffre / potion / horcrux)
    print("Un gros coffre vous attend,MAIS QUE CONTIENT-IL ??\n")
    print(coffre)
    while not keyboard.is_pressed('enter'):
            sleep
    piece = randint(1,3)
    if piece == 1:
        print("Malheuresement le coffre contient 0 Gallions\n")
        sleep(2)
        nb_piece = 0
    else:
        nb_piece = randint(101,500)*salle//2
        print(""" 

     _____
    /     \ 
   |   G   | X %d OR
    \_____/
    """%(nb_piece))
        sleep(2)
    return nb_piece

def potion(salle):
    potion = randint(1,3)
    if potion == 1:
       print("""                                 
                                /  )
                               /  / )
                          -   /  / / 
                             '  / / -
                            / _/ / /
                      _    / _/_, /          ,
                    + $$$ / _/_/_/          \       |
                  /- + $$/ _/_/_/      / 
                  \`_ $$/'_/_/    .    ______   _
                     \ (  / ___,_____ _ _____,
                     |  `(|/_,_,__ ________/
                     |.   |''_,_______)
                      \   (                           
                       \  / |-._      Un ange vous a soigne
                        \.' /|/ \_._
                        /_/   _/    /-'__
                          \     \'       \.___
                           '.   /,     |_/_   |._
                             \ / )   '.     '_/, )
                              (_(     -\_   /  \ \
                                 \__      |-'   |/
                                   \._  /_/_
                                      \_/\' )
                                          \ |
                                          |/                            Entrer
            """)
       while not keyboard.is_pressed('enter'):
            sleep
       endur = 50
    else:
        print("""
              (-)     
            .-'-'-.
            |-...-|  X 0 POTIONS
            |;:.._|  Il faudrat se battre sans potion
            `-...-' 
                                                                        Entrer
            """)

        while not keyboard.is_pressed('enter'):
            sleep
        endur = 0
    return endur

############################################################################## 
##############################################################################   
##############################################################################
# FONCTIONS DE COMBAT
    
def demonstre(x): #ATTAQUE DU MONSTRE
    while not keyboard.is_pressed('enter'):
            sleep
    de_monstre = randint(5,25)*x
    
    return de_monstre

def dejoueur(x): #ATTAQUE DU JOUEUR
    while not keyboard.is_pressed('enter'):
            sleep
    de_joueur = randint(5,25)
    return de_joueur

def ennemi(n, i): #gÃ©nÃ¨re un adversaire.
    print(monstres[i], "apparait devant vous et semble vous vouloir du mal ! A  vous de gagner en combattant ! Attention son nombre d'Hp est de ",n)
    endur_monstre = n
    if i == 0:
        print(ombragecombat)
    if i == 1:
        print(luciuscombat)
    if i == 2:
        print(bellatrixcombat)
    if i == 3:
        print(acromantulacombat)
    if i == 4:
        print(basiliccombat)
    if i == 5:
        print(detraqueurcombat)
    sleep(1)
    return endur_monstre
    

def combattre(endurance,endur_monstre): #pour departager les deux beligerants.
    combat = input(combat1)
    while combat != "demagique" and combat != "fuir":
        combat = input(combat1)
        
    if combat == "fuir":
        if chance >= 20:
            chancefuite = randint(1,2)
        else:
            chancefuite = randint(1,3)
        if chancefuite == 1:
            print("Votre Fuite a reussi\n")
            p = False
        else:
            print("Votre Fuite a echoue\n Le combat commence !")
            p = True
            
    elif combat == "demagique":
        p = True
    if p == False:
        return endurance
    while endurance > 0 and endur_monstre > 0:
        if force > 0:
            force1 = force // 20
            if force1 >= 1:
                deJ = dejoueur(1) + force1
                deM = demonstre(1)
            else:
                deJ = dejoueur(1)
                deM = demonstre(1)  
        else:
            deJ = dejoueur(1)
            deM = demonstre(1)
        if deM < deJ:
            endur_monstre -= deJ
            clear()
            print(""" 
                  \ _ /
                  /O O \   _                        z  z
                  \~~~ / // \                     z        z
                  /--\//   ))         z        z
             ()==/()== \__./  B z z z   z    z               z
             ()=(  ()= )                  z z
                 \____/                                        z z z
                  ||||
                 (/  \)         Points de vie Ennemi: %d                                                  
                        
                        
                        
                        
                            [Vous avez inflige %s dÃ©gats]
  
        !
      _.-._      /   
     __| |__    /
    /_ `-` _\  /                Point de vie Joueur: %d
    ||\___/\\ /
                                                                        Entrer
    """ %(endur_monstre,deJ,endurance))
            sleep(1)
        elif deM > deJ:
            endurance -= deM
            clear()
            print(""" 
                  \ _ /
                  /O O \   _                        z  z
                  \~~~ / // \                     z        z
                  /--\//   ))         z        z
             ()==/()== \__./  B z z z   z    z               z
             ()=(  ()= )                  z z
                 \____/                                        z z z
                  ||||
                 (/  \)         Points de vie Ennemi: %d 
                                                     

                        
                        
                            [L'ennemi vous a inflige %s degats]
  
        !
      _.-._      /   
     __| |__    /
    /_ `-` _\  /                Point de vie Joueur: %d
    ||\___/\\ /
                                                                        Entrer
    """ %(endur_monstre,deM,endurance))
            sleep(1)
    while not keyboard.is_pressed('enter'):
            sleep
    if endurance <= 0:
        clear()
        print(perdu)
        while not keyboard.is_pressed('enter'):
            sleep
        return endurance
    elif endur_monstre <= 0:
        clear()
        print(gagner)
        while not keyboard.is_pressed('enter'):
            sleep
        return endurance
    else:
        return endurance

############################################################################## 
##############################################################################   
##############################################################################
# ENTRAINEMENT

def entrainement(salle, j):
    print(entraineurs[j], "va vous entrainer pour vous faire devenir pour fort")
    if j == 0 :
        print(hg1)
        while not keyboard.is_pressed('enter'):
            sleep
        wl = input()
        print(hg2)
        winsound.PlaySound('hermionegranger.mp3',winsound.SND_ASYNC)
        while not keyboard.is_pressed('enter'):
            sleep
    if j == 1:
        print(hp1)
        while not keyboard.is_pressed('enter'):
            sleep
        st = input()
        while st != "Stupefix" and st != "stupefix" and st != "stupefix":
            st = input()
        print(hp2)
        while not keyboard.is_pressed('enter'):
            sleep
    if j == 2:
        print("Ron n'est pas la , tu es tombe sur le mauvais entraineur")

############################################################################## 
##############################################################################   
##############################################################################
# COMBAT BOSS

def deboss(x): #ATTAQUE DU MONSTRE
    while not keyboard.is_pressed('enter'):
            sleep
    de_boss = randint(30,100)*x
    
    return de_boss

def dejboss(x): #ATTAQUE DU JOUEUR
    while not keyboard.is_pressed('enter'):
            sleep
    dejoueurboss = randint(30,100)
            
    return dejoueurboss

def boss(z):
    endur_boss = z
    print("Voldemort Ã  ",endur_boss ,"HP")
    print(msgboss)
    while not keyboard.is_pressed('enter'):
            sleep
    return endur_boss

def combatboss(endurance,endur_boss):
    combatb = input(combatboss1)
    while combatb != "demagique" and combatb != "fuir":
        combatb = input(combatboss1)
        
    if combatb == "fuir":
        if chance >= 20:
            chancefuite = randint(1,3)
        else:
            chancefuite = randint(1,5)
        if chancefuite == 1:
            print("Votre Fuite a reussi\n")
            p = False
        else:
            print("Votre Fuite a echoue\n Le combat commence !")
            sleep(2)
            p = True
            
    elif combatb == "demagique":
        p = True
    if p == False:
        return endurance
    while endurance > 0 and endur_boss > 0:
        if force > 0:
            force1 = force // 20
            if force1 >= 1:
                deJb = dejboss(1) + force1
                deMb = deboss(1)
            else:
                deJb = dejboss(1)
                deMb = deboss(1)
        else:
            deJb = dejboss(1)
            deMb = deboss(1)
        enduraide = endurance // 2
        if endurance <= enduraide:
            p = randint(1,3)
            if p == 2:
                rendu = randint(10,75)
                endurance += rendu
                print("Un ange mysterieux est venu vous soigner durant le combat !\nVous avez recupere", rendu)
            
        if deMb < deJb:
            endur_boss -= deJb
            clear()
            print(""" 
                                                            .-````-.
                                                           /        \
                                                          /_        _\
                                                         // \      / \\
                 Points de vie Voldemort: %d             |\__\    /__/|
                                                          \    ||    /
                                                           \        /
                                                            \  __  / 
                                                             '.__.'
                                                              |  |
                      _________               
                     /        /                                       
                    /    0   /
                   /    0   / 
                  /________/    [Vous avez inflige %s degats]
  
        !
      _.-._      /   
     __| |__    /
    /_ `-` _\  /                Point de vie Joueur: %d
    ||\___/\\ /
                                                                        Entrer
    """ %(endur_boss,deJb,endurance))
            sleep(1)
        elif deMb > deJb:
            endurance -= deMb
            clear()
            print(""" 
                                                            .-````-.
                                                           /        \
                                                          /_        _\
                                                         // \      / \\
                 Points de vie Voldemort: %d             |\__\    /__/|
                                                          \    ||    /
                                                           \        /
                                                            \  __  / 
                                                             '.__.'
                                                              |  |
                      _________               
                     /        /                                       
                    /    0   /
                   /    0   / 
                  /________/    [L'ennemi vous a infligé %s degats]
  
        !
      _.-._      /   
     __| |__    /
    /_ `-` _\  /                Point de vie Joueur: %d
    ||\___/\\ /
                                                                        Entrer
    """ %(endur_boss,deMb,endurance))
            sleep(1)
    while not keyboard.is_pressed('enter'):
            sleep
    if endurance <= 0:
        clear()
        print(perduboss)
        while not keyboard.is_pressed('enter'):
            sleep
        gagner = False
    elif endur_boss <= 0:
        clear()
        print(gagnerboss)
        gagner = True
        while not keyboard.is_pressed('enter'):
            sleep
        return gagner
    else:
        return endurance
        