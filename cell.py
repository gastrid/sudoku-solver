

class Cell:


    def __init__(self, row, col, square, number, initial):
        self.row = row
        self.col = col
        self.square = square
        self.number = self.verify(number)
        self.initial = initial

    def verify(self, entry):
        try:
            entry = int(entry)
        except:
            print "the value you entered is not a number."
        if entry > 9 & entry < 0:
            raise ValueError("The value you entered, {0}, is not between 0 and 9".format(entry))
        return entry


class Block(dict):

    def __setitem__(self, key, value):
        if type(value) is Cell:
            if key <= 9 & key >= 1:
                dict.__setitem__(self, key, value)
            else:
                raise ValueError("The dictionary key is incorrect.")
        else:
            raise ValueError("The entry value is not type Cell.")


