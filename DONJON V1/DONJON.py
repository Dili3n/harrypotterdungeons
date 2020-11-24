# -*- coding: utf-8 -*-
### FAIT DE A a W par Dilien Oeuvrard.
### Seul les dessins ne viennent pas de moi !
from liste import *
from fonctions import *
from time import sleep
import keyboard
import winsound

file = "D:/Documents/Ecole/DONJONv3/son/hptheme.wav"

##############################################################################

menu = True
jeu = False
finjeu = False
entre = () #MAIN INPUT
salle = 0
skip = 0 # PERMET DE PASSER UNE SALLE || ACHETABLE EN BOUTIQUE
nbhorcrux = 0
MINB = 50
MAXB = 100
codetriche = False
trichehorcrux = False
    
##############################################################################
     
print(message1)

while menu: 
    
    if keyboard.is_pressed('enter'):
        clear()
        print(menu1)
        
    if keyboard.is_pressed('h'):
        clear()
        print(jeu1)
        
    if keyboard.is_pressed('p'):
        clear()
        print(menu2)
        
    if keyboard.is_pressed('s'):
        menu = False
        jeu = True

clear()
print(jeu1)
while not keyboard.is_pressed('p'):
    sleep
        
##############################################################################   
##############################################################################
##############################################################################
##############################################################################   
##############################################################################   
##############################################################################
##############################################################################
##############################################################################    
    
while jeu: 
    entre = input("Pour continuer veuillez taper une commande :\n")
    while entre != "avancer" and entre != "fuir" and entre != "boutique" and entre != "argent" and entre != "stop" and entre != "entrainement" and entre != "SKIP" and entre != "salle" and entre != "aide" and entre != "codetriche" and entre != "boss" and entre != "horcrux" and entre != "force" and entre != "chance" and entre != "musique":
        entre = input("Pour continuer veuillez taper une commande :\n")

##############################################################################   
########################## Entrainement ######################################
############################################################################## 

    if entre == "entrainement":
        if portefeuille >= 100:
            portefeuille -= 100
            clear()
            if codetriche:
                j = 0
                entrainement(salle, j)
            else:
                j = randint(0, 2)
                entrainement(salle, j)
        else:
            print("Vous n'avez pas assez d'argent, un entrainement coute 100 Gallions")
            continue



    elif entre == "musique":
        clear()
        print(musique)
        winsound.PlaySound(
    file,
    winsound.SND_FILENAME|winsound.SND_NOWAIT,
    )
        continue
##############################################################################   
########################## Boss ##############################################
##############################################################################

    elif entre == "boss":
        clear()
        if nbhorcrux >= 7:
            gagner = combatboss(endurance,boss(randint(200, 500)))
            jeu = False
        else:
            continue
        if gagner:
            finjeu = True
            continue
        else:
            print(mort)
            while not keyboard.is_pressed('enter'):
                sleep
            break
            
            


##############################################################################   
########################## CHANCE ET FORCE ###################################
##############################################################################

    elif entre == "chance":
        print(chance)
        
    elif entre == "force":
        print(force)
    
##############################################################################   
########################## HORCRUX ###########################################
##############################################################################

    elif entre == "horcrux":
        print("Vous avez", nbhorcrux, "Horcrux")
        print(horcruxtrouve)
        print("Il vous en manque", 7 - nbhorcrux, "avant de pouvoir combattre Voldemort")
        
##############################################################################   
########################## AIDE  #############################################
############################################################################## 

    elif entre == "aide":
        clear()
        print(jeu1)
     
##############################################################################   
########################## SALLE 0 ###########################################
############################################################################## 


    elif entre == "salle":
        clear()
        print("Vous êtes en ce moment à la salle numéro", salle)
         
