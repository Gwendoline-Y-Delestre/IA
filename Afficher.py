# Afficher.py
import tkinter as tk
from ezCLI import *
from ezTK import *
from BaseAffiche import BaseAffiche
import time

colorMap = {
    0: 97,
    2: 41,
    4: 42,
    8: 43,
    16: 44,
    32: 45,
    64: 46,
    128: 100,
    256: 101,
    512: 102,
    1024: 103,
    2048: 104

}
colorMapTK = {
    0: 'lightgrey',
    2: 'red',
    4: 'green',
    8: 'yellow',
    16: 'blue',
    32: 'purple',
    64: 'lightblue',
    128: 'pink',
    256: 'orange',
    512: 'grey',
    1024: 'cyan',
    2048: 'magenta'

}

cTemp = "\x1b[%dm%7s\x1b[0m "


class Afficher(BaseAffiche):
    def __init__(self):
        self.afficheGrille = self.grilleAffiche

    def afficher(self, grille):
        pass

    def grilleAffiche(self, grille):

        win = Win(title='2048', bg='#FFF', op=2, grow=True)
        win.grid = Frame(win, fold=4, bg='#eee')

        for i in range(3 * grille.size):

            for j in range(grille.size):
                v = grille.map[int(i / 3)][j]

                if i % 3 == 1:
                    # creer grille dans terminal
                    string = str(v).center(7, " ")
                    # creer une grille de 4*4 dans une autre fenetre
                    Label(win.grid, height=5, width=9,
                          bg=colorMapTK[v], border=1, text=string)
                else:
                    string = " "  # afficher les espaces entre les lignes
                #my_label.config(text=cTemp % (colorMap[v], string), end="")
                print(cTemp % (colorMap[v], string), end="")

            print("")
            if i % 3 == 2:
                print("")  # afficher les espaces entre les lignes

        win.after(500, lambda: win.exit())
        win.loop()
