

class Cell:


    def __init__(self, row, col, square, number, initial):
        self.row = row
        self.col = col
        self.square = square
        self.number = self.verify(number)
        self.initial = initial
        self._possibleDict = {}
        self._possibleList = []
        self.fillPossible()
    #     Potentially add a lock when possible is "paired" with another one?

    def verify(self, entry):
        try:
            entry = int(entry)
        except:
            print ("the value you entered is not a number.")
        if entry > 9 & entry < 0:
            raise ValueError("The value you entered, {0}, is not between 0 and 9".format(entry))
        return entry

    def __repr__(self):
        if self.number == 0:
            return " "
        return str(self.number)

    def __str__(self):
        return str(self.number)

    def fillPossible(self):
        if self.number == 0:
            self.row.leftCells.append(self)
            self.col.leftCells.append(self)
            self.square.leftCells.append(self)

    def removePossible(self):
            self.row.leftCells.remove(self)
            self.col.leftCells.remove(self)
            self.square.leftCells.remove(self)


    def addToPossible(self, number):
        number = self.verify(number)
        self._possibleDict[number] = True
        self._possibleList.append(number)
        if number not in self.row.leftNumbers:
            self.row.leftNumbers.append(number)
        if number not in self.col.leftNumbers:
            self.col.leftNumbers.append(number)
        if number not in self.square.leftNumbers:
            self.square.leftNumbers.append(number)

    def removeFromPossible(self, number):
        del(self._possibleDict[number])
        self._possibleList.remove(number)

    def delPossible(self):
        self._possibleDict = {}
        self._possibleList = []

    def nOfPossibilities(self):
        return len(self._possibleList)



    def changeNumber(self, number):
        number = self.verify(number)
        # Is that necessary?
        if number not in self._possibleList:
            raise IndexError('The number {0} is not in the range of possiblities'.format(number))
        else:
            self.number = number
            self.delPossible()
            self.row.leftNumbers.remove(number)
            self.col.leftNumbers.remove(number)
            self.square.leftNumbers.remove(number)
            self.removePossible()



class Block(dict):

    def __init__(self, pos):
        self.pos = pos
        self.leftCells = []
        self.leftNumbers = []

    def __setitem__(self, key, value):
        if type(value) is Cell:
            if (key <= 8) & (key >= 0):
                dict.__setitem__(self, key, value)
            else:
                raise ValueError("The dictionary key {} (with value {}) is incorrect.".format(key, value))
        else:
            raise ValueError("The entry value is not type Cell.")


