# -*-coding:Utf-8 -*

from sudoku import Sudoku
import memory_profiler


@profile
def t_func():

    string = "460805003003070000075901060084000070900706001030000650090402830000080500300509027"

    sud = Sudoku()

    sud.stringToCell(string)
    print(sud)

    sud.solve()

    abv = 23405934703458

    print("")
    print(sud)

if __name__ == '__main__':
    t_func()


