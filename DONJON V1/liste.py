# -*- coding: utf-8 -*-
### FAIT DE A a W par Dilien Oeuvrard.
### Seul les dessins ne viennent pas de moi !
from random import randint


message1 = ("""
          
      
          
      
          
          
                              Bonjour jeune Aventurier
                                  et bienvenue dans 
                               Le Donjon Harry Potter !
          
          
                                  
          
                                              
                                                                         Enter
        """)
        
##############################################################################   
##############################################################################   
##############################################################################
# menu   
           
menu1 = ("""
          
      
          
                  Pendant ton aventure tu seras confronté à combattre plusieurs
                  monstres. Gare à toi ! Si tu t'aventure dans ce chateau cela 
                  sera à tes risques et périls.
                  Tu devras réunir les 7 Horcrux afin de battre Voldemort !
                  Pour que le monde des sorciers redeviennent un monde
                  paisible !
                  
                  
                 
          
                                            
         h = aide                                                    p = suite
        """)
        
                
menu2 = ("""
          
              
          
             
      
          
                  Appuyez sur START pour rentrer dans le chateau 
                 
         
          
          
          
                                            
                                                                     s = start
        """)
        
############################################################################## 
##############################################################################   
##############################################################################
# JEU     
            
jeu1 = ("""
          
             
                  Commandes : 
                      
                      - fuir (pour tenter de fuir le combat)
                      - boutique (entre chacune des salles)
                      - stop (pour terminer la partie)
                      - argent (pour voir son argent)
                      - entrainement (pour s'entrainer) coute 100 Gallions
                      - horcrux (voir le nombre d'horcrux')
                      - boss (combattre le boss)
                      
                      - avancer (changer de salle ! // Commencer)
                      
                      
          
                                                                     p = suite
                """)        
############################################################################## 
##############################################################################   
##############################################################################
# FUITE
        
fuite1 = ("""
          
        
          
        
              
                  La fuite est souvent utilisé par les poules !
                          Voulez-vous vraiment fuir ?
                      
                      


                """) 
fuite2 = ("Vous avez fuit ! Votre pays vous renira jusqu'à votre mort ")

############################################################################## 
##############################################################################   
##############################################################################
# COMBAT


monstres = ["Le professeur Ombrage", "Lucius Malefoy", "Bellatrix Lestrange", "Acromantula", "Basilic", "Détraqueur"]

### OMBRAGE

ombragecombat = ("ih ih ih... D'après la règle", randint(20,100), "du règlement de poudlard je dois vous défier !\n")

### Lucius

luciuscombat = ("Donc tu penses pouvoir me battre avec cette baguette magique de seconde main ?\n")

### Bellatrix

bellatrixcombat = ("Je vais te tuer comme j'ai tuer Sirius Black !\n")

### Acromantula

acromantulacombat = ("La géante arraigné vous attaque en vous lançant du fil\n")

### Basilic

basiliccombat = ("Pssstt : Ne le regardez jamais dans les yeux\n")

### detraqueur

detraqueurcombat = ("Huhuhuhuhuhuhuhhhhhhh : Il aspira votre âme !\n")


combat1 = ("""
           
           
           
                   Plus qu'une solution s'offre à vous faire un combat 
                            de dé magique contre le monstre.
           
           
           
           
           
           
          fuir = pour fuir                           demagique = combat de dé
          \n""")
          
          
          
gagner = ("""
          
          
          
          
                          Vous avez gagné votre combat !
                    Vous pourrez trouver un coffre au fond de
                                    la salle
          
          
                                                                        Entrer          
          """)
          
perdu = ("""
         
         
                         Vous avez perdu ! Dommage !
                Une autre fois vous pourrez venir au bout de
                                ce chateau !
         
         
                                                                        Entrer        
         """)
         
         
coffre = ("""
                                         __________
                                        /\____;;___\ 
                                       | /         /
                                       `. ())oo() .
                                       |\(%()*^^()^\ 
                                      %| |-%-------|
                                     % \ | %  ))   |
                                     %  \|%________|
                                     
                                                                        Entrer
        """)
        
##############################################################################
##############################################################################
##############################################################################
# ENTRAINEMENT

entraineurs = ["Hermione Granger", "Harry Potter", "Ron Weasley"]

hg1 = ("""
      
              Bonjour jeune aventurier je suis Hermione Granger.
              Je suis ici pour t'entrainer.
              On va apprendre à faire voler une plume.
              Pour cela tu auras juste à écrire "Wingardium Leviosa"
      
                                                                        Entrer      
      """)
      
chance = randint(4,20)   
   
hg2 = ("""
       
              C'est Levioooooooooosa... et pas LeViOsA
              Entraine-toi encore tu y arriveras un jour.
              
              Vous avez gagné %s de chances
                                                                        Entrer
       """%(chance))
       
hp1 = ("""
               Oui, c'est bien moi, Harry Potter...
               Aujourd'hui je vais t'initier au sortilège du 
               stupéfix ! Tout est dans le geste de la baguette.
               Tu as juste à crier stupéfix !
       
       
                                                                        Entrer       
       """)
