# -*-coding:Utf-8 -*

from sudoku import Sudoku
import memory_profiler


@profile
def function():

    string = "350400108800007000004001000048705001010080030900604850000100300000200009702003016"

    sud = Sudoku()

    sud.stringToCell(string)

    print(sud)

    sud.solve()

    print("")
    print(sud)



