

class Cell:


    def __init__(self, row, col, square, number, initial):
        self.row = row
        self.col = col
        self.square = square
        self.number = self.verify(number)
        self.initial = initial
        self._possible = []
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

    def addToPossible(self, number):
        number = self.verify(number)
        self._possible.append(number)

    def changeNumber(self, number):
        number = self.verify(number)
        # Is that necessary?
        if number not in self._possible:
            raise IndexError("This number is not in the range of possiblities")
        else:
            self.number = number



class Block(dict):

    def __init__(self, pos):
        self.pos = pos

    def __setitem__(self, key, value):
        if type(value) is Cell:
            if (key <= 8) & (key >= 0):
                dict.__setitem__(self, key, value)
            else:
                raise ValueError("The dictionary key {} (with value {}) is incorrect.".format(key, value))
        else:
            raise ValueError("The entry value is not type Cell.")


