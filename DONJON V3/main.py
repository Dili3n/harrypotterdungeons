# CREATION PAR DILIEN OEUVRARD
# LE 12 / 01 / 2021

import pickle
from tkfr import *
from time import sleep
from random import randint
from textes import *
import math
import winsound
import pygame

##############################################################################
#                           VARIABLES PRINCIPALES                            #
##############################################################################


# VARIABLES POUR GERER LE JOUEUR.
experience = 0
niveau =  1
salle = 0
horcrux = 0
ballais = 0
energie = 100
gallions = 800
force = 0
chance = 0

# VARIABLES BOULEENNES POUR GERER LES MENUS.
main = True
accueil = True
menu = False
entrainement = False
boutique = False
jeu = False
boss = False
coffre = False
inventaire = False

# MUSIQUES.

file = 'assets/musique/song.mp3'
filefight = 'assets/musique/battle.mp3'

## FENETRE EN PIXELS ! 
largeur_plateau = 1280
hauteur_plateau = 720
## 

##############################################################################
#                               LES FONCTIONS                                #
##############################################################################

def fin_game():

    save = [0,0,0,0,0,100,200,0,0] 
    fichier = open("save.txt", "wb")
    pickle.dump(save,fichier)
    fichier.close()

def sauvegarde(experience,niveau,salle,horcrux,ballais,energie,gallions,force,chance):

    """
    Fontion utilisée pour sauvegarder une partie en cours.
    La sauvegarde comprend, qui été en train de jouer,
    le nom des joueurs, la date de création de la partie,
    l'échiquier ainsi que l'emplacement des pièces.
    La fonction ouvre un fichier txt pour ensuite y écrire les
    informations.
    """
    save = [experience,niveau,salle,horcrux,ballais,energie,gallions,force,chance] 
    fichier = open("save.txt", "wb")
    pickle.dump(save,fichier)
    fichier.close()

def recuperation():

    """
    Fonction utilisée pour récupérer une sauvegarde dans le fichier
    save.txt
    """
    fichier = open("save.txt", "rb")
    save = pickle.load(fichier)
    fichier.close()
    return save

def fin():
    accueil = False
    menu = False
    entrainement = False
    boutique = False
    jeu = False
    boss = False
    coffre = False
    pygame.mixer.music.stop()   

def stats():
    
    texte(40, 60,(gallions))
    texte(1178,60,(energie))
    texte(638,60,(horcrux))

def affiche_accueil(file):

    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)

    image(640,360,'assets/bg.png', ancrage = "center")
    image(285, 387.5, 'assets/button1.png')
    image(985, 387.5, 'assets/button2.png')

def clic_accueil(event):

    if 235 <= abscisse(event) <= 335 and 287.5 <= ordonnee(event) <= 487.5:
        return False, True, True

    elif 935 <= abscisse(event) <= 1035 and 287.5 <= ordonnee(event) <= 487.5:
        return False, False, False
    else: return True, False, True

def affiche_menu(experience,niveau,force,chance):

    image(640,360,'assets/bgdebut.png', ancrage = "center")
    texte(1150,655,(str("Force ")+str(force)),taille = 18,couleur="saddle brown")
    texte(1150,685,(str("Chance ")+str(chance)),taille = 18,couleur="saddle brown")
    affiche_xp_bar(experience,niveau)
    stats()
    image(645,370,'assets/button1.png', ancrage = "center")
    image(295,375,'assets/button3.png', ancrage = "center")
    image(995,375,'assets/button4.png', ancrage = "center")
    image(22.5,695,'assets/ballais.png', ancrage = "center")

def affiche_xp_bar(experience,niveau):

    texte(460,690,str(niveau),couleur="saddle brown",taille=18)
    if 0 <= experience < 25:
        image(600,705,'assets/xp_bar.png', ancrage = "center")
    elif 25 <= experience < 50: 
        image(600,705,'assets/xp_bar1.png', ancrage = "center")
    elif 50 <= experience < 75:
        image(600,705,'assets/xp_bar2.png', ancrage = "center")
    elif 75 <= experience < 95:
        image(600,705,'assets/xp_bar3.png', ancrage = "center")
    elif 95 <= experience <= 10000:
        image(600,705,'assets/xp_bar4.png', ancrage = "center")

def clic_menu(event,ballais,horcrux):

     if 569 <= abscisse(event) <= 724 and 250 <= ordonnee(event) <= 479:
         if horcrux < 7:
            return False, True, False, False, False, ballais, False
         else: return False, False, False, False, False, ballais, True
     elif 217 <= abscisse(event) <= 372 and 180 <= ordonnee(event) <= 400:
         return False, False, True, False, False, ballais, False
     elif 917 <= abscisse(event) <= 1072 and 180 <= ordonnee(event) <= 400:
        return False, False, False, True, False, ballais, False
     elif 10 <= abscisse(event) <= 35 and 670 <= ordonnee(event) <= 720 and ballais >= 1:
        return False, False, False, False, True, ballais-1, False    
     else: return True, False, False, False, False, ballais, False

def leave():

    return False, False, False, False, False,False, False, False

