
from random import randint
from ezCLI import *
from ezTK import *
from Afficher import Afficher
from Grille import Grille
from JoueurAI import JoueurAI
from OrdiAI import OrdiAI

defaultProba = 0.8  # probabilité que la tuile nouvellement générée ait une valeur de 2

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(TOUR_JOUEUR, TOUR_ORDI) = (0, 1)


class Jeu:
    def __init__(self, size=4):
        self.grille = Grille(size)
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
    def insertRandonTile(self) -> object:
        tileValue = self.newTuileVal()
        cells = self.grille.getCellVide()
        cell = cells[randint(0, len(cells) - 1)]
        self.grille.setValeur(cell, tileValue)

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

        # afficher la grille initial
        self.afficher.afficheGrille(self.grille)

        # D'abord le tour du joueur
        tour = TOUR_JOUEUR
        maxVal = 0

        while not self.gameOver() and not self.over:
            # Cloner pour s'assurer que l'IA ne peut pas changer la vraie grille
            grilleClone = self.grille.clone()

            move = None

            if tour == TOUR_JOUEUR:
                print("Mouvement de joueur:", end="")
                move = self.JoueurAI.getMove(grilleClone)
                print(actionDic[move])

                if move != None and move >= 0 and move < 4:
                    if self.grille.movePossible([move]):
                        self.grille.move(move)
                    # Mise à jour la valeur max des tuiles
                        maxVal = self.grille.getMaxVal()

                        # Valeur pour gagner
                        if maxVal == 32:  # changer pour 2048
                            self.over = True
                            self.afficher.afficheGrille(self.grille)

                    else:
                        print("Mouvement interdit")
                        self.over = True
                else:
                    print("Mouvement interdit")
                    self.over = True
            else:
                print("Nouvelles tuiles créées par ordi:")
                move = self.ordiAI.getMove(grilleClone)
                # Validate Move
                if move and self.grille.inserPossible(move):
                    self.grille.setValeur(move, self.newTuileVal())
                else:
                    print("Invalid Ordinateur AI Move")
                    self.over = True

            if not self.over:
                self.afficher.afficheGrille(self.grille)


            tour = 1 - tour

        print("Gagner!")


def main():

    # global win_start
    jeu = Jeu()
    joueurAI = JoueurAI()
    ordiAI = OrdiAI()
    afficher = Afficher()

    # win_start = Win(title='2048', op=3)
    # frame = Frame(win_start)
    # Label(frame, text='Lancement du jeu', bg='#000', fg='#FFF',
    #       font='Arial 18 bold', height=2)

    jeu.setAfficher(afficher)
    jeu.setJoueurAI(joueurAI)
    jeu.setOrdiAI(ordiAI)

    # Button(win_start, text='START', command=jeu.start(), font='Arial 18 bold',
    #        bg='#000', fg='#FFF')

    jeu.start()

    # win_start.loop()


if __name__ == '__main__':
    main()
