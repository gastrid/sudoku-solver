# -*-coding:Utf-8 -*

from sudoku import Sudoku

string = "005280000000004100009000403900700060080010040050009001406000200007400000000025600"

sud = Sudoku()

sud.stringToCell(string)

sud.printLeft()
print(sud)

sud.solve()



# Ideas:
# - [performance] add a field in block listing the remaining numbers to be found in that block.






