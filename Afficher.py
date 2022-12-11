# Afficher.py
import tkinter as tk

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

    def grilleAffiche(self, grille, win, container, message):

        # On creer un canvas pour pouvoir intégrer des frames
        # et ensuite les mettre à jour à chaque appel de la fonction
        canvas = tk.Canvas(container, height=450, width=450)
        canvas.create_window((0, 0), window=container, anchor="nw")

        # label_message permet de connaitre le temps et le nombre de coup
        label_message = tk.Label(container, text=message)
        label_message.pack()

        # ce frame donne la grille de jeu
        lframe = tk.LabelFrame(
            canvas, text="Grille de jeu :", height=400, width=400)

        lframe.pack(fill="both", expand="yes")

        for i in range(3 * grille.size):

            for j in range(grille.size):
                v = grille.map[int(i / 3)][j]

                if i % 3 == 1:
                    # créer grille dans terminal
                    string = str(v).center(7, " ")

                    # créer une grille de 4*4 dans une fenetre graphique
                    label = tk.Label(lframe, height=5, width=9,
                                     bg=colorMapTK[v], border=1, text=string).grid(row=int(i), column=j)
                else:
                    string = " "  # afficher les espaces entre les lignes

                print(cTemp % (colorMap[v], string), end="")

            print("")
            if i % 3 == 2:
                print("")  # afficher les espaces entre les lignes

        # mise à jour de la grille
        container.pack()
        canvas.pack(side="left", fill="both", expand=True)

        lframe.update_idletasks()
        label_message.update_idletasks()
        time.sleep(1)
        label_message.destroy()
        lframe.destroy()
        canvas.update_idletasks()
        canvas.destroy()
        win.update_idletasks()
        win.update()
