# Jeu.py
from random import randint

from Afficher import Afficher
from Grille import Grille
from JoueurAI import JoueurAI
from OrdiAI import OrdiAI

defaultProba = 0.8 # probabilité que la tuile nouvellement générée ait une valeur de 2

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(TOUR_JOUEUR, TOUR_ORDI) = (0, 1)

# Time Limit
timeLimit = 0.3
allowance = 0.05



class Jeu:
    def __init__(self, size=4):
        self.grille = Grille(size)
        self.ordiAI = None
        self.joueurAI = None
        self.afficher = None
        self.over = False


    def setOrdiAI(self, ordiAI):
        self.ordiAI = ordiAI

    def setJoueurAI(self, JoueurAI):
        self.JoueurAI = JoueurAI

    def setAfficher(self, afficher ):
        self.afficher  = afficher


    # def updateAlarm(self, currTime):
    #     if currTime - self.prevTime > timeLimit + allowance:
    #         self.over = True
    #     else:
    #         while time.perf_counter() - self.prevTime < timeLimit + allowance:
    #             pass
    #         self.prevTime = time.perf_counter()


    # Insertion aléatoire de tuiles
    def insertRandonTile(self) -> object :
        tileValue = self.newTuileVal()
        cells = self.grille.getCellVide()
        cell = cells[randint(0, len(cells) - 1)]
        self.grille.setValeur(cell, tileValue)


    def newTuileVal(self):
        if randint(0, 99) < 100 * defaultProba :
            return 2
        else:
            return 4

    def gameOver(self):
        return not self.grille.movePossible()


    def start(self):
        for i in range(2): # Initialiser la grille, insérer deux tuiles aléatoires
            self.insertRandonTile()

        self.afficher.afficheGrille(self.grille) # afficher la grille initial

        # D'abord le tour du joueur
        tour = TOUR_JOUEUR
        maxVal = 0

        ## self.prevTime = time.perf_counter()

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

                        # Valeur pour ganger
                        if maxVal == 256:
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

            # Exceeding the Time Allotted for Any Turn Terminates the Game
           ## self.updateAlarm(time.perf_counter())

            tour = 1 - tour

            #score = self.playerAI.evaluation(grilleCopy)
            #print(score)

        print("Gagner!")



def main():
    jeu = Jeu()
    joueurAI = JoueurAI()
    ordiAI = OrdiAI()
    afficher = Afficher()
    jeu.setAfficher (afficher)
    jeu.setJoueurAI(joueurAI)
    jeu.setOrdiAI(ordiAI)

    jeu.start()

if __name__ == '__main__':
    main()

