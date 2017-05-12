# -*-coding:Utf-8 -*

import memory_profiler

from cell import Cell, Block

class Sudoku:

    def __init__(self,):
        self._cells = []
        self._cols = []
        self._rows = []
        self._squares = []
        self.makeElms()

    @profile
    def makeElms(self):
        for i in range(0, 9):
            self._cols.append(Block(i))
            self._rows.append(Block(i))
            self._squares.append(Block(i))


    @profile
    def stringToCell(self, sudoku_string):
        if len(sudoku_string) != 81:
            raise ValueError("You have not entered the right number of digits.")

        # The column number -- 0-8
        col = 0
        # The position inside the column -- 0-8
        col_i = 0
        # The row number -- 0-8
        row = 0
        # The position inside the row -- 0-8
        row_i = 0
        # The square number  -- 0-8
        square = 0
        # The horizontal position of the square in the sudoku  -- 0-2
        square_i = 0
        # The horizontal position in the square  -- 0-2
        square_j = 0
        # The vertical position in the square  -- 0-2
        square_k = 0

        square_pos = 0

        for nb in sudoku_string:
            try:
                number = int(nb)
            except:
                raise ValueError("What you entered was not a number.")

            initial = False
            if (number != 0):
                initial = True
            cell = Cell(self._rows[row], self._cols[col], self._squares[square], number, initial)
            self._cells.append(cell)
            self._rows[row][row_i] = cell
            self._cols[col][col_i] = cell
            self._squares[square][square_pos] = cell

            col += 1
            if col > 8:
                col_i += 1
                col = 0

            row_i += 1
            if row_i > 8:
                row += 1
                row_i = 0

            square_j += 1
            square_pos += 1
            if square_j > 2:
                square += 1
                square_i += 1
                square_j = 0
                square_pos -= 3
                if square_i > 2:
                    square_k += 1
                    square_pos += 3
                    if square_k > 2:
                        square_k = 0
                        square_pos = 0
                    else:
                        square -= 3
                    square_i = 0



    def __repr__(self):
        top = "|-------------------------------------------------------|| \n"
        bottom = "--------------------------------------------------------||"
        cont = ""

        for i in range(0, 9):
            row_string = "|"
            for j in range(0, 9):
                row_string += "  " + str(self._rows[i][j].number)
                if (j + 1) % 3 == 0:
                    row_string += "  ||"
                else:
                    row_string += "  ¦"
            row_string += "\n"
            cont += row_string
            if i == 8:
                pass
            elif (i + 1) % 3 == 0:
                cont += "|=====|=====|=====||=====|=====|=====||=====|=====|=====|| \n"
            else:
                cont += "|-----|-----|-----||-----|-----|-----||-----|-----|-----|| \n"

        return top + cont + bottom

    @profile
    def solve(self):
        i = 0
        j = 0
        k = 0
        back = False
        while i < 81:
            if i < 0:
                self.negativesDiagnosis()
                raise IndexError("Something went seriously wrong: your code is checking negative cells")
            i = self.isInitial(i, back)
            if i > 80:
                return
            cell = self._cells[i]
            result = self.addAndCheck(cell)
            if result == True:
                if k % 10 != 0:
                    print("[{}]".format(j), end='')
                else:
                    print("[{}]".format(j))
                k += 1
                back = False
                i += 1
            else:
                cell.number = 0
                back = True
                i -= 1
            j += 1



        print("")
        return

    def isInitial(self, i, back):
        if self._cells[i].initial == True:
                if back:
                    i -= 1
                else:
                    i += 1
                if i < 81:
                    i = self.isInitial(i, back)
        return i


    def addAndCheck(self, cell):
        if cell.number < 9:
            cell.number += 1
            valid = self.checkValid(cell)
            if valid == False:
               result = self.addAndCheck(cell)
               return result
            else:
                return True
        else:
            return False

    def checkValid(self, cell):
        singleInRow = self.checkGroup(cell, cell.row)
        if singleInRow == False:
            return False

        singleInCol = self.checkGroup(cell, cell.col)
        if singleInCol == False:
            return False

        singleInSquare = self.checkGroup(cell, cell.square)
        if singleInSquare == False:
            return False

        return True

    def checkGroup(self, cell, group):
        for k, nCell in group.items():
            if (nCell.number == cell.number) & (nCell != cell):
                return False
        return True

    def negativesDiagnosis(self):
        print("We've entered the diagnosis centre")
        for c in self._cells:
            if c.initial == False & c.number != 0:
                print("This cell col {0}, row {1}, value {2}".format(c.col, c.row, c.number))




