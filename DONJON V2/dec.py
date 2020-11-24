# -*- coding: utf-8 -*-
"""
Created on Tue Nov 24 08:55:22 2020

@author: xarfy
"""

import pygame
import os
from random import randint
from textes import *
from time import sleep
import keyboard

pygame.init()
pygame.font.init()
pygame.mixer.init()

pygame.mixer.music.load('assets/song.mp3')

screen = pygame.display.set_mode((1280,720))

font = pygame.font.SysFont('helvetic', 70)

pygame.display.set_caption("Donjon : Harry Potter")

background = pygame.image.load('assets/bg.png')

play_button = pygame.image.load('assets/button1.png')
play_button = pygame.transform.scale(play_button, (200, 400))
play_button_rect = play_button.get_rect()
play_button_rect.x = 170
play_button_rect.y = 175
play_button_rect1 = play_button.get_rect()
play_button_rect1.x = 640
play_button_rect1.y = 360

leave_button = pygame.image.load('assets/button2.png')
leave_button = pygame.transform.scale(leave_button, (200, 400))
leave_button_rect = leave_button.get_rect()
leave_button_rect.x = 870
leave_button_rect.y = 175

mute_button = pygame.image.load('assets/mute.png')
mute_button = pygame.transform.scale(mute_button, (50, 50))
mute_button_rect = mute_button.get_rect()
mute_button_rect.x = 1220
mute_button_rect.y = 660

boutique_button = pygame.image.load('assets/button3.png')
boutique_button = pygame.transform.scale(boutique_button, (200, 400))
boutique_button_rect = boutique_button.get_rect()
boutique_button_rect.x = 150
boutique_button_rect.y = 240

play2_button = pygame.image.load('assets/button1.png')
play2_button = pygame.transform.scale(play2_button, (200, 400))
play2_button_rect = play2_button.get_rect()
play2_button_rect.x = 550
play2_button_rect.y = 240

entrainement_button = pygame.image.load('assets/button4.png')
entrainement_button = pygame.transform.scale(entrainement_button, (200, 400))
entrainement_rect = entrainement_button.get_rect()
entrainement_rect.x = 950
entrainement_rect.y = 240

boutique1_button = pygame.image.load('assets/boutique1.png')
boutique1_button = pygame.transform.scale(boutique1_button, (500, 300))
boutique1_button_rect = boutique1_button.get_rect()
boutique1_button_rect.x = 150
boutique1_button_rect.y = 240

boutique2_button = pygame.image.load('assets/boutique2.png')
boutique2_button = pygame.transform.scale(boutique2_button, (500, 300))
boutique2_button_rect = boutique2_button.get_rect()
boutique2_button_rect.x = 630
boutique2_button_rect.y = 240

boutique_accept_button = pygame.image.load('assets/button4.png')
boutique_accept_button = pygame.transform.scale(entrainement_button, (500, 300))
boutique_accept_button_rect = boutique2_button.get_rect()
boutique_accept_button_rect.x = 630
boutique_accept_button_rect.y = 240

boutique_accept_button = pygame.image.load('assets/achataccept.png')
boutique_accept_button = pygame.transform.scale(boutique_accept_button, (500, 300))

boutique_refus_button = pygame.image.load('assets/achatrefus.png')
boutique_refus_button = pygame.transform.scale(boutique_refus_button, (500, 300))

hermione = pygame.image.load('assets/hermione.png')
hermione = pygame.transform.scale(hermione, (360, 450))

harry = pygame.image.load('assets/harry.png')
harry = pygame.transform.scale(harry, (360, 450))

leaveb_button = pygame.image.load('assets/croix.png')
leaveb_button = pygame.transform.scale(leaveb_button, (50, 50))
leaveb_button_rect = leaveb_button.get_rect()
leaveb_button_rect.x = 1220
leaveb_button_rect.y = 660

ballais_button = pygame.image.load('assets/ballais.png')
ballais_button = pygame.transform.scale(ballais_button, (42, 64))
ballais_button_rect = ballais_button.get_rect()
ballais_button_rect.x = 0
ballais_button_rect.y = 650


parchemin = pygame.image.load('assets/bgtexte.png')
parchemin_rect = parchemin.get_rect()

bgtextdebut = pygame.image.load('assets/bgtextdebut.png')

bgdebut = pygame.image.load('assets/bgdebut.png')

ombragecombat =  pygame.image.load('assets/ombragecombat.png')

ombragedegat =  pygame.image.load('assets/ombragedegat.png')

ombragedegat2 = pygame.image.load('assets/ombragedegat2.png')

detraqueurcombat =  pygame.image.load('assets/detraqueurcombat.png')

detraqueurdegat =  pygame.image.load('assets/detraqueurdegat.png')

detraqueurdegat2 = pygame.image.load('assets/detraqueurdegat2.png')

dragomcombat =  pygame.image.load('assets/dragomcombat.png')

dragomdegat =  pygame.image.load('assets/dragomdegat.png')

dragomdegat2 = pygame.image.load('assets/dragomdegat2.png')

basiliccombat =  pygame.image.load('assets/basiliccombat.png')

basilicdegat =  pygame.image.load('assets/basilicdegat.png')

basilicdegat2 = pygame.image.load('assets/basilicdegat2.png')

perdubasilic = pygame.image.load('assets/perdubasilic.png')

gagne = pygame.image.load('assets/gagne.png')

perdudragom = pygame.image.load('assets/perdudragom.png')

perduombrage = pygame.image.load('assets/perduombrage.png')

perdudetraqueur = pygame.image.load('assets/perdudetraqueur.png')

butin = pygame.image.load('assets/butin.png')

ballaisuse = pygame.image.load('assets/ballaisuse.png')

font = pygame.font.Font(None, 24)
enter = font.render(enter,1,(0,0,0))
texte1 = font.render(presentation1,1,(0,0,0))
texte2 = font.render(presentation2,1,(0,0,0))
texte2_1 = font.render(presentation2_1,1,(0,0,0))
texte2_2 = font.render(presentation2_2,1,(0,0,0))
texte2_3 = font.render(presentation2_3,1,(0,0,0))
texte3 = font.render(presentation3,1,(0,0,0))

font2 = pygame.font.Font(None, 50)

hg1 = font.render(hg1,1,(0,0,0))
hg1_2 = font.render(hg1_2,1,(0,0,0))
hg2 = font.render(hg2,1,(0,0,0))
hp1 = font.render(hp1,1,(0,0,0))
hp1_2 = font.render(hp1_2,1,(0,0,0))
hp2 = font.render(hp2,1,(0,0,0))