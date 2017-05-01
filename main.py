# -*-coding:Utf-8 -*

from sudoku import Sudoku

yes = ""

while yes != "yes":
    string = input("Enter your sudoku string > ")

    sud = Sudoku()

    sud.stringToCell(string)

    print(sud)

    yes = input("Is this what you want to solve? (yes/no)").lower()

    if yes == "yes":
        sud.solve()
        print(sud)