##############################################################################   
########################## Code de Triche ####################################
##############################################################################
        
    elif entre == "codetriche":
        clear()
        print(triche)
        triche1 = True
        while triche1:
            ctriche = input()
            while ctriche != "1" and ctriche != "2" and ctriche != "3" and ctriche != "4" and ctriche != "5" and ctriche != "6" and ctriche != "7" and ctriche != "8" and ctriche != "9" and ctriche != "0":
                ctriche = input()
            if ctriche == "1":
                print("pas encore dev")
            elif ctriche == "2":
                portefeuille += 1000000
                print("Code Triche x1.000.000 Gallions activé")
            elif ctriche == "3":
                skip += 10
                print("Code Triche x10 ballais activé")
            elif ctriche == "4":
                codetriche = True
                print("Code Triche Hermione Granger activé")
            elif ctriche == "5":
                trichehorcrux = True
                print("Code Triche Horcrux activé")
            elif ctriche == "6":
                chance += 1000
                print("Code Triche Chance activé")
            elif ctriche == "7":
                force += 1000
                print("Code Triche Force activé")
            elif ctriche == "8":
                nbhorcrux += 7
                print("Code Triche Horcrux activé")
            elif ctriche == "9":
                endurance = 1000
                print("Code Triche HP activé")
            elif ctriche == "0":
                triche1 = False
                clear()
                continue
                 
##############################################################################   
########################## STOP  #############################################
##############################################################################

    elif entre == "stop":
        clear()
        print("LA PARTIE EST FINIE !\n")
        print(""" 

     _____
    /     \ 
   |   G   | Vous aviez %d Gallions
    \_____/
    """%(portefeuille))
        clear()
        break
        jeu = False
        menu = False
        
##############################################################################   
########################## ARGENT ############################################
##############################################################################        
        
    if entre == "argent":
            clear()
            print(""" 

     _____
    /     \ 
   |   G   | Vous avez %d Gallions
    \_____/
    """%(portefeuille))
     
##############################################################################   
########################## Boutique ##########################################
############################################################################## 
    
    elif entre == "boutique":
        clear()
        print(boutique)
        while not keyboard.is_pressed('enter'):
            sleep
        achat = input()
        while achat != "1" and achat != "2" and achat != "3" and achat != "4" and achat != "5" and achat != "6" and achat != "7":
            achat = input()
        if achat == "1":
            if portefeuille >= 200:
                portefeuille -= 200
                endurance += 20
                print("Vous avez acheté une potion de 20HP. Vous avez maintenant", endurance, "HP")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "2":
            if portefeuille >= 450:
                portefeuille -= 450
                endurance += 50
                print("Vous avez acheté une potion de 50HP. Vous avez maintenant", endurance, "HP")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "3":
            if portefeuille >= 850:
                portefeuille -= 850
                endurance += 100
                print("Vous avez acheté une potion de 100HP. Vous avez maintenant", endurance, "HP")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "4":
            if portefeuille >= 500:
                portefeuille -= 500
                chance += 30
                print("Vous avez acheté une potion de chance. Vous avez maintenant", chance, "de chance")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "2":
            if portefeuille >= 500:
                portefeuille -= 500
                force += 30
                print("Vous avez acheté une potion de force. Vous avez maintenant", force, "de force")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "6":
            if portefeuille >= 800:
                portefeuille -= 800
                skip += 1
                print("Vous avez récupéré un balais. Vous pouvez l'utiliser au début de chacune des parties en écrivant SKIP")
            else:
                print("Vous n'avez pas assez d'argent")
        if achat == "7":
            continue
  
##############################################################################   
########################## FUIR  #############################################
##############################################################################        
 
    elif entre == "fuir":
        fuite = input("Fuir ? [O/N]\n")
        while fuite == "O" and fuite == "N":
            fuite = input("Fuir ? [O/N]")
        
        if fuite == "O":
            print(fuite2)
        elif fuite == "N":
            entre = input("Pour rentrer dans la première salle écrire avancer\n")
            while entre != avancer:
                entre = input("Pour rentrer dans la première salle écrire avancer\n")
                
