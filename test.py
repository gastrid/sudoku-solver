# -*-coding:Utf-8 -*

from sudoku import Sudoku

string = "604000008008045700000008001060010300000809000001060070400900000002530900100000802"

sud = Sudoku()

sud.stringToCell(string)

print(sud)

sud.solve()

print(sud)



