# Grille.py
from copy import deepcopy

vecDirection = (UP_VEC, DOWN_VEC, LEFT_VEC, RIGHT_VEC) = ((-1, 0), (1, 0), (0, -1), (0, 1))
vecIndex = [UP, DOWN, LEFT, RIGHT] = range(4)


class Grille:
    def __init__(self):
        '''
            UP = 0
            DOWN = 1
            LEFT = 2
            RIGHT = 3
        '''
        self.map = [[0] * 4 for i in range(4)]


    # Faire un deepcopy de grille
    def clone(self):
        cloneGrille = Grille()
        cloneGrille.map = deepcopy(self.map)
        return cloneGrille

    # renvoi des cellules vides
    def getCellVide(self):
        cell = []
        for x in range(4):
            for y in range(4):
                if self.map[x][y] == 0:
                    cell.append((x, y))
        return cell

    # Vérifier la posibilité d'insérer une tuile dans la position
    def inserPossible(self, pos):
        return self.getCellVal(pos) == 0

    # Insérer une tuile dans une cellule vide
    def inserTuile(self, pos, val):
        self.setValeur(pos, val)

    def setValeur(self, pos, val):
        self.map[pos[0]][pos[1]] = val

    # renvoi la valeur max des tuiles
    def getMaxVal(self):
        maxVal = 0
        for x in range(4):
            for y in range(4):
                maxVal = max(maxVal, self.map[x][y])
        return maxVal

    # Mouvement de la grille
    def move(self, d):
        d = int(d)
        if d == UP:
            return self.moveU()
        if d == DOWN:
            return self.moveD()
        if d == LEFT:
            return self.moveL()
        if d == RIGHT:
            return self.moveR()


    # mouvement vers le haut
    def moveU(self):
        moved = False
        for j in range(4):
            cells = []
            for i in range(4):
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.fusionTuile(cells)
            for i in range(4):
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # mouvement vers le bas
    def moveD(self):
        moved = False
        for j in range(4):
            cells = []
            for i in range(4 - 1, -1, -1):
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.fusionTuile(cells)
            for i in range(4 - 1, -1, -1):
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # mouvement vers la gauche
    def moveL(self):
        moved = False
        for i in range(4):
            cells = []
            for j in range(4):
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.fusionTuile(cells)
            for j in range(4):
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved

    # mouvement vers la droite
    def moveR(self):
        moved = False
        for i in range(4):
            cells = []
            for j in range(4 - 1, -1, -1):
                cell = self.map[i][j]
                if cell != 0:
                    cells.append(cell)
            self.fusionTuile(cells)
            for j in range(4 - 1, -1, -1):
                value = cells.pop(0) if cells else 0
                if self.map[i][j] != value:
                    moved = True
                self.map[i][j] = value
        return moved


    # Fusionner des tuiles
    def fusionTuile(self, cell):
        if len(cell) <= 1:
            return cell
        i = 0
        while i < len(cell) - 1:
            if cell[i] == cell[i + 1]:
                cell[i] *= 2 # fusionner
                del cell[i + 1]
            i += 1

    # Vérifier s'il y a un mouvement possible
    def movePossible(self, dirs=vecIndex):
        checkingMoves = set(dirs)
        for x in range(4):
            for y in range(4):
                if self.map[x][y]:  # Si la cellule actuelle est remplie
                    for i in checkingMoves: # Vérifier la valeur de la cellule adjacente
                        move = vecDirection[i]
                        adjCellValue = self.getCellVal((x + move[0], y + move[1]))
                        # Si la valeur est la même ou si la cellule adjacente est vide
                        if adjCellValue == self.map[x][y] or adjCellValue == 0:
                            return True
                # Else if la cellule actuelle est vide
                elif self.map[x][y] == 0:
                    return True
        return False

    # Voir tous les mouvements disponibles
    def getMovePossible(self, dirs=vecIndex):
        movepossible = []
        for i in dirs:
            gridCopy = self.clone()
            if gridCopy.move(i):
                movepossible.append(i)
        return movepossible

    def getCellVal(self, pos):
        if not (pos[0] < 0 or pos[0] >= 4 or pos[1] < 0 or pos[1] >= 4):
            return self.map[pos[0]][pos[1]]
        else:
            return None


