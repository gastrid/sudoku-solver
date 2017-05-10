# -*-coding:Utf-8 -*

from cell import Cell, Block

class Sudoku:

    def __init__(self,):
        self._cells = []
        self._cols = []
        self._rows = []
        self._squares = []
        self.makeElms()
        self.left = 0

    def makeElms(self):
        for i in range(0, 9):
            self._cols.append(Block(i))
            self._rows.append(Block(i))
            self._squares.append(Block(i))


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


    def solve(self):

        # First strategy -- No errors
        for cell in filter(lambda x: x.initial is False, self._cells):
            if cell == self._cells[28]:
                print("hered")
            self.populateList(cell)
            self.singleNumber(cell)
        self.printLeft()
        print(self)



        for i in range(0, 3):

            # Second Strategy
            for row in self._rows:
                self.singleInGroup(row)
            for col in self._cols:
                self.singleInGroup(col)
            for square in self._squares:
                self.singleInGroup(square)
            self.printLeft()
            print(self)

            print(self._cells[6]._possibleList)

            # Repeat singleNumber
            for cell in filter(lambda c: c.number == 0, self._cells):
                self.singleNumber(cell)

            self.printLeft()
            print(self)

            # Third strategy - not sure it's that effective
            # Not working for the moment !!!!!!!
            for square in self._squares:
                self.squareToColRow(square)

            for row in self._rows:
                self.rowToSquare(row)

            for col in self._cols:
                self.colToSquare(col)


            # Repeat singleNumber
            for cell in filter(lambda c: c.number == 0, self._cells):
                self.singleNumber(cell)



            self.printLeft()
            print(self)


    #    could be reduced immensely with group possibleList
    def doubleExclusive(self, group):
        for n in group.leftNumbers:
            for m in group.leftNumbers:
                if n != m:
                    cellsN = []
                    cellsM = []
                    for cell in group.leftCells:
                        if n in cell._possibleList:
                            cellsN.append(cell)
                        if m in cell._possibleList:
                            cellsM.append(cell)
                        if cellsM == cellsN:

        for n in range(1, 10):
            for m in range(1, 10):
                if n != m:
                    taken = False
                    for k, cell in group.items():
                        if cell.number == n or cell.number == m:
                            taken = True
                    if taken == False:
                        cellsN = []
                        cellsM = []
                        for k, cell in group.items():
                            if n in cell._possibleList:
                                cellsN.append(cell)
                            if m in cell._possibleList:
                                cellsM.append(cell)
                        if cellsM == cellsN:
                            # remove anything that's not m or n.




    def singleInGroup(self, group):
        for n in range(1, 10):
            total = 0
            singleCell = 0
            for k, cell in group.items():
                if cell.number == 0:
                    if n in cell._possibleDict:
                        total += 1
                        singleCell = cell
            if total == 1:
                singleCell.changeNumber(n)
                self.cleanLine(singleCell)


    def singleInLine(self, cell):
        number = 0
        for n in cell._possibleDict:
            single = True
            for k, nCell in cell.row.items():
                if n in nCell._possibleList:
                    single = False
            for k, nCell in cell.row.items():
                if n in nCell._possibleList:
                    single = False
            for k, nCell in cell.row.items():
                if n in nCell._possibleList:
                    single = False
            if single is True:
                number = n
        if number != 0:
            cell.changeNumber(number)
            self.cleanLine(cell)

    def squareToColRow(self, square):
        for n in range(1, 10):
            cells = []
            for k, cell in square.items():
                if n in cell._possibleList:
                    cells.append(cell)
            if len(cells) > 0 & len(cells) < 4:
                if all(c.row == cells[0].row for c in cells):
                    self.straightenRow(cells[0].row, square, n)
                if all(c.col == cells[0].col for c in cells):
                    self.straightenCol(cells[0].col, square, n)

    def colToSquare(self, col):
        for n in range(1, 10):
            cells = []
            for k, cell in col.items():
                if n in cell._possibleList:
                    cells.append(cell)
            if len(cells) > 0 & len(cells) < 4:
                if all(c.row == cells[0].square for c in cells):
                    self.straightenSquare(col, cells[0].square, n)

    def rowToSquare(self, row):
        for n in range(1, 10):
            cells = []
            for k, cell in row.items():
                if n in cell._possibleList:
                    cells.append(cell)
            if len(cells) > 0 & len(cells) < 4:
                if all(c.row == cells[0].square for c in cells):
                    self.straightenSquare(row, cells[0].square, n)


    def straightenSquare(self, square, colRow, number):
        for k, cell in colRow.items():
            if (cell.square != square) & (number in cell._possibleList):
                cell.removeFromPossible(number)

    def straightenCol(self, col, square, number):
        for k, cell in square.items():
            if (cell.col != col) & (number in cell._possibleList):
                cell.removeFromPossible(number)

    def straightenRow(self, row, square, number):
        for k, cell in square.items():
            if (cell.row != row) & (number in cell._possibleList):
                cell.removeFromPossible(number)


    def populateList(self, cell):
        for n in range(1, 10):
            single = True
            for k, nCell in cell.row.items():
                if nCell.number == n:
                    single = False
            for k, nCell in cell.col.items():
                if nCell.number == n:
                    single = False
            for k, nCell in cell.square.items():
                if nCell.number == n:
                    single = False
            if single:
                cell.addToPossible(n)

    def singleNumber(self, cell):
        if cell.nOfPossibilities() == 1:
            cell.changeNumber(cell._possibleList[0])
            self.cleanLine(cell)


    def cleanLine(self, cell):
        self.cleanGroup(cell, cell.row)
        self.cleanGroup(cell, cell.col)
        self.cleanGroup(cell, cell.square)


    def cleanGroup(self, cell, group):
        for k, nCell in group.items():
            if cell.number in nCell._possibleDict:
                nCell.removeFromPossible(cell.number)


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

    def printLeft(self):
        left = 0
        for cell in self._cells:
            if cell.number == 0:
                left += 1
        print(left)




