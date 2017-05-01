# -*-coding:Utf-8 -*

from sudoku import Sudoku

string = "004080300000003042800405907302070508050000070608090201406207009520900000007010400"

sud = Sudoku()

sud.stringToCell(string)

print(sud)

sud.solve()

print(sud)