def affiche_entrainement(gallions):

    if gallions >= 100:
        image(640,360,'assets/bgtextdebut.png', ancrage = "center")
        mise_a_jour()
        return gallions - 100, True, False
    else:
        return gallions, False, True

def chance_entraineur():

    chance_train = randint(1,2)
    if chance_train == 1:
        hermione_train()
    else:
        harry_train()

def hermione_train():

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
    attend_clic_gauche()

def harry_train():

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
    attend_clic_gauche()

def recompense_train(energie,experience):

    experience += randint(1,50)
    energie_chance = randint(1,25)
    return experience, energie + energie_chance

def fin_entrainement():

    return False, True

def affiche_boutique():

    image(640,360,'assets/bgdebut.png', ancrage = "center") 
    stats()   
    image(240,360,'assets/boutique1.png', ancrage = "center")
    image(970,360,'assets/boutique2.png', ancrage = "center")
    image(1230,670,'assets/croix.png', ancrage = "center")
    mise_a_jour()

def achat_boutique(gallions,energie,ballais):

    if 140 <= abscisse(event) <= 340 and 300 <= ordonnee(event) <= 460:
        if gallions >= 200:
            gallions -= 200
            energie += 20     
            verification_achat(1,0)
        else:
            verification_achat(0,0)

    elif 870 <= abscisse(event) <= 1070 and 300 <= ordonnee(event) <= 460:
        if gallions >= 800:
            gallions -= 800
            ballais += 1
            verification_achat(1,1)
        else:
            verification_achat(0,1)

    elif 1180 <= abscisse(event) <= 1280 and 620 <= ordonnee(event) <= 720:
        return gallions, energie, ballais, False, True
    
    return gallions, energie, ballais, True, False


def verification_achat(indice, y):
    
    if indice == 1 and y == 0:
        image(240,360,'assets/achataccept.png', ancrage = "center")
    elif indice == 0 and y == 0:
        image(240,360,'assets/achatrefus.png', ancrage = "center")
    elif indice == 1 and y == 1:
        image(970,360,'assets/achataccept.png', ancrage = "center")
    elif indice == 0 and y == 1:
        image(970,360,'assets/achatrefus.png', ancrage = "center")
    mise_a_jour()
    sleep(0.5)

