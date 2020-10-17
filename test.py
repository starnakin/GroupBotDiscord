from robot import *

for i in range(9):
    droite()
haut()
for i in range(8):
    gauche()
haut()
for k in range(4):
    for i in range(8):
        droite()
    haut()
    for i in range(8):
        gauche()
    haut()