force = randint(4,20)     
hp2 = ("""
               Ah ce n'est pas nul mais pas parfait ! Tu y arriveras
               bientôt enfin, je l'espère
               
               Vous avez gagné %d de forces
       
       
                                                                        Entrer      
       """%(force)) 

##############################################################################
##############################################################################
##############################################################################
# BOUTIQUE
         
                                        
boutique = ("""
            
            
            
                    Bienvenue dans la boutique des sorciers !
                    
                    Ici tu peux acheter plusieurs sortes d'item
                    Des potions, de la puissance, une potion de chance
                    ou encore un balais (pour voler au dessus d'une salle)
                                         
                    Soins :
                        [1] Potion 20 HP : 200 Gallions
                        [2] Potion 50 HP : 450 Gallions
                        [3] Potion 100 HP : 850 Gallions
                        
                    Puissance : 
                        [4] Potion de chance : 500 Gallions
                        [5] Potion de force : 500 Gallions
                        
                    Divers  : 
                        [6] Balais magique : 800 Gallions
                    
                    Pour acheter il suffit d'écrire le numéro juste avant
                    l'objet en question.
                    
                        [7] pour quitter
            
            
                                                                        Entrer   
            """)
        
##############################################################################
##############################################################################
##############################################################################
# TRICHE
            
triche = ("""
          
          
                  Voici l'espace caché du jeu de donjon :
                      Il y a plusieurs méthodes de triche:
                          
                [1] ONE SHOT monste : vous gangez tous vos combats.
                [2] 1000000 Gallions : Vous gagnez 1000000 Gallions.
                [3] 10 Ballais : Vous récupérez 10 ballais.
                [4] Hermione Granger : Devient votre seule entraineuse.
                [5] Horcrux : 100 % taux de drop.
                [6] Chance : Donne 1000 de chance
                [7] Force : Donne 1000 de force
                [8] 7 Horcrux : vous donne 7 Horcrux
                [9] 1000 HP : donne 1000 points de vie
                
                [0] Pour quitter
                                                                        Entrer          
          """)
          
##############################################################################
##############################################################################
##############################################################################
# BOSS
         
msgboss = ("""
           
           
           
           
                           Je suis Voldemort, l'invinsible Voldemort
                      Tu penses pouvoir me battre ? Hmmm je ne pense pas 
                    Je vois que tu as réuni les horcrux ! Je suis donc plus
                  faible, mais je reste le plus fort ! Aurais-tu une dernière
                                          volonté ?
                               Hmmm.. Allons-y combattions
           
           
    
                                                                        Entrer           
           """)
           
combatboss1 = ("""
           
           
           
                   Plus qu'une solution s'offre à vous faire un combat 
                            de dé magique contre Voldemort.
           
           
           
           
           
           
          fuir = pour fuir                           demagique = combat de dé
          \n""")
        
perduboss = ("""
             
                 Voldemort à encore gagné ! Vous n'arriverez pas à le 
                     vaincre si vous ne vous entrainez pas plus.
                         Le chef des lieux reste Voldemort !
             
      
             """)
            
gagnerboss = ("""
                                  Vous avez gagné !   
              
                    Les ténèbres s'estompent et le bonheur demeure,
                Voldemort à été vaincu ! Vous avez donc réussi votre
                      mission ! Le monde des sorciers est sauvé !
              
              """)
##############################################################################
##############################################################################
##############################################################################
# HORCRUX
              
lsthorcrux = ["Journal intime de Tom Jedusor", "Bague de Gaunt", "Le médaillon de Salazar Serpentard", "Coupe de Helga Poufsouffle", "Diadème de Rowena Serdaigle", "Nagini", "Harry Potter"] 
horcruxtrouve = []


mort = ("""
        
    
        
                            VOUS ETES MORTS !
        
        
        
                                                                        Entrer    
        """)
        
##############################################################################
##############################################################################
##############################################################################
# FIN JEU
        
finjeu = (""""
          
                  Liste des commandes fin de game :
                      
                      suite : None.
                      stop : stopper le jeu.
          
            
          """)
          
suite = ("""
         
         
         
                     Le monde des sorciers est hors de danger !
                   Attention toute fois, Aux crocs morts qui sont
                  encore plus déchaînés qu'au paravant car le grand
                               maître est mort !
                               
                              
                                
                              
                            
                                
                               7 Ans Plus tard..                         Enter
         """)
         
suite2 = ("""
          
                  Le monde des sorciers est entrain d'être anéanti par
                      le fils de Voldemort ! Nous avons besoin de
                       toi pour y venir à bout ! Bonne chance
                       
                       
                                   
                               Suite......                               Enter
          
            
          """)
          
musique = ("""
           
           
           
           
                           Musique Harry Potter THEME
                             Durée : 44 secondes !
           
            
           
           
           
                                                                        Entrer           
           """)