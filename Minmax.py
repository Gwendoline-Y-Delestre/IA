# JoueurAI.py

import time

timeLimit = 0.2


def h(grille):
    # renvoie la valeur de hachage de l'objet (tuple)
    return hash(tuple([tuple(x) for x in grille.map]))


class Minmax():

    def getMove(self, grille):
        '''
            UP 0
            DOWN 1
            LEFT 2
            RIGHT 3
        '''
        self.startTime = time.perf_counter()
        self.depthLimit = 6 # Profondeur de recherche
        self.heuristique = dict()
        self.filsMaxDict = dict()
        self.filsMinDict = dict()

        bestMove = None

        while not self.timeOver():
            move, _, _ = self.maximiser(grille, 1)
            if not self.timeOver() or bestMove is None:
                bestMove = move
        return bestMove


    ## Algorithme MinMax

    #Trouve la plus grande utilité(valeur du noeud) pour le joueur
    def maximiser(self, grille, depth):
        if depth > self.depthLimit: #si fini ou la profondeur de recherche atteint le maximum
            return None, None, self.evaluation(grille)
        key = h(grille) #  Obtenez le hachage de la grille
        if key not in self.filsMaxDict:
            mouvement = grille.getMovePossible() # trouver des mouvement possible
            if not mouvement: # pas de mouvement possible
                return None, None, self.evaluation(grille)
            filsList = []
            for move in mouvement:
                fils = grille.clone() # cloner la grille
                fils.move(move) # Simuler les mouvements sur les grilles clones
                filsList.append([fils, move]) # Ajouter le mouvement à la liste fils
            self.filsMaxDict[key] = filsList

        filsMax, noeudMax = None, float('-inf') # initialiser fils et la valeur de noeud max

        for fils in self.filsMaxDict[key]:
            # Obtenir la valeur du noeud au niveau suivant (profondeur de recherche)
            _, _, noeud = self.minimiser(fils[0],depth + 1)

            if noeud > noeudMax:
                bestMove, filsMax, noeudMax = fils[1], fils[0], noeud # Mises à jour


        return bestMove, filsMax, noeudMax


    # Trouve la plus petite utilité pour l' ordinateur qui mis les tuiles aléatoires
    def minimiser(self, grille, depth):
        if depth > self.depthLimit:
            return None, None, self.evaluation(grille)

        key = h(grille)
        if key not in self.filsMinDict:
            cellVide = grille.getCellVide()
            if not cellVide:
                return None, None, self.evaluation(grille)
            filsList = []
            for cell in cellVide:
                fils2 = grille.clone()
                fils2.inserTuile(cell, 2)
                filsList.append(fils2)

                fils4 = grille.clone()
                fils4.inserTuile(cell, 4)
                filsList.append(fils4)

            self.filsMinDict[key] = filsList

        filsMax, noeudMin = None, float('inf')

        ### Algorithme α-β
        for fils in self.filsMinDict[key]:
            _, _, noeud = self.maximiser(fils, depth + 1)

            if noeud < noeudMin:
                _, filsMin, noeudMin = _, fils, noeud

        return _, filsMin, noeudMin

    # Évaluer le score du mouvement
    def evaluation(self, grille):
        key = h(grille)
        if key in self.heuristique:
            return self.heuristique[key]

        score = 0
        for i in range(4):
            for j in range(4):
                # calculer la valeur des tuiles et multiplier par un coefficient
# Signification du coefficient : Les positions dans le coin supérieur gauche et ses deux côtés adjacents ont des scores plus élevés
                score += grille.map[i][j] * (i + j)

        cellVide = len(grille.getCellVide())
        score -= score / (cellVide + 1) # +1 : évider la division à zero
        # plus il y a de cellules vides, plus le score soustrait est petit

        if not grille.movePossible():
            score -= 2 * grille.getMaxVal() # déduction de score

        self.heuristique[key] = score
        return score


    def timeOver(self):
        return self.startTime + timeLimit <= time.perf_counter()