def setup_combat(salle, x):

    pygame.mixer.music.stop
    pygame.mixer.music.load(filefight)
    pygame.mixer.music.play(-1)

    salle += 1
    if x == 0:
        endurance_monstre = (randint(30, 50))*((salle//2)+1)
    else: endurance_monstre = (randint(50, 75))*((salle//2)+1) 
    combat_random = randint(1,4)
    combat(combat_random, endurance_monstre)
    return salle, endurance_monstre, combat_random

def combat(x, endurance_monstre):

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
    texte(750,570,(energie))
    mise_a_jour()
    attend_clic_gauche()

def can_hit(energie, endurance_monstre, combat_random,salle,force,chance):

    if chance < 30:
        chance_tape = randint(1,2)
    else: chance_tape = randint(1,3) 
    if chance_tape == 1 or chance_tape == 3:
        degat = randint(5,20)*((force//100)+1)
        endurance_monstre -= degat
        aff_degat_joueur(degat, combat_random, energie, endurance_monstre)
        return energie, endurance_monstre
    else:
        degat = randint(1,5)*salle
        energie -= degat
        aff_degat_monstre(degat, combat_random, energie, endurance_monstre)
        return energie, endurance_monstre 

def aff_degat_joueur(degat, x, energie, endurance_monstre):

    if x == 1:
        image(640,360,'assets/ombragedegat2.png', ancrage = "center")
    elif x == 2:
        image(640,360,'assets/detraqueurdegat2.png', ancrage = "center")
    elif x == 3:
        image(640,360,'assets/dragomdegat2.png', ancrage = "center")
    elif x == 4:
        image(640,360,'assets/basilicdegat2.png', ancrage = "center")
    stats()            
    texte(720,380,(degat)) 
    if endurance_monstre < 0:
        texte(520,230,("0"))
    else: texte(520,230,(endurance_monstre))
    texte(750,570,(energie))
    mise_a_jour()
    attend_clic_gauche()

def aff_degat_monstre(degat, x, energie, endurance_monstre):

    if x == 1:
        image(640,360,'assets/ombragedegat.png', ancrage = "center")
    elif x == 2:
        image(640,360,'assets/detraqueurdegat.png', ancrage = "center")
    elif x == 3:
        image(640,360,'assets/dragomdegat.png', ancrage = "center")
    elif x == 4:
        image(640,360,'assets/basilicdegat.png', ancrage = "center")
    stats()            
    texte(720,380,(degat)) 
    if energie < 0:
        texte(750,570,("0"))
    else:  texte(750,570,(energie))
    texte(520,230,(endurance_monstre))
    mise_a_jour()
    attend_clic_gauche()

def victoire(energie):

    image(640,360,'assets/gagne.png', ancrage = "center")
    stats()
    texte(750,570,(energie))
    mise_a_jour()
    attend_clic_gauche()

def defaite(energie, x):

    if x == 1:
        image(640,360,'assets/perduombrage.png', ancrage = "center")
    elif x == 2:
        image(640,360,'assets/perdudetraqueur.png', ancrage = "center")
    elif x == 3:
        image(640,360,'assets/perdudragom.png', ancrage = "center")
    elif x == 4:
        image(640,360,'assets/perdubasilic.png', ancrage = "center")
    stats()
    texte(750,570,(energie))
    mise_a_jour()
    attend_clic_gauche()
    pygame.mixer.music.stop()
    return False

def salle_coffre(salle, horcrux, gallions, energie, experience):

    image(640,360,'assets/butin.png', ancrage = "center")
    stats()   
    nb1 = randint(0,1)
    texte(400, 575,(nb1)) 
    horcrux += nb1
    nb2 = randint(1,50)*salle
    texte(200, 290,(nb2))
    gallions += nb2
    nb3 = randint(1,50)
    texte(850,260,(nb3))
    energie += nb3
    experience += randint(30,150)*((salle//100)+1)
    mise_a_jour()
    attend_clic_gauche()
    return horcrux, gallions, energie, experience

def coffre_to_menu():

    pygame.mixer.music.stop()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(-1)
    return False, True

def clic_inventaire(event):

    if 1180 <= abscisse(event) <= 1280 and 620 <= ordonnee(event) <= 720:
        return False, True

def affiche_inventaire():

     image(640,360,'assets/bginventaire.png', ancrage = "center")
     image(1230,670,'assets/croix.png', ancrage = "center")
     mise_a_jour()

def level_up(experience, niveau, force, chance):
    
    if experience >= 100:
        experience -= 100
        niveau += 1
        force += randint(1,15)
        chance += randint(1,15)
    return experience, niveau, force, chance

    


##############################################################################
#                           PROGRAMME PRINCIPAL                              #
##############################################################################

pygame.init()
pygame.mixer.init()

cree_fenetre(largeur_plateau,hauteur_plateau)

save = recuperation()
experience  = save[0]
niveau = save[1]
salle = save[2]
horcrux = save[3]
ballais = save[4]
energie = save[5]
gallions = save[6]
force = save[7]
chance = save[8]


# BOUCLE PRINCIPALE DU JEU

while main:

    while accueil:

        affiche_accueil(file) 
        mise_a_jour()

        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, coffre = leave()

        if type == 'ClicGauche':
            accueil, menu, main = clic_accueil(event)

        efface_tout()

    while menu:

        affiche_menu(experience,niveau,force,chance)
        mise_a_jour()

        experience, niveau, force, chance = level_up(experience, niveau, force, chance)
        sauvegarde(experience,niveau,salle,horcrux,ballais,energie,gallions,force,chance)

        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, coffre = leave()

        if type == 'ClicGauche':
            menu, jeu, boutique, entrainement, coffre, ballais, boss = clic_menu(event, ballais, horcrux)

    while entrainement:

        gallions, entrainement, menu = affiche_entrainement(gallions)
        stats()
        mise_a_jour()

        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, coffre = leave()

        if entrainement:
            chance_entraineur()
            experience, energie = recompense_train(energie,experience)
            entrainement, menu = fin_entrainement()

    while boutique:

        affiche_boutique()

        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, coffre = leave()

        if type == 'ClicGauche':
            gallions, energie, ballais, boutique, menu = achat_boutique(gallions,energie,ballais)

    while inventaire:

        affiche_inventaire()

        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, inventaire = leave()

        if type == 'ClicGauche':
            inventaire, menu = clic_inventaire(event)



    while jeu:

        salle, endurance_monstre, combat_random = setup_combat(salle,0)
        while endurance_monstre > 0 and energie > 0:
            energie, endurance_monstre = can_hit(energie, endurance_monstre, combat_random, salle,force,chance)

        if endurance_monstre <= 0:
            victoire(energie)
            salle += 1
            print(salle)
            jeu, coffre = False, True

        elif energie <= 0:
            jeu = defaite(energie, combat_random)
            experience, niveau, salle, horcrux, ballais, energie, gallions,force,chance = 0,0,0,0,0,100,200,0,0
            fin_game()
            jeu, accueil = False,True

    while boss:

        salle, endurance_monstre, combat_random = setup_combat(salle,1)
        while endurance_monstre > 0 and energie > 0:
            energie, endurance_monstre = can_hit(energie, endurance_monstre, combat_random, salle,force,chance)

        if endurance_monstre <= 0:
            victoire(energie)
            fin_game()
            boss ,accueil = False,True

        elif energie <= 0:
            jeu = defaite(energie, combat_random)
            experience, niveau, salle, horcrux, ballais, energie, gallions,force,chance = 0,0,0,0,0,100,200,0,0
            fin_game()
            jeu, accueil = False,True




    while coffre:
        
        event = donne_ev()
        type = type_ev(event)

        if type == 'Quitte':
            main, accueil, menu, entrainement, boutique, jeu, boss, coffre = leave()
            
        horcrux, gallions, energie, experience = salle_coffre(salle,horcrux, gallions, energie, experience)
        coffre, menu = coffre_to_menu()

        efface_tout()


ferme_fenetre()































