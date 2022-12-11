# JoueurAI.py



def h(grille):
    # renvoie la valeur de hachage de l'objet (tuple)
    return hash(tuple([tuple(x) for x in grille.map]))


class JoueurAI():

    def getMove(self, grille):
        '''
            UP 0
            DOWN 1
            LEFT 2
            RIGHT 3
        '''
        self.depthLimit = 6 # Profondeur de recherche
        self.heuristique = dict()
        self.filsMaxDict = dict()
        self.filsMinDict = dict()

        move, _, _ = self.maximiser(grille, float('-inf'), float('inf'), 1)

        return move


    ## Algorithme MinMax

    #Trouve la plus grande utilité(valeur du noeud) pour le joueur
    def maximiser(self, grille, alpha, beta, depth):
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

        ### Algorithme α-β
        for fils in self.filsMaxDict[key]:
            # Obtenir la valeur du noeud au niveau suivant (profondeur de recherche)
            _, _, noeud = self.minimiser(fils[0], alpha, beta, depth + 1)

            if noeud > noeudMax:
                bestMove, filsMax, noeudMax = fils[1], fils[0], noeud # Mises à jour

            if noeudMax >= beta: # α > β, pas besoin d’être explorée
                break

            if noeudMax > alpha:
                alpha = noeudMax # Mises à jour le score minimum

        return bestMove, filsMax, noeudMax


    # Trouve la plus petite utilité pour l' ordinateur qui mis les tuiles aléatoires
    def minimiser(self, grille, alpha, beta, depth):
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
            _, _, noeud = self.maximiser(fils, alpha, beta, depth + 1)

            if noeud < noeudMin:
                _, filsMin, noeudMin = _, fils, noeud

            if noeudMin <= alpha: # β < α, pas besoin d’être explorée
                break

            if noeudMin < beta:
                beta = noeudMin # Mises à jour le score maximum

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
        score += cellVide
        # plus il y a de cellules vides, plus le score est grand

        if not grille.movePossible():
            score = 0

        self.heuristique[key] = score
        return score




