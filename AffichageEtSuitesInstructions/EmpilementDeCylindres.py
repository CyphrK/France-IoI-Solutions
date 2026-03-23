#Le but est de déplacer tous les disques de la zone 1 à la zone 3 en respectant deux règles :
#on ne peut déplacer qu'un disque à la fois ;
#on ne peut jamais poser un disque sur un disque plus petit que lui;
#Encore une fois on appel un robot donc il faut l'appeler.

from robot import *

deplacer(1,2) #on dépalce le cylindre tout en haut de la zone 1 à la zone 2 
deplacer(1,3)
deplacer(2,3)
deplacer(1,2)
deplacer(3,1)
deplacer(3,2)
deplacer(1,2)
deplacer(1,3)
deplacer(2,3)
deplacer(2,1)
deplacer(3,1)
deplacer(2,3)
deplacer(1,2)
deplacer(1,3)
deplacer(2,3)
