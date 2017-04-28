from cell import Cell, Block

class Sudoku:

    def __init__(self, sudoku_string):
        self._cells = []
        self._cols = []
        self._rows = []
        self._squares = []
        self.makeElms()

    def makeElms(self):
        for i in range(0, 9):
            for j in range (0, 9):
                self._cells.append(Cell())
            self._cols.append(Block())
            self._rows.append(Block())



    def stringToCell(self, sudoku_string):
        col = 0
        col_i = 0
        row = 0
        row_i = 0
        square = 0
        square_i = 0

        for index, nb in sudoku_string:
            initial = False
            if nb != 0:
                initial = True
            cell = Cell(self._rows[row], self._cols[col], self._squares[square], initial)
            self._rows[row][row_i] = cell
            self._cols[col][col_i] = cell
            self._squares[square][square_i] = cell




