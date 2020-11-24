# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 18:36:21 2020

@author: xarfy
"""

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