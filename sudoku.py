from cell import Cell

class Sudoku:

    def __init__(self, sudoku_string):
        self._cells = []
        self._cols = []
        self._rows = []
        self._squares = []

    def stringToCell(self, sudoku_string):
        col = 1
        col_i = 0
        row = 1
        square = 1
        square_i = 0
        for index, nb in sudoku_string:
            cell = Cell()

    