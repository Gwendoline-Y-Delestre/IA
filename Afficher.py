# Afficher.py
from BaseAffiche import BaseAffiche


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

cTemp = "\x1b[%dm%7s\x1b[0m "


class Afficher(BaseAffiche):
    def __init__(self):

            self.afficheGrille = self.grilleAffiche

    def afficher(self, grille):
        pass

    def grilleAffiche(self, grille):
        for i in range(3 * grille.size):
            for j in range(grille.size):
                v = grille.map[int(i / 3)][j]
                if i % 3 == 1:
                    string = str(v).center(7, " ")
                else:
                    string = " " # afficher les espaces entre les lignes

                print(cTemp % (colorMap[v], string), end="")

            print("")
            if i % 3 == 2:
                print("") # afficher les espaces entre les lignes

