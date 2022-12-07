# OrdiAI.py
from random import randint

class OrdiAI():
    def getMove(self, grid):
        cells = grid.getCellVide()
        return cells[randint(0, len(cells) - 1)] if cells else None

