
from random import randint
from Afficher import Afficher
from Grille import Grille
from JoueurAI import JoueurAI
from OrdiAI import OrdiAI
import time
import tkinter as tk
from tkinter import ttk

defaultProba = 0.9  # probabilité que la tuile nouvellement générée ait une valeur de 2

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(TOUR_JOUEUR, TOUR_ORDI) = (0, 1)


class Jeu:
    def __init__(self):
        self.grille = Grille()
        self.ordiAI = None
        self.joueurAI = None
        self.afficher = None
        self.over = False

    def setOrdiAI(self, ordiAI):
        self.ordiAI = ordiAI

    def setJoueurAI(self, joueurAI):
        self.joueurAI = joueurAI

    def setAfficher(self, afficher):
        self.afficher = afficher

    # Insertion aléatoire de tuiles
    def insertRandonTile(self):
        tuileVal = self.newTuileVal()
        cells = self.grille.getCellVide()
        cell = cells[randint(0, len(cells) - 1)]
        self.grille.setValeur(cell, tuileVal)

    def newTuileVal(self):
        if randint(0, 99) < 100 * defaultProba:
            return 2
        else:
            return 4

    def gameOver(self):
        return not self.grille.movePossible()

    def start(self):
        for i in range(2):  # Initialiser la grille, insérer deux tuiles aléatoires
            self.insertRandonTile()

        # création de la fenêtre de jeu
        win = tk.Tk()
        win.title("2048")
        win.geometry('500x500+50+10')
        container = ttk.Frame(win)
        message = ""

        # afficher la grille initiale
        self.afficher.afficheGrille(self.grille, win, container, message)

        # D'abord le tour du joueur
        tour = TOUR_JOUEUR

        nbmoves = 0  # calculer le nombre de mouvement

        while not self.gameOver() and not self.over:
            # Cloner pour s'assurer que l'IA ne peut pas changer la vraie grille
            grilleClone = self.grille.clone()

            if tour == TOUR_JOUEUR:
                print("Mouvement de joueur:", end="")
                move = self.joueurAI.getMove(grilleClone)
                print(actionDic[move])

                if move != None:
                    if self.grille.movePossible([move]):
                        self.grille.move(move)
                        nbmoves += 1
                    # Mise à jour la valeur max des tuiles
                        maxVal = self.grille.getMaxVal()

                        # Valeur pour ganger
                        if maxVal == 2048:
                            self.over = True
                            message = "Gagné !"
                            self.afficher.afficheGrille(
                                self.grille, win, container, message)
                            print("Gagné!")
                            print(time.perf_counter())
                            print("nb de mouvement :", nbmoves)
                    else:
                        self.over = True
                else:
                    self.over = True
            else:
                print("Nouvelles tuiles créées par ordi:")
                move = self.ordiAI.getMove(grilleClone)
                # Validate Move
                if move and self.grille.inserPossible(move):
                    self.grille.setValeur(move, self.newTuileVal())
                else:
                    self.over = True

            if not self.over:
                message = "temps : " + str(time.perf_counter()) + \
                    "  nb de mouvement : " + str(nbmoves)
                self.afficher.afficheGrille(
                    self.grille, win, container, message)

                print(time.perf_counter())
                print("nb de mouvement :", nbmoves)
            tour = 1 - tour


# def main():

#     jeu = Jeu()
#     joueurAI = JoueurAI()
#     ordiAI = OrdiAI()
#     afficher = Afficher()

#     jeu.setAfficher(afficher)
#     jeu.setJoueurAI(joueurAI)
#     jeu.setOrdiAI(ordiAI)

#     jeu.start()

# if __name__ == '__main__':
#     main()
