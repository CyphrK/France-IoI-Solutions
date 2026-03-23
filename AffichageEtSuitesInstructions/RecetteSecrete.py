#Écrire un programme qui effectue une série de transvasements permettant d'obtenir exactement 4 litres d'eau dans le plus grand tonneau, sachant que l'on dispose d'un tonneau de 5l et un de 3l

from robot import *

remplir(5)             #on a 5 litres dans le grand tonneau (GT)
transferer(5,3)        #2 litres dans GT et 3 litres dans le petit tonneau (PT)
vider(3)               #2 litres dans GT et 0 litres dans PT
transferer(5,3)        #0 litres dans GT et 2 litres dans PT
remplir(5)             #5 litres dans GT et 2 litres dans PT
transferer(5,3)        #4 litres dans GT et 3 litres dans PT
