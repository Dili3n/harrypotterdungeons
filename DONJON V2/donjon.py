# -*- coding: utf-8 -*-

#WSH LA ZONE C'Est BIEN MOI

import pygame
import os
from random import randint
from textes import *
from dec import *
from time import sleep
import keyboard
import winsound

pygame.init()
pygame.font.init()
pygame.mixer.init()

gallions = 1000
endurance = 100
nbhorcrux = 0
nbballais = 0
i = 1
salle = 0

accueil = True
menu = False
game = False
boutique = False
jeu = False
entrainement = False
coffre = False

jeut = True

while jeut:
    
    print(aide)

    while accueil:
    
    
        screen.blit(background, (0, 0))

        screen.blit(play_button, play_button_rect)
        screen.blit(leave_button, leave_button_rect)
        screen.blit(mute_button, mute_button_rect)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                accueil = False
                pygame.quit()
                print("Fermeture de la fênetre de jeu")


        if event.type == pygame.MOUSEBUTTONDOWN:
            if leave_button_rect.collidepoint(event.pos):
               accueil = False
               pygame.quit()
                
            elif play_button_rect.collidepoint(event.pos):
               accueil = False
               menu = True
               continue
    
            elif mute_button_rect.collidepoint(event.pos):
                pygame.mixer.music.pause()
            
            
        pygame.display.flip()

    while menu:  
    
        pygame.mixer.music.play(-1)
        pygame.mixer.music.set_volume(50)

    
        screen.blit(parchemin, (0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                menu = False
                pygame.quit()
                print("Fermeture de la fênetre de jeu")
        
        if event.type == pygame.MOUSEBUTTONDOWN:
           None
            
        screen.blit(texte1, (150, 570))
        screen.blit(enter, (1095 ,675))
        pygame.display.update()
        while not keyboard.is_pressed('enter'):
           sleep
        pygame.time.wait(300)
        pygame.display.update()
        screen.blit(parchemin, (0, 0))
        screen.blit(texte2, (150, 570))
        screen.blit(texte2_1, (150, 585))
        screen.blit(texte2_2, (150, 600))
        screen.blit(texte2_3, (150, 615))
        screen.blit(enter, (1095 ,675))
        pygame.display.update()
        while not keyboard.is_pressed('enter'):
           sleep
        pygame.time.wait(300)
        pygame.display.update()
        screen.blit(parchemin, (0, 0))
        screen.blit(texte3, (150, 570))
        screen.blit(enter, (1095 ,675))
        pygame.display.update()
        while not keyboard.is_pressed('enter'):
            sleep
        pygame.time.wait(300)
        menu = False
        game = True
        continue

        pygame.display.update()

    font1 = pygame.font.Font(None, 24)

    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
    horcruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))

    while game:
    
        screen.blit(bgdebut, (0, 0))
        screen.blit(portefeuilletexte, (73, 68))
        screen.blit(endurancetexte, (1198, 68))
        screen.blit(horcruxtexte, (638, 68))
    
        screen.blit(boutique_button, boutique_button_rect)
        screen.blit(play2_button, play2_button_rect)
        screen.blit(entrainement_button, entrainement_rect)
        screen.blit(ballais_button, ballais_button_rect)
    
        pygame.display.update()
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game = False
               pygame.quit()
               print("Fermeture de la fênetre de jeu")
            
        if event.type == pygame.MOUSEBUTTONUP:
            if boutique_button_rect.collidepoint(event.pos):
                boutique = True
                game = False
                continue
            elif play2_button_rect.collidepoint(event.pos):
               game = False
               jeu = True
               continue
            elif entrainement_rect.collidepoint(event.pos):
                s = randint(1,2)
                game = False
                entrainement = True
                continue
            elif ballais_button_rect.collidepoint(event.pos):
                if nbballais >= 1:
                    nbballais -= 1
                    salle += 1
                    game = False
                    coffre = True
                    screen.blit(ballaisuse, (0,0))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(300)
                    continue
            
        pygame.display.update()
    
    while boutique:
    
        endurancetexte = font1.render((str(endurance)),1,(0,0,0))
        portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
        hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
    
        screen.blit(bgdebut, (0, 0))
        screen.blit(portefeuilletexte, (73, 68))
        screen.blit(endurancetexte, (1198, 68))
        screen.blit(horcruxtexte, (638, 68))
    
        screen.blit(boutique1_button, boutique1_button_rect)
        screen.blit(boutique2_button, boutique2_button_rect)
        screen.blit(leaveb_button, leaveb_button_rect)
    
        pygame.display.update()
    
        for event in pygame.event.get():
           if event.type == pygame.QUIT:
               game = False
               pygame.quit()
               print("Fermeture de la fênetre de jeu")
    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if boutique1_button_rect.collidepoint(event.pos):
                if gallions >= 200:
                    gallions -= 200
                    screen.blit(portefeuilletexte, (73, 68))
                    endurance = endurance + 20
                    screen.blit(boutique_accept_button, (150, 240))
                    pygame.display.update()
                    pygame.time.wait(700)
                else: 
                    screen.blit(boutique_refus_button, (150, 240))
                    pygame.display.update()
                    pygame.time.wait(700)
            elif boutique2_button_rect.collidepoint(event.pos):
                if gallions >= 800:
                    gallions -= 800
                    screen.blit(portefeuilletexte, (73, 68))
                    nbballais += 1
                    screen.blit(boutique_accept_button, (630, 240))
                    pygame.display.update()
                    pygame.time.wait(700)
                else: 
                    screen.blit(boutique_refus_button, (630, 240))
                    pygame.display.update()
                    pygame.time.wait(700)
            elif leaveb_button_rect.collidepoint(event.pos):
                boutique = False
                game = True
                continue
            
        pygame.display.update()
        
    while entrainement:
        gallions -= 100
        screen.blit(bgtextdebut, (0, 0))
        screen.blit(portefeuilletexte, (73, 68))
        screen.blit(endurancetexte, (1198, 68))
        screen.blit(horcruxtexte, (638, 68))

        if s == 1:
            screen.blit(hermione, (81, 320))
            screen.blit(hg1, (447, 594))
            screen.blit(hg1_2, (447, 619))
            screen.blit(enter, (1095 ,675))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
               sleep
            pygame.time.wait(300)
            pygame.display.update()
            screen.blit(bgtextdebut, (0, 0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            screen.blit(hermione, (81, 320))
            screen.blit(hg2, (447, 619))
            endurance += 15
            screen.blit(enter, (1095 ,675))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
               sleep
            pygame.time.wait(300)
            entrainement = False
            game = True
            pygame.display.update()
            continue
            
        elif s == 2:
            screen.blit(harry, (81, 320))
            screen.blit(hp1, (371, 589))
            screen.blit(hp1_2, (371, 614))
            screen.blit(enter, (1095 ,675))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
               sleep
            pygame.time.wait(300)
            pygame.display.update()
            screen.blit(bgtextdebut, (0, 0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            screen.blit(harry, (81, 320))
            screen.blit(hp2, (371, 589))
            endurance += 5
            screen.blit(enter, (1095 ,675))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
               sleep
            pygame.time.wait(300)
            entrainement = False
            game = True
            pygame.display.update()
            continue
                
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               game = False
               pygame.quit()
               print("Fermeture de la fênetre de jeu")
               
        if event.type == pygame.MOUSEBUTTONUP:
            print(pygame.mouse.get_pos())
               
        pygame.display.update()

    while jeu:
        
        salle += 1
        endurance_monstre = (randint(30, 50))*salle
        combatrandom = randint(1,4)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
                pygame.quit()
                print("Fermeture de la fênetre de jeu")
        
        if combatrandom == 1:
            screen.blit(ombragecombat, (0, 0))
            pygame.display.update()
            endurancetexte = font1.render((str(endurance)),1,(0,0,0))
            portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
            hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
            endurance_ = font1.render((str(endurance)),1,(0,0,0))
            screen.blit(endurancemonstre, (500, 240))
            screen.blit(endurance_, (750, 580))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
                sleep
            pygame.time.wait(300)
            while endurance_monstre >= 0 and endurance >= 0:
                chancetape = randint(1,2)
                if chancetape == 1:         
                    degat2 = randint(5,20)
                    endurance -= degat2
                    screen.blit(ombragedegat, (0, 0))
                    pygame.display.update()
                    degatombrage = font1.render((str(degat2)),1,(0,0,0))
                    screen.blit(degatombrage, (700, 390))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (500, 240))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
                elif chancetape == 2:
                    screen.blit(ombragedegat2, (0, 0))
                    pygame.display.update()
                    degat1 = randint(5,20)
                    endurance_monstre -= degat1
                    degatheros = font1.render((str(degat1)),1,(0,0,0))
                    screen.blit(degatheros, (700, 390))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (500, 240))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
            if endurance_monstre <= 0:
                screen.blit(gagne, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68)) 
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                coffre = True
                continue
            elif endurance <= 0:
                screen.blit(perduombrage, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                break
            pygame.display.update()   
               
        elif combatrandom == 2:
            screen.blit(detraqueurcombat, (0, 0))
            pygame.display.update()
            endurancetexte = font1.render((str(endurance)),1,(0,0,0))
            portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
            hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            pygame.display.update()
            endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
            endurance_ = font1.render((str(endurance)),1,(0,0,0))
            screen.blit(endurancemonstre, (520, 240))
            screen.blit(endurance_, (750, 580))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
                        sleep
            pygame.time.wait(300)
            pygame.display.update()
            while endurance_monstre >= 0 and endurance >= 0:
                chancetape = randint(1,2)
                if chancetape == 1:         
                    degat2 = randint(5,20)
                    endurance -= degat2
                    screen.blit(detraqueurdegat, (0, 0))
                    pygame.display.update()
                    degatdetraqueur = font1.render((str(degat2)),1,(0,0,0))
                    screen.blit(degatdetraqueur, (720, 390))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (520, 240))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
                elif chancetape == 2:
                    screen.blit(detraqueurdegat2, (0, 0))
                    pygame.display.update()
                    degat1 = randint(5,20)
                    endurance_monstre -= degat1
                    degatheros = font1.render((str(degat1)),1,(0,0,0))
                    screen.blit(degatheros, (700, 390))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (520, 240))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
            if endurance_monstre <= 0:
                screen.blit(gagne, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                pygame.display.update()
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                coffre = True
                continue
            elif endurance <= 0:
                screen.blit(perdudetraqueur, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                pygame.display.update()
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                pygame.mixer.music.volume(0)
                jeu = False
                pygame.quit
                continue
            pygame.display.update()
            
        elif combatrandom == 3:
            screen.blit(dragomcombat, (0, 0))
            pygame.display.update()
            endurancetexte = font1.render((str(endurance)),1,(0,0,0))
            portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
            hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            pygame.display.update()
            endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
            endurance_ = font1.render((str(endurance)),1,(0,0,0))
            screen.blit(endurancemonstre, (520, 240))
            pygame.display.update()
            screen.blit(endurance_, (750, 580))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
                        sleep
            pygame.time.wait(300)
            pygame.display.update()
            while endurance_monstre >= 0 and endurance >= 0:
                chancetape = randint(1,2)
                if chancetape == 1:         
                    degat2 = randint(5,20)
                    endurance -= degat2
                    screen.blit(dragomdegat, (0, 0))
                    pygame.display.update()
                    degatdragom = font1.render((str(degat2)),1,(0,0,0))
                    screen.blit(degatdragom, (720, 390))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (520, 240))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
                elif chancetape == 2:
                    screen.blit(dragomdegat2, (0, 0))
                    pygame.display.update()
                    degat1 = randint(5,20)
                    endurance_monstre -= degat1
                    degatheros = font1.render((str(degat1)),1,(0,0,0))
                    screen.blit(degatheros, (700, 390))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (520, 240))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
            if endurance_monstre <= 0:
                screen.blit(gagne, (0, 0))
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                pygame.display.update()
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                coffre = True
                continue
            elif endurance <= 0:
                screen.blit(perdudragom, (0, 0))
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                pygame.display.update()
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                pygame.mixer.music.volume(0)
                jeu = False
                pygame.quit
                continue
            pygame.display.update()
            
        if combatrandom == 4:
            screen.blit(basiliccombat, (0, 0))
            endurancetexte = font1.render((str(endurance)),1,(0,0,0))
            portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
            hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
            screen.blit(portefeuilletexte, (73, 68))
            screen.blit(endurancetexte, (1198, 68))
            screen.blit(horcruxtexte, (638, 68))
            endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
            endurance_ = font1.render((str(endurance)),1,(0,0,0))
            screen.blit(endurancemonstre, (500, 240))
            screen.blit(endurance_, (750, 580))
            pygame.display.update()
            while not keyboard.is_pressed('enter'):
                sleep
            pygame.time.wait(300)
            pygame.display.update()
            while endurance_monstre >= 0 and endurance >= 0:
                chancetape = randint(1,2)
                if chancetape == 1:         
                    degat2 = randint(5,20)
                    endurance -= degat2
                    screen.blit(basilicdegat, (0, 0))
                    pygame.display.update()
                    degatbasilic = font1.render((str(degat2)),1,(0,0,0))
                    screen.blit(degatbasilic, (700, 390))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (500, 240))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
                elif chancetape == 2:
                    screen.blit(basilicdegat2, (0, 0))
                    pygame.display.update()
                    degat1 = randint(5,20)
                    endurance_monstre -= degat1
                    degatheros = font1.render((str(degat1)),1,(0,0,0))
                    screen.blit(degatheros, (700, 390))
                    pygame.display.update()
                    endurance_ = font1.render((str(endurance)),1,(0,0,0))
                    screen.blit(endurance_, (750, 580))
                    pygame.display.update()
                    endurancemonstre = font1.render((str(endurance_monstre)),1,(0,0,0))
                    screen.blit(endurancemonstre, (500, 240))
                    pygame.display.update()
                    endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                    portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                    hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                    screen.blit(portefeuilletexte, (73, 68))
                    screen.blit(endurancetexte, (1198, 68))
                    screen.blit(horcruxtexte, (638, 68))
                    pygame.display.update()
                    while not keyboard.is_pressed('enter'):
                        sleep
                    pygame.time.wait(400)
                    pygame.display.update()
            if endurance_monstre <= 0:
                screen.blit(gagne, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68)) 
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                coffre = True
                continue
            elif endurance <= 0:
                screen.blit(perdubasilic, (0, 0))
                pygame.display.update()
                endurancetexte = font1.render((str(endurance)),1,(0,0,0))
                portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
                hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
                screen.blit(portefeuilletexte, (73, 68))
                screen.blit(endurancetexte, (1198, 68))
                screen.blit(horcruxtexte, (638, 68))     
                pygame.display.update()
                endurance_ = font1.render((str(endurance)),1,(0,0,0))
                screen.blit(endurance_, (750, 580))
                pygame.display.update()
                while not keyboard.is_pressed('enter'):
                        sleep
                pygame.time.wait(400)
                pygame.display.update()
                jeu = False
                break
            pygame.display.update()
        pygame.display.update()
        
    while coffre:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jeu = False
                pygame.quit()
                print("Fermeture de la fênetre de jeu")
        
        screen.blit(butin, (0, 0))
        pygame.display.update()
        endurancetexte = font1.render((str(endurance)),1,(0,0,0))
        portefeuilletexte = font1.render((str(gallions)),1,(0,0,0))
        hocruxtexte = font1.render((str(nbhorcrux)),1,(0,0,0))
        screen.blit(portefeuilletexte, (73, 68))
        screen.blit(endurancetexte, (1198, 68))
        screen.blit(horcruxtexte, (638, 68))
        horcruxchance = randint(0,1)
        horcruxsv = font2.render((str(horcruxchance)),1,(0,0,0))
        nbhorcrux += horcruxchance
        screen.blit(horcruxsv, (400, 575))
        gallionsplus = randint(1,50)*salle
        gallions += gallionsplus
        gallionsplusv = font2.render((str(gallionsplus)),1,(0,0,0))
        screen.blit(gallionsplusv, (200, 300))
        enduranceplus = randint(1,50)
        endurance += enduranceplus
        enduranceplusv = font2.render((str(enduranceplus)),1,(0,0,0))
        screen.blit(enduranceplusv, (850, 270))
        pygame.display.update()
        coffre = False
        while not keyboard.is_pressed('enter'):
            sleep
        pygame.time.wait(400)
        pygame.display.update()
        game = True
        