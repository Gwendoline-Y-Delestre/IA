
from random import randint
import time
from Afficher import Afficher
from Grille import Grille
from OrdiAI import OrdiAI

defaultProba = 0.9 # probabilité que la tuile nouvellement générée ait une valeur de 2

actionDic = {
    0: "UP",
    1: "DOWN",
    2: "LEFT",
    3: "RIGHT"
}

(TOUR_JOUEUR, TOUR_ORDI) = (0, 1)

# simuler un joueur qui effectue le mouvement dans l’ordre de haut, bas, gauche et droite
class Test:
    def __init__(self):
        self.grille = Grille()
        self.afficher = None
        self.ordiAI = None
        self.over = False

    def setOrdiAI(self, ordiAI):
        self.ordiAI = ordiAI

    def setAfficher(self, afficher ):
        self.afficher  = afficher

    # Insertion aléatoire de tuiles
    def insertRandonTile(self) :
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

        tour = TOUR_JOUEUR
        j = -1

        nbmoves = 0

        while not self.gameOver() and not self.over:
            # Cloner pour s'assurer que l'IA ne peut pas changer la vraie grille
            grilleClone = self.grille.clone()

            if tour == TOUR_JOUEUR:
                #mouvement = self.grille.getMovePossible()
                #move = mouvement[j]
                j += 1
                move = j

                if j == 3:
                    j=-1


                print("Mouvement de joueur:", end="")
                print(actionDic[move])

                if self.grille.movePossible([move]):
                    self.grille.move(move)
                    nbmoves +=1

                    maxVal = self.grille.getMaxVal()

                    # Valeur pour ganger
                    if maxVal == 256:
                        self.over = True
                        self.afficher.afficheGrille(self.grille)
                        print("Gagner!")
                        break

                else:
                    self.over = True
                    print("Grille plein, échouer!")
            else:
                print("Nouvelles tuiles créées par ordi:")
                move = self.ordiAI.getMove(grilleClone)
                # Validate Move
                if move and self.grille.inserPossible(move):
                    self.grille.setValeur(move, self.newTuileVal())
                else:
                    self.over = True

            if not self.over:
                self.afficher.afficheGrille(self.grille)
                time.sleep(0.2)
                ######################
                print(time.perf_counter())
                print("nb de mouvement :", nbmoves)
            tour = 1 - tour




def main():
    test = Test()
    ordiAI = OrdiAI()
    afficher = Afficher()
    test.setAfficher (afficher)
    test.setOrdiAI(ordiAI)

    test.start()

if __name__ == '__main__':
    main()




