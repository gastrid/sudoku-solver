# -*-coding:Utf-8 -*

from sudoku import Sudoku

string = input("Enter your sudoku string > ")

sud = Sudoku()

sud.stringToCell(string)

print(sud)

for cell in sud._cells:
    if cell.initial:
        print("yes")