##############################################################################   
########################## SKIP ##############################################
##############################################################################
                
    elif entre == "SKIP":
        clear()
        if skip >= 1:
            skip -= 1
            salle += 1
            print("Vous avez ouvert la porte de la salle numéro", salle,"\n")
            sleep(2)
            money = (fouillez_salle(salle))
            endur = (potion(salle))
            horcruxrandom = randint(1,2)
            if horcruxrandom == 1 or trichehorcrux:
                n = 6
                i = randint(0,n)
                ajouter(horcruxtrouve, lsthorcrux[i])
                Suppr(lsthorcrux, i)
                n -= 1
                nbhorcrux += 1
                print("""
             
                                  VOUS AVEZ TROUVÉ LE HORCRUX :
                                              %s
              
              
                  """%(lsthorcrux[i]))
            portefeuille += money
            endurance += endur
            print("\nVous avez désormais", endurance, "HP")
            print("Vous avez un total de", portefeuille, "Gallions\n")
    
##############################################################################   
########################## AVANCER ###########################################
##############################################################################

    elif entre == "avancer":
        clear()
        if nbhorcrux == 7:
            print("Vous avez déjà les 7 horcrux ! faites boss pour combattre Voldemort")
            continue
        salle += 1
        visitez_salle(salle)
        r = randint(1,4)
        if r != 1:
            nbv = 5
            i = randint(0,nbv)
            Suppr(monstres, i)
            nbv -= 1
            combattre(endurance,ennemi(randint(MIN, MAX)*salle, i))
            if endurance <= 0:
                break
            print("\n")
            money = 0
            endur = 0
            money = (fouillez_salle(salle))
            endur = (potion(salle))
            horcruxrandom = randint(1,2)
            if horcruxrandom == 1 or trichehorcrux:
                n = 6
                i = randint(0,n)
                ajouter(horcruxtrouve, lsthorcrux[i])
                Suppr(lsthorcrux, i)
                n -= 1
                nbhorcrux += 1
                print("""
             
                                  VOUS AVEZ TROUVÉ LE HORCRUX :
                                              %s
              
              
                  """%(lsthorcrux[i]))
            portefeuille += money
            endurance += endur
            print("\nVous avez désormais", endurance, "HP")
            print("Vous avez un total de", portefeuille, "Gallions\n")
            
        else:
            print("La voix est libre !\nAucun monstre n'est présent dans la salle")
            sleep(2)
            money = 0
            endur = 0
            money = (fouillez_salle(salle))
            horcruxrandom = randint(1,2)
            if horcruxrandom == 1 or trichehorcrux:
                n = 6
                i = randint(0,n)
                ajouter(horcruxtrouve, lsthorcrux[i])
                Suppr(lsthorcrux, i)
                n -= 1
                nbhorcrux += 1
                print("""
             
                                  VOUS AVEZ TROUVÉ LE HORCRUX :
                                              %s
              
              
                  """%(lsthorcrux[i]))
            portefeuille += money
            endurance += endur
            if salle != 10:
                print("\nVous avez désormais", endurance, "HP")
                print("Vous avez un total de", portefeuille, "Gallions\n")
            else:
                print("\nBien joué ! Vous avez fini le chateau ! avec un total de", portefeuille)
    

##############################################################################   
##############################################################################
##############################################################################
##############################################################################   
##############################################################################   
##############################################################################
##############################################################################
##############################################################################    
    
while finjeu:
    clear()
    print(finjeu)
    entrefin = input("Pour continuer veuillez taper une commande :\n")
    while  entrefin != "suite" and entrefin != "stop":
        entrefin = input("Pour continuer veuillez taper une commande :\n")
        
##############################################################################   
################################## STOP ######################################
##############################################################################        
        
    if entrefin == "stop":
        clear()
        print("LA PARTIE EST FINIE VOUS AVEZ GAGNE!\n")
        print(""" 

     _____
    /     \ 
   |   G   | Vous aviez %d Gallions
    \_____/
    """%(portefeuille))
        clear()
        finjeu = False
        break
    
    elif entrefin == "suite":
        clear()
        print(suite)
        while not keyboard.is_pressed('enter'):
                sleep
        clear()
        print(suite2)
        while not keyboard.is_pressed('enter'):
                sleep
        finjeu = False
        break
        
        
        
